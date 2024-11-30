# Python-Data-Science-Session5

## Overview

This repository contains the exercises and solutions for Session 5 of Python Data Science. The session focuses on working with JSON, Pickle, and Parquet file formats, along with regular expressions and datetime libraries, using the annotations data processed in Session 4.

## Contents

- `exercise_zip_file_2.py`: The main Python script containing solutions for all the exercises.
- `annotations_by_month.json`: JSON file containing annotation names grouped by month.
- `annotations_by_month.pkl`: Pickle file containing the same data as the JSON file.
- `annotations_with_dates.json`: JSON file containing annotation names and their corresponding dates as `datetime` objects.

## Exercise Description

The exercises reuse the same annotation files from Session 4 and involve the following tasks:

1. **Annotations per Month and Year**:
   - Count the total annotations per month and year.
   - Identify the month with the highest number of annotations.

2. **Monthly Dictionary**:
   - Create a dictionary where:
     - **Key**: Month (e.g., `YYYYMM`).
     - **Value**: List of all annotation names for that month.
   - Save the dictionary in both:
     - **JSON format**.
     - **Pickle format**.

3. **Enhanced Dictionary with Dates**:
   - Create a modified dictionary where each annotation is represented as:
     - **Name**: The file name.
     - **Date**: A `datetime` object corresponding to the annotation's date.

4. **Sorting by Date**:
   - Print all annotations from **July 2024 onward**, sorted from the oldest to the newest.

## How to Use

### Prerequisites

- Python 3.8 or later
- Required libraries: `os`, `re`, `glob`, `json`, `pickle`, `datetime`, and `numpy`

### Steps to Run the Script

1. Clone the repository:
   git clone https://github.com/yourusername/Python-Data-Science-Session5.git
   cd Python-Data-Science-Session5
2. Ensure the annotations folder from Session 4 is correctly set up:
   /Users/lorenzoferrantin/Python-Data-Science-Session4 (example in my case)
3. Run the script:
   exercise_zip_file_2.py


