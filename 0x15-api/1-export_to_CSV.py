#!/usr/bin/python3
"""
'1-export_to_CSV' is a script that:
* Takes in a cmd line argument,
* Utilizes it as 'USER_ID'
* Retrieves associated informations from a web resource
* Generates a Custom View

* Exports the result in a CSV file ('USER_ID.csv') formatted as:
    "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
"""
import requests
import sys
import csv


if len(sys.argv) != 2:
    print("Usage: ./1-export_to_csv <user_id>")
else:
    user_id = sys.argv[1]
    resource = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(resource).json()

    user_tasks = []
    for data in response:
        if data.get('userId') == int(user_id):
            user_tasks.append(data)

    tasks_done = []
    tasks_todo = []
    for task in user_tasks:
        if task.get('completed'):
            tasks_done.append(task)
        else:
            tasks_todo.append(task)

    resource = 'https://jsonplaceholder.typicode.com/users/'
    url = resource + user_id
    response = requests.get(url).json()
    user_name = response.get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        user_name, len(tasks_done), len(user_tasks)))
    for task in tasks_done:
        print("\t {}".format(
            task.get('title')))

    filename = user_id + ".csv"
    with open(filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for task in user_tasks:
            writer.writerow([task.get('userId'), user_name,
                            task.get('completed'), task.get('title')])

    print(filename)
    print("USER_ID USERNAME TASK_COMPLETED_STATUS TASK_TITLE")
