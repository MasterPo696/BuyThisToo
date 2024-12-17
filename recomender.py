import pandas as pd
import random
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors


class Recommender:
    def __init__(self, interactions_path, products_path):
        self.interactions_path = interactions_path
        self.products_path = products_path
        self.df_interactions = pd.read_csv(interactions_path)
        self.df_products = pd.read_csv(products_path)
        self.final_list = []

    def _calculate_ratings(self, row):
        """Helper function to calculate the rating score based on interactions."""
        rating = 0
        rating += row['is_viewed'] * 1
        rating += row['is_clicked'] * 2
        rating += row['is_added_to_cart'] * 3
        rating += row['is_purchased'] * 5
        return (rating / 11) * 5

    def _content_recommender(self, user_id):
        """Content-based recommendation system."""
        df = pd.merge(
            self.df_interactions, self.df_products, on='product_id', how='left'
        )
        df = df[df['is_purchased'] == 1]
        important_columns = ['user_id', 'product_id', 'interaction_date', 'description', 'extracted_category']
        df = df[important_columns]

        # Get user's top categories
        recommended_items = df[df['user_id'] == user_id]['extracted_category'].value_counts().reset_index()
        recommended_list = recommended_items['extracted_category'][0:3].to_list()

        def generate_content(recommended_list):
            count_random = 3
            for category in recommended_list:
                content = df[df['extracted_category'] == category]['description'].unique().tolist()
                random_elements = random.sample(content, min(len(content), count_random))
                count_random -= 1
                self.final_list.append(random_elements)

        generate_content(recommended_list)
        return self.final_list

    def _collaborative_recommender(self):
        """Collaborative filtering recommendation system."""
        # Add calculated ratings to interactions dataframe
        self.df_interactions['rating'] = self.df_interactions.apply(self._calculate_ratings, axis=1)

        df_merged = pd.merge(
            self.df_interactions[['user_id', 'product_id', 'rating']],
            self.df_products,
            on='product_id',
            how='left'
        )
        df_merged = df_merged.drop_duplicates().reset_index(drop=True)
        interaction_matrix = df_merged.pivot(index='product_id', columns='user_id', values='rating').fillna(0)

        # Train collaborative filtering model
        final_matrix = csr_matrix(interaction_matrix)
        model = NearestNeighbors(algorithm="brute")
        model.fit(final_matrix)

        # Recommend based on a random product (for demonstration)
        first_product_vector = interaction_matrix.iloc[0].values.reshape(1, -1)
        distances, suggestions = model.kneighbors(first_product_vector, n_neighbors=6)
        suggested_indices = suggestions.flatten()

        suggested_names = df_merged.iloc[suggested_indices]['name'].drop_duplicates()
        return suggested_names.tolist()

    def recommend(self, user_id):
        """Recommender function that chooses the method based on user interactions."""
        try:
            user_purchases = self.df_interactions[
                (self.df_interactions['user_id'] == user_id) & (self.df_interactions['is_purchased'] == 1)
            ]
            if len(user_purchases) > 3:
                return self._content_recommender(user_id)
            else:
                return self._collaborative_recommender()
        except Exception as e:
            print(f"Error during recommendation: {e}")
            return self._collaborative_recommender()


# Example Usage:
if __name__ == "__main__":
    recommender = Recommender(
        interactions_path="Dataset_PSnake/user_interactions.csv",
        products_path="Dataset_PSnake/final_standardized_labelled.csv"
    )
    print(recommender.recommend(723189371092873021))


