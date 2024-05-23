#!/usr/bin/python3
"""REST API for employees todos"""
import json
import requests
import sys


if __name__ == "__main__":
    employeeId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/" + employeeId
    url_td = "https://jsonplaceholder.typicode.com/todos?userId=" + employeeId

    response = requests.get(url=url)
    response_t = requests.get(url=url_td)

    t_response = response_t.json()
    b_response = response.json()

    dictionary = {employeeId: []}
    usern = b_response["username"]
    for item in t_response:
        comp = item["completed"]
        t_dict = {"task": item["title"], "completed": comp, "username": usern}
        dictionary[employeeId].append(t_dict)
    with open('{}.json'.format(employeeId), 'w') as file:
        json.dump(dictionary, file)
