#!/usr/bin/python3
"""REST API for employees todos"""
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
    list_n = []

    for item in t_response:
        if item['completed']:
            list_n.append(item['title'])

    len_l = len(list_n) 
    n_l = len(t_response)
    print("Employee {} is done with tasks({}/{}):".format(b_response['name'], len_l, n_l))
    for l_item in list_n:
        print("\t{}".format(l_item))
