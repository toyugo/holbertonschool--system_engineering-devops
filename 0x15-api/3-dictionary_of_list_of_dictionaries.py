#!/usr/bin/python3
""" Gather API Information """
import csv
import json
import requests
import sys
import urllib


def get_deserialised_json(inputurl):
    """
        inputurl: url which return a json formated string
        return: the deserialised Json
    """
    response = requests.get(inputurl).content.decode('UTF-8')
    # or return (requests.get(input).content.decode('UTF-8').json())
    try:
        obj = json.loads(response)
    except valueError:
        return ('input is not a json')
    return (obj)

if __name__ == '__main__':
    """
        Script which get data from a jsonplaceholder api
        and create a JSON file.
    """
    url = 'https://jsonplaceholder.typicode.com'
    url_user = '{}/users/'.format(url)
    data_user = get_deserialised_json(url_user)
    obj = {}
    for user in data_user:
        data_todo = "{}/users/{}/todos"\
              .format(url, user['id'])
        request = get_deserialised_json(data_todo)
        list_tasks = []
        for content in request:
            obj_task = {}
            obj_task['task'] = content['title']
            obj_task['completed'] = content['completed']
            obj_task['username'] = user['username']
            list_tasks.append(obj_task)
        obj[user['id']] = list_tasks
    with open('todo_all_employees.json', 'w') as f:
        json.dump(obj, f)
