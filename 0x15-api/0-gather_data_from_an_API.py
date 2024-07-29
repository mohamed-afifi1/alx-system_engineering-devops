#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get(f"{url}/users/{id}").json()
    todos = requests.get(f"{url}/todos?userId={id}").json()
    complete = []

    for task in todos:
        if task.get("completed") is True:
            complete.append(task.get("title"))
    print(f"Employee {employee.get('name')} \
is done with tasks({len(complete)}/{len(todos)}):")
    for task in complete:
        print(f"     {task}")
