#!/usr/bin/python3
"""Using a REST API to get todo list of a user based on id
and export to json file"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    u = requests.get('https://jsonplaceholder.typicode.com/users')
    todo_list = []
    name = ''
    for i in range(0, len(r.json())):
        if r.json()[i]['userId'] == int(argv[1]):
            todo_list.append(r.json()[i])
    for i in range(0, len(u.json())):
        if u.json()[i]['id'] == int(argv[1]):
            name = u.json()[i]['username']
            break
    new_list = []
    for i in range(0, len(todo_list)):
        todo_dict = {}
        todo_dict['task'] = todo_list[i]['title']
        todo_dict['completed'] = todo_list[i]['completed']
        todo_dict['username'] = name
        new_list.append(todo_dict)
    user_dict = {argv[1]: new_list}
    with open(argv[1] + '.json', 'w') as f:
        json.dump(user_dict, f)
