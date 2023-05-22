#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using the JSONPlaceholder REST API.
"""

import json
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

    # Create a list to store the JSON data
    json_data = []

    # Iterate over the TODO list and extract relevant information
    for task in todos_data:
        task_title = task['title']
        task_completed = task['completed']

        # Create a dictionary with task information
        task_info = {
            "task": task_title,
            "completed": task_completed,
            "username": employee_data['username']
        }

        # Append the task information to the JSON data
        json_data.append(task_info)

    # Create a dictionary with the final JSON structure
    json_output = {
        "USER_ID": json_data
    }

    # Convert the JSON data to a string
    json_string = json.dumps(json_output, indent=4)

    # Print the JSON data
    print(json_string)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

