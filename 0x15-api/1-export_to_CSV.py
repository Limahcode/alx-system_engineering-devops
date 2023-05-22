#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using the JSONPlaceholder REST API.
"""

import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Retrieve employee information
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    # Retrieve employee's TODO list
    todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create a list to store the CSV data
    csv_data = []

    # Iterate over the TODO list and extract relevant information
    for task in todos_data:
        task_id = task['id']
        task_title = task['title']
        task_completed = task['completed']

        # Create a row of CSV data
        csv_row = [employee_id, employee_data['username'], task_completed, task_title]
        csv_data.append(csv_row)

    # Define the CSV file path
    csv_file = f"employee_{employee_id}_tasks.csv"

    # Write the CSV data to a file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])  # Write the header
        writer.writerows(csv_data)  # Write the data rows

    print(f"CSV file '{csv_file}' has been generated.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

