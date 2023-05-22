#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using the JSONPlaceholder REST API.
"""

import json
import requests
import sys

def get_employee_todo_progress():
    # Retrieve all employees
    employees_url = 'https://jsonplaceholder.typicode.com/users'
    employees_response = requests.get(employees_url)
    employees_data = employees_response.json()

    # Create a dictionary to store the JSON data
    json_output = {}

    # Iterate over the employees
    for employee in employees_data:
        employee_id = employee['id']
        employee_username = employee['username']

        # Retrieve employee's TODO list
        todos_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Create a list to store the tasks for the current employee
        tasks = []

        # Iterate over the TODO list and extract relevant information
        for task in todos_data:
            task_title = task['title']
            task_completed = task['completed']

            # Create a dictionary with task information
            task_info = {
                "username": employee_username,
                "task": task_title,
                "completed": task_completed
            }

            # Append the task information to the list of tasks
            tasks.append(task_info)

        # Update the JSON output with the tasks for the current employee
        json_output[str(employee_id)] = tasks

    # Convert the JSON data to a string
    json_string = json.dumps(json_output, indent=4)

    # Print the JSON data
    print(json_string)

if __name__ == "__main__":
    get_employee_todo_progress()

