#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    employee = requests.get("{}/users/{}".format(url, id)).json()
    todos = requests.get("{}/todos?userId={}".format(url, id)).json()

    with open("{}.csv".format(id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                id,
                employee.get("username"),
                task.get('completed'),
                task.get('title'),
            ])
