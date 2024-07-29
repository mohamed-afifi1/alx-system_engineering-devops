#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get("{}/users/{}".format(url, id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, id)).json()
    complete = []

    for task in todos:
        if task.get("completed") is True:
            complete.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        employee.get('name'), len(complete), len(todos)))

    for task in complete:
        print(f"     {task}")
