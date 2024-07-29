#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests

if __name__ == '__main__':
    with open("todo_all_employees.json", "w") as json_file:
        for userid in range(1, 11):
            url = "https://jsonplaceholder.typicode.com/"
            employee = requests.get("{}/users/{}".format(url, userid)).json()
            todos = requests.get("{}/todos?userId={}".format(url, userid))\
                .json()
            json.dump({userid: [{
                    "task": t.get("title"),
                    "completed": t.get("completed"),
                    "username": employee.get("username")
                } for t in todos]}, json_file)
