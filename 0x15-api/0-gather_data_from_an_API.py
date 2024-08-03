#!/usr/bin/python3
"""
'0-gather_data_from_an_API' is a script that:
* Takes in a cmd line argument,
* Utilizes it as a 'path parameter'
* Retrieve information for a resource
* Generate a Custom View
"""
import requests
import sys


if len(sys.argv) != 2:
    print("Usage: ./0-gather_data_from_an_API <id>")
else:
    id = sys.argv[1]
    resource = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(resource).json()

    user_tasks = []
    for data in response:
        if data.get('userId') == int(id):
            user_tasks.append(data)

    tasks_done = []
    tasks_todo = []
    for task in user_tasks:
        if task.get('completed'):
            tasks_done.append(task)
        else:
            tasks_todo.append(task)

    resource = 'https://jsonplaceholder.typicode.com/users/'
    url = resource + id
    response = requests.get(url).json()
    name = response.get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(tasks_done), len(user_tasks)))
    for task in tasks_done:
        print("\t {}".format(
            task.get('title')))
