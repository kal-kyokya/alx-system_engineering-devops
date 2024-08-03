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

    tasks_done = 0
    tasks_todo = 0
    for task in user_tasks:
        if task.get('completed'):
            tasks_done += 1
        else:
            tasks_todo += 1

    resource = 'https://jsonplaceholder.typicode.com/users/'
    url = resource + id
    response = requests.get(url).json()
    user_name = response.get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        user_name, tasks_done, len(user_tasks)))
    for task in user_tasks:
        print("\t {}".format(
            task.get('title')))
