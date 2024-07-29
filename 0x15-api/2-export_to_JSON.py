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
        json.dump({id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": employee.get("username")
            } for t in todos]}, json_file)
