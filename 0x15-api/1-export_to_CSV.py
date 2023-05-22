#!/usr/bin/python3
"""Using a REST API to get todo list of a user based on id
and export to csv file"""
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
    with open(argv[1] + ".csv", 'w') as f:
        for i in range(0, len(todo_list)):
            f.write('"{}","{}","{}","{}"\n'.format(argv[1], name, todo_list[i]['completed'], todo_list[i]['title']))
