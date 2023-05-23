#!/usr/bin/python3
"""Using a REST API to get todo list of a user based on id"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    u = requests.get('https://jsonplaceholder.typicode.com/users')
    todo_list = []
    completed = 0
    completed_list = []
    name = ''
    for i in range(0, len(r.json())):
        if r.json()[i]['userId'] == int(argv[1]):
            todo_list.append(r.json()[i])
    for i in range(0, len(todo_list)):
        if todo_list[i]['completed']:
            completed_list.append(todo_list[i]['title'])
            completed += 1
    for i in range(0, len(u.json())):
        if u.json()[i]['id'] == int(argv[1]):
            name = u.json()[i]['name']
            break
    print('Employee {} is done with tasks ({:d}/{:d}):'.format(name, completed, len(todo_list)))
    for i in range(0, len(completed_list)):
        print('\t {}'.format(completed_list[i]))
