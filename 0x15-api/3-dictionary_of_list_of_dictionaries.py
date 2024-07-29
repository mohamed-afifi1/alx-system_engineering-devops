#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import json
import requests

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get("{}/users".format(url,)).json()

    with open("todo_all_employees.json", "w") as json_file:
        for employee in users:
            todos = requests.get("{}/todos?userId={}".format(
                                 url, employee.get("id"))).json()
            json.dump({employee.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": employee.get("username")
            } for t in todos]}, json_file)
