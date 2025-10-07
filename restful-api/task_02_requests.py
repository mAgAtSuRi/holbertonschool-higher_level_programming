#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")
    json_data = r.json()
    for dic in json_data:
        print(dic["title"])


def fetch_and_save_posts():
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {r.status_code}")
    json_data = r.json()
    list = []
    fieldnames = ["id", "title", "body"]
    for dic in json_data:
        list.append({k: dic[k] for k in fieldnames})
    with open("posts.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list)
