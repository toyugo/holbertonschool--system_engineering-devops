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
    user = requests.get("https://jsonplaceholder.typicode.com/users/2")
    try:
        obj = json.loads(response)
    except valueError:
        return ('url do not return a json')
    return (obj)

if __name__ == '__main__':
    employeeId = sys.argv[1]
    mainUrl = 'https://jsonplaceholder.typicode.com'
    urlEmployee = '{}/users/{}'.format(mainUrl, employeeId)
    urlTask = '{}/users/{}/todos'.format(mainUrl, employeeId)

    dataEmployee = getDeserialisedJson(urlEmployee)
    dataTask = getDeserialisedJson(urlTask)

    employeeName = dataEmployee.get('name')
    employeeTotalTask = dataTask
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
