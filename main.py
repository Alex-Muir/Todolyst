import argparse

import file_funcs as ff
import helpers as h

# A simple command line to-do list using argparse
    
filename = 'todo_list.txt'
todo_list = ff.read_from_file(filename)

# set up parser and arguments
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--add", help="add an item to your to-do list")
parser.add_argument("-p", "--print", help="print your todo list", 
                    action="store_true")
parser.add_argument("-c", "--clear", help="clear your todo list", 
                    action="store_true")
parser.add_argument("-m", "--complete", help="mark an item complete",
                    action="store_true")
parser.add_argument("-r", "--remove", help="remove an item from the todo list",
                    action="store_true")
parser.add_argument("-b", "--move_to_bottom", 
                    help="move completed items to the bottom of the list",
                    action="store_true")
args = parser.parse_args()

# add a new item to the list
if args.add:
    item = {
        'position': len(todo_list) + 1,
        'description': args.add,
        'status': 'Incomplete'
        }
    todo_list.append(item)
    ff.write_to_file(filename, todo_list)

# print the list
if args.print:
    if(todo_list):
        h.print_list(todo_list)
    else:
        print("The list is empty")

# clear the list
if args.clear:
    todo_list.clear()
    message = 'your list has been cleared'
    ff.write_to_file(filename, todo_list, message)

# mark an item complete
if args.complete:
    if todo_list:
        h.print_list(todo_list)
        while True:
            selection = h.get_selection()

            if selection.lower() == 'c':
                break
            else:
                try:
                    selection = int(selection)
                except ValueError:
                    print("Invalid input. Enter a valid position number")
                else:
                    if selection < 1 or selection > len(todo_list):
                        print("Invalid input. Enter a valid postion number")
                    else:
                        index = selection - 1
                        todo_list[index]['status'] = 'Complete'
                        message = "item has been marked as 'complete'"
                        ff.write_to_file(filename, todo_list, message)
                        break
    else: 
        print("The list is empty")
        
        
# remove an item
if args.remove:
    if todo_list:
        h.print_list(todo_list)
        while True:
            selection = h.get_selection()
            if selection.lower() == 'c':
                break
            else:
                try:
                    selection = int(selection)
                except ValueError:
                    print("Invalid input. Enter a valid position number")
                else:
                    if selection < 1 or selection > len(todo_list):
                        print("Invalid input. Enter a valid position number")
                    else:
                        index = selection - 1
                        todo_list.pop(index)
                        h.reorder(index, todo_list)
                        message = "Item has been removed"
                        ff.write_to_file(filename, todo_list, message)
                        break
    
if args.move_to_bottom:
    if todo_list:
        for i in range(len(todo_list)):
            if todo_list[i]['status'].lower() == 'complete':
                tmp = todo_list.pop(i)
                todo_list.append(tmp)
        ff.write_to_file(filename, todo_list)
    else:
        print("The list is empty")


