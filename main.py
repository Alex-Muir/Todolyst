import argparse
import json

# A simple command line to-do list using argparse

filename = 'todo_list.txt'

try:
    with open(filename, encoding='utf-8') as f:
        todo_list = json.load(f)
except FileNotFoundError:
    todo_list = []


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", help="add an item to your to-do list")
parser.add_argument("-p", "--print", help="print your todo list", action="store_true")
args = parser.parse_args()

if args.add:
    item = {
        'position': len(todo_list) + 1,
        'description': args.add,
        'status': 'Incomplete'
        }
    todo_list.append(item)

    try:
        with open(filename, 'w') as f:
            json.dump(todo_list, f)
    except FileNotFoundError:
        pass


if args.print:
    for item in todo_list:
        for k, v, in item.items():
            print(f"\n{k}: {v}")
    
    


