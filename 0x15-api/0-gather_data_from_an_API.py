#!/usr/bin/python3

"""
This script retrieves information about an employee's TODO list progress
using the JSONPlaceholder REST API.
"""

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

    # Count the number of completed tasks
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    number_of_completed_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    # Display the employee TODO list progress
    print(f"Employee {employee_data['name']} is done with tasks "
          f"({number_of_completed_tasks}/{total_number_of_tasks}):")

    # Display the titles of completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_progress.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)

