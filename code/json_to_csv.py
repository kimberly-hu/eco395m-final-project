import os
import json
import csv
import pandas as pd
from tqdm import tqdm



def process_json(json_text):
    """Replace newline characters with a single space
    to avoid reading new lines in reviews as a new json object."""

    json_object = json.loads(json_text)
    json_object["text"] = json_object["text"].replace('\n', ' ')
    return json_object


def json_to_csv(input_file, output_folder, chunk_size=1000000):
    """Convert a single json file into multiple csv files. 
    Each json object is stored as a row in the csv.
    The json objects are processed and saved in chunks."""

    with open(input_file, 'r', encoding='utf-8') as file:
        json_objects = []
        file_counter = 1

        for line_number, line in tqdm(enumerate(file, start=1), desc='Processing JSON', unit='lines'):
            json_objects.append(line)

            if len(json_objects) == chunk_size:
                process_and_save_chunk(json_objects, output_folder, file_counter)
                json_objects = []
                file_counter += 1

        if json_objects:
            process_and_save_chunk(json_objects, output_folder, file_counter)


def process_and_save_chunk(json_objects, output_folder, file_counter):
    """Process and save the json object chunks."""

    processed_objects = [process_json(json_text) for json_text in json_objects]

    header = list(processed_objects[0].keys())

    filename = f"{output_folder}/review_{file_counter}.csv"

    with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=header)
        csv_writer.writerows(processed_objects)



if __name__ == "__main__":

    base_dir = "data"
    review_json_path = os.path.join(base_dir, "yelp_academic_dataset_review.json")
    review_folder = os.path.join(base_dir, "reviews")

    json_to_csv(review_json_path, review_folder, chunk_size=1000000)
