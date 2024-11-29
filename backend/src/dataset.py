import pandas
import csv

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

def get_combined_data_for_cbf():
    return 0