#!/usr/bin/python3
""" Gather API Information """
import json
import requests
import sys
import urllib


def getDeserialisedJson(url):
    """
        From an url which return serialised jsonFile request
        return the deserialised Json
    """
    response = requests.get(url).content.decode('UTF-8')
    # or return (requests.get(url).content.decode('UTF-8').json())
    try:
        obj = json.loads(response)
    except valueError:
        return ('url do not return a json')
    return (obj)

if __name__ == '__main__':
    """
        Script which get data from a jsonplaceholder api
        and print a formated string.
    """
    employeeId = sys.argv[1]
    Url = 'https://jsonplaceholder.typicode.com'
    urlEmployee = '{}/users/{}'.format(Url, employeeId)
    urlTask = '{}/users/{}/todos'.format(Url, employeeId)

    dataEmployee = getDeserialisedJson(urlEmployee)
    dataTask = getDeserialisedJson(urlTask)

    employeeName = dataEmployee.get('name')
    taskCounter = 0
    completeCounter = 0
    titleAll = ""

    for task in dataTask:
        taskCounter += 1
        if task.get('completed'):
            completeCounter += 1
            titleAll += '\t %s\n' % task.get('title')
    totalTask = taskCounter

    print("Employee %s is done with \
tasks(%s/%s):" % (employeeName, completeCounter, totalTask))
    print("%s" % titleAll, end='')
