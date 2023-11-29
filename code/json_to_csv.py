import os
import json
import pandas as pd
import tqdm



def json_to_csv(json_file_path, csv_file_path):
    df = pd.read_json(json_file_path)
    total_rows = len(df)
    tqdm_bar = tqdm(total=total_rows, desc="Converting JSON to CSV", unit="row")
    df.to_csv(csv_file_path, index=False, header=False, mode='a')
    tqdm_bar.close()



if __name__ == "__main__":

    base_dir = "data"
    review_json_path = os.path.join(base_dir, "yelp_academic_dataset_review.json")
    review_csv_path = os.path.join(base_dir, "review.csv")

    json_to_csv(review_json_path, review_csv_path)
