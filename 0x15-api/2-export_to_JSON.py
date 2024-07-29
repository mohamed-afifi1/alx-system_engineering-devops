#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get("{}/users/{}".format(url, id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, id)).json()
    with open("{}.json".format(id), "w") as json_file:
        user = []
        tasks = {}
        for task in todos:
            tasks["task"] = task.get("title")
            tasks["completed"] = task.get('completed')
            tasks["username"] = employee.get('username')
            user.append(tasks)
        json.dump({id: user}, json_file)
