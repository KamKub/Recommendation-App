import pandas
import os
import csv
import random

"""
comment
"""
def get_combined_data():
    data = pandas.read_csv('dataset_1000.csv')
    data['combined_data'] = data.apply(lambda row: f"Title: {row['name']}. Overview: {row['overview']} Genre: {row['genres']}", axis=1)
    return data['combined_data'].to_list()

"""
comment
"""
def get_data_list():
    with open('dataset_1000.csv', mode='r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        data_list = list(reader)
    return data_list

"""
comment
"""
def get_user_ratings(user_id):
    filename = 'ratings.csv'
    if not os.path.exists(filename):
        print(f"Creating {filename} file.")
        user_id = 1
        data = []
        for _ in range(5):
            tv_series_id = f"id{random.randint(1, 1000)}"
            rating = round(random.uniform(0, 10), 1) 
            data.append({"user_id": user_id, "tv_series_id": tv_series_id, "rating": rating})
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['user_id', 'tv_series_id', 'rating']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
    df = pandas.read_csv(filename)
    user_df = df[df['user_id'] == user_id]

    return user_df.to_dict(orient='records')