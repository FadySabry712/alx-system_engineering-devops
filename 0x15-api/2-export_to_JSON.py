#!/usr/bin/python3
""" Exports data to JSON file format """

import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    username = employee_response.json().get('username')

    t_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todos_response = requests.get(t_url)
    tasks = todos_response.json()
    dictionary = {employee_id: []}
    for task in tasks:
        dictionary[employee_id].append({
            "tasks": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })
    with open(f'{employee_id}.json', 'w') as f:
        json.dump(dictionary, f)
