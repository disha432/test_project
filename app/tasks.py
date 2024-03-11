 # Import Task model if applicable
from django.utils import process_csv_data  # Assuming you have a function for CSV processing
from django.utils import process_csv_data 
from django.utils import get_csv_data
from celery import Celery
import os
import validators
import csv

app = Celery('app')

@app.task
def process_csv(path_url):
  """
  Celery task function that processes a CSV file at the provided path/URL.
  """
  # Access the CSV data from the path/URL (implementation details not shown)
  csv_data = get_csv_data(path_url)
  # Process the CSV data using your utility function
  process_csv_data(csv_data)



def is_valid_file_path(path):
  """
  Checks if the provided path points to an existing file.
  """
  return os.path.isfile(path)


def is_valid_url(url):
  """
  Checks if the provided string is a valid URL format.
  """
  return validators.url(url)


def process_csv_data(csv_data):
  """
  Processes the provided CSV data (list of lists).
  """
  # Loop through each row in the CSV data
  for row in csv_data:
    # Access data within each row (columns)
    # Example: Assuming you have columns "Name", "Age", and "City"
    name = row[0]
    age = row[1]
    city = row[2]

    # Perform your processing logic here
    # Example: Print data to console
    print(f"Name: {name}, Age: {age}, City: {city}")


def get_csv_data(path_url):
  """
  Fetches CSV data from the provided path/URL.
  """
  try:
    # Check if path_url is a file path
    if os.path.isfile(path_url):
      with open(path_url, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)  # Convert reader object to a list of lists

    # Otherwise, assume it's a URL (implementation details not shown)
    # You'll need to implement logic for downloading or accessing data from the URL
    # This part might involve libraries like requests or urllib
    # ... (Implement URL handling logic)
    # return processed_data  # Replace with the processed data from the URL

  except FileNotFoundError:
    # Handle case where file is not found
    print(f"Error: File not found at {path_url}")
    return None  # Or raise an exception

  except Exception as e:
    # Handle other potential errors
    print(f"Error processing CSV data: {e}")
    return None  # Or raise an exception

 


