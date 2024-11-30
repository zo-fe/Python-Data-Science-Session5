import os
import re
import glob
import json
import pickle
from datetime import datetime

# Directory containing the annotation files
annotations_dir = "/Users/lorenzoferrantin/Python-Data-Science-Session4/annotations"

# Regex pattern to validate annotation files
pattern = r"(\d{8})_(\d{6})_SN(\d+)_QUICKVIEW_VISUAL_([\d_]+)_([A-Za-z0-9\-_.]+)\.txt"

# Task 1: Count annotations per month and year
def count_annotations_by_month(annotations):
    annotations_per_month = {}
    for annotation in annotations:
        filename = os.path.basename(annotation)
        match = re.match(pattern, filename)
        if match:
            date, *_ = match.groups()
            year_month = date[:6]
            annotations_per_month[year_month] = annotations_per_month.get(year_month, 0) + 1
    return annotations_per_month

# Task 2: Create dictionary and save it in JSON and Pickle formats
def create_monthly_dict(annotations):
    monthly_dict = {}
    for annotation in annotations:
        filename = os.path.basename(annotation)
        match = re.match(pattern, filename)
        if match:
            date, *_ = match.groups()
            year_month = date[:6]
            monthly_dict.setdefault(year_month, []).append(filename)

    # Save to JSON
    with open("annotations_by_month.json", "w") as json_file:
        json.dump(monthly_dict, json_file)
    print("Saved monthly dictionary to annotations_by_month.json")

    # Save to Pickle
    with open("annotations_by_month.pkl", "wb") as pickle_file:
        pickle.dump(monthly_dict, pickle_file)
    print("Saved monthly dictionary to annotations_by_month.pkl")

    return monthly_dict

# Task 2c: Dictionary with names and dates
def create_monthly_dict_with_dates(annotations):
    monthly_dict = {}
    for annotation in annotations:
        filename = os.path.basename(annotation)
        match = re.match(pattern, filename)
        if match:
            date, time, *_ = match.groups()
            year_month = date[:6]
            datetime_obj = datetime.strptime(date + time, "%Y%m%d%H%M%S")
            monthly_dict.setdefault(year_month, []).append({
                "name": filename,
                "date": datetime_obj
            })

    # Save to JSON for verification
    with open("annotations_with_dates.json", "w") as json_file:
        json.dump(
            {k: [{"name": v["name"], "date": v["date"].strftime("%Y-%m-%d %H:%M:%S")} for v in values]
             for k, values in monthly_dict.items()},
            json_file
        )
    print("Saved annotations with dates to annotations_with_dates.json")
    return monthly_dict

# Task 3: Sort annotations from July 2024 onward
def sort_annotations_second_half(annotations):
    annotations_with_dates = []
    for annotation in annotations:
        filename = os.path.basename(annotation)
        match = re.match(pattern, filename)
        if match:
            date, time, *_ = match.groups()
            datetime_obj = datetime.strptime(date + time, "%Y%m%d%H%M%S")
            if datetime_obj >= datetime(2024, 7, 1):
                annotations_with_dates.append((filename, datetime_obj))

    # Sort annotations by date
    annotations_with_dates.sort(key=lambda x: x[1])

    print("Annotations from the second half of 2024 (sorted):")
    for name, date in annotations_with_dates:
        print(f"{name}: {date.strftime('%Y-%m-%d %H:%M:%S')}")

# Main function
def main():
    # Get all annotations
    annotations = glob.glob(f"{annotations_dir}/*.txt")

    # Task 1
    annotations_per_month = count_annotations_by_month(annotations)
    print("Annotations per month and year:", annotations_per_month)
    max_month = max(annotations_per_month, key=annotations_per_month.get)
    print(f"Month with the most annotations: {max_month} ({annotations_per_month[max_month]} files)")

    # Task 2
    monthly_dict = create_monthly_dict(annotations)

    # Task 2c
    create_monthly_dict_with_dates(annotations)

    # Task 3
    sort_annotations_second_half(annotations)

if __name__ == "__main__":
    main()
