import os
import json
import csv

def json_to_csv(json_file_path, csv_file_path, properties_to_drop):
    """Convert a json file into a csv file. Each json object is stored in one row in csv.
    Drop properties not interested in."""

    with open(json_file_path, "r", encoding="utf-8") as json_file:
        data = [json.loads(line) for line in json_file]

    filtered_data = [
        {key: value for key, value in entry.items() if key not in properties_to_drop}
        for entry in data
    ]

    with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        header = list(filtered_data[0].keys())

        for entry in filtered_data:
            row_values = [entry[key] for key in header]
            csv_writer.writerow(row_values)


if __name__ == "__main__":
    base_dir = "data"
    business_json_path = os.path.join(base_dir, "yelp_academic_dataset_business.json")
    business_csv_path = os.path.join(base_dir, "business.csv")

    os.makedirs(base_dir, exist_ok=True)

    properties_to_drop = ["attributes", "hours"]

    json_to_csv(business_json_path, business_csv_path, properties_to_drop)
