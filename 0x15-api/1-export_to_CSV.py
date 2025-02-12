#!/usr/bin/python3
"""Export Data to CSV"""

from requests import get
from sys import argv


if __name__ == '__main__':
    employee_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = get(url)
    username = response.json().get('username')

    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = get(url)
    tasks = response.json()
    with open('{}.csv'.format(employee_id), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_id, username, task.get('completed'),
                               task.get('title')))
