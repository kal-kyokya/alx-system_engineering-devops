#!/usr/bin/python3
"""
'1-export_to_CSV' is a script that:
* Takes in a cmd line argument,
* Utilizes it as 'USER_ID'
* Retrieves associated informations from a web resource
* Generates a Custom View

* Exports the result in a JSON file ('USER_ID.json') formatted as:
[PS: This is the 'Pretty view', output will be on a single line]
{ "USER_ID":
  [
      {"task": "TITLE", "completed": COMPLETED_STATUS, "username": "USERNAME"},
      {"task": "TITLE", "completed": COMPLETED_STATUS, "username": "USERNAME"},
      ...
  ]
}
"""
import json
import requests
import sys


if len(sys.argv) != 2:
    print("Usage: ./2-export_to_JSON <user_id>")
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
    name = response.get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        name, len(tasks_done), len(user_tasks)))
    for task in tasks_done:
        print("\t {}".format(
            task.get('title')))

    filename = user_id + ".json"
    with open(filename, 'w') as jsonfile:
        my_list = []
        for task in user_tasks:
            my_list.append({"task": task.get('title'),
                            "completed": task.get('completed'),
                            "username": response.get('username')})
        json.dump({user_id: my_list}, jsonfile)
