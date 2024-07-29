#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
"""
import json
import requests


url = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    data = {}
    users_res = requests.get('{}/users'.format(url)).json()
    todos_res = requests.get('{}/todos'.format(url)).json()
    for user in users_res:
        user_name = user.get('username')
        id = user.get('id')
        todos = list(filter(lambda x: x.get('userId') == id, todos_res))
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        data['{}'.format(id)] = user_data
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file)
