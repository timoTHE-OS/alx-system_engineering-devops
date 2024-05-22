#!/usr/bin/python3
"""REST API for employees todos"""
import csv
import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + employeeId
    url_t = "https://jsonplaceholder.typicode.com/todos?userId="
    url_todo = url_t + employeeId

    response = requests.get(url=url)
    response_t = requests.get(url=url_todo)

    t_response = response_t.json()
    b_response = response.json()
    username = b_response["username"]

    with open('{}.csv'.format(employeeId), 'w') as file:
        for item in t_response:
            file.write('"{}","{}","{}","{}"\n'.format(item["userId"], username, item["completed"], item["title"]))
