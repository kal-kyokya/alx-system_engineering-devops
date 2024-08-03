#!/usr/bin/python3
"""
'1-export_to_CSV' is a script that:
* Retrieves informations from a web resource

* Exports the result in a JSON file named:
    ('todo_all_employees.json.json')
and formatted as:
{ "USER_ID":
    [
      {"username": "USERNAME", "task": "TITLE", "completed": COMPLETED_STATUS},
      {"username": "USERNAME", "task": "TITLE", "completed": COMPLETED_STATUS},
      ...
    ],
  "USER_ID":
    [
      {"username": "USERNAME", "task": "TITLE", "completed": COMPLETED_STATUS},
      {"username": "USERNAME", "task": "TITLE", "completed": COMPLETED_STATUS},
       ...
    ]
}

[PS: This is the 'Pretty view', actual output will be on a single line]
"""
import json
import requests
import sys


if len(sys.argv) != 1:
    print("Script takes NO ARGUMENT")
else:
    todo_resource = "https://jsonplaceholder.typicode.com/todos/"
    todo_response = requests.get(todo_resource).json()

    users_resource = 'https://jsonplaceholder.typicode.com/users/'
    users_response = requests.get(users_resource).json()

    filename = "todo_all_employees.json"
    with open(filename, 'w') as jsonfile:
        users = {}
        user_data = []

        for user in users_response:
            for task in todo_response:
                if user.get('id') == task.get('userId'):
                    user_data.append({"username": user.get('username'),
                                      "task": task.get('title'),
                                      "completed": task.get('completed')})
            users[user.get('id')] = user_data

        json.dump(users, jsonfile)
