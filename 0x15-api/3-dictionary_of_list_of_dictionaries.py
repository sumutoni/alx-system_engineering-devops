#!/usr/bin/python3
"""Using a REST API to get todo list of a user based on id
and export to json file"""
import json
import requests


if __name__ == "__main__":
    u = requests.get('https://jsonplaceholder.typicode.com/users')
    todo_list = []
    name = ''
    user_id = ''
    users_dict = {}
    for i in range(0, len(u.json())):
        name = u.json()[i]['username']
        user_id = u.json()[i]['id']
        todo_list = requests.get(
                    'https://jsonplaceholder.typicode.com/todos?userId='
                    + str(user_id)).json()
        new_list = []
        for i in range(0, len(todo_list)):
            todo_dict = {}
            todo_dict['username'] = name
            todo_dict['task'] = todo_list[i]['title']
            todo_dict['completed'] = todo_list[i]['completed']
            new_list.append(todo_dict)
        users_dict[str(user_id)] = new_list
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dict, f)
