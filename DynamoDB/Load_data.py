import json
from decimal import Decimal
import boto3

client = boto3.resource('dynamodb')


def load_json_data(movies_list):
    table = client.Table('Movies')
    for movie in movies_list:
        table.put_item(Item=movie)
        print(f"The data pushed for movie title {movie['title']} & year is {movie['year']}")


with open('sample_load.json') as json_file:
    movie_list = json.load(json_file, parse_float=Decimal)
print((movie_list))

load_json_data(movie_list)