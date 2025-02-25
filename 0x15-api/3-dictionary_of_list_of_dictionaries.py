#!/usr/bin/python3
"""Exports data of all employees in JSON format"""

from json import dump
from requests import get


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/'
    response = get(url)
    users = response.json()

    dictionary = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        response = get(url)
        tasks = response.json()
        dictionary[user_id] = []
        for task in tasks:
            dictionary[user_id].append({
                                        "task": task.get('title'),
                                        "completed": task.get('completed'),
                                        "username": username
                                        })
    with open('todo_all_employees.json', 'w') as f:
        dump(dictionary, f)
