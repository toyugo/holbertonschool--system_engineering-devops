#!/usr/bin/python3
""" Gather API Information """
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
        and print a formated string.
    """
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    url_employee = '{}/users/{}'.format(url, user_id)
    url_task = '{}/users/{}/todos'.format(url, user_id)

    data_employee = get_deserialised_json(url_employee)
    data_task = get_deserialised_json(url_task)

    employee_name = data_employee.get('name')
    task_counter = 0
    complete_counter = 0
    title_all = ""

    for task in data_task:
        task_counter += 1
        if task.get('completed'):
            complete_counter += 1
            title_all += "\t %s\n" % task.get('title')
    total_task = task_counter

    print("Employee %s is done with \
tasks(%s/%s):" % (employee_name, complete_counter, total_task))
    print("%s" % title_all, end='')
