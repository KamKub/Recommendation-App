from database import get_or_create_collection, get_data_from_collection
from dataset import get_user_ratings
from sklearn.linear_model import LinearRegression 
import pandas

class Cbf_model:
  def __init__(self, user_id):

    self.user_data = get_user_ratings(user_id=user_id)
    self.collection = get_or_create_collection("tv_series_rag", "rag")
    self.watched_ids = [row['tv_series_id'] for row in self.user_data]
    ratings = [row['rating'] for row in self.user_data]

    results = get_data_from_collection(self.collection, self.watched_ids)

    self.model = LinearRegression()
    self.model.fit(results["embeddings"], ratings)

  def recommend_series(self):
    all_data = get_data_from_collection(self.collection)
    
    all_ids = [item for item in all_data["ids"]]
    not_watched_ids = [item for item in all_ids if item not in self.watched_ids]

    not_watched_data = get_data_from_collection(self.collection, not_watched_ids)

    predictions = self.model.predict(not_watched_data["embeddings"])
    titles = [item["name"] for item in not_watched_data["metadatas"]]

    df = pandas.DataFrame({
    'title': titles,
    'prediction': predictions
    })

    return df.sort_values(by='prediction', ascending=False)

