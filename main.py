import argparse
import file_funcs as ff

# A simple command line to-do list using argparse
    
def print_list(todo_list):
    for item in todo_list:
        print(f"{item['position']}. {item['description']}\t{item['status']}")

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
        print_list(todo_list)
    else:
        print("The list is empty")

# clear the list
if args.clear:
    todo_list.clear()
    ff.write_to_file(filename, todo_list, 'your list has been cleared')

# mark an item complete
if args.complete:
    if todo_list:
        print_list(todo_list)
        while True:
            selection = input("Which item would you like to mark as complete?"
                              " Enter a number or 'c' to cancel: ")

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
                        selection -= 1
                        todo_list[selection]['status'] = 'Complete'
                        ff.write_to_file(filename, todo_list, "item has been markes as 'complete'")
                        break
    else: 
        print("The list is empty")
        
        
# remove an item
if args.remove:
    print("remove option set")
    
    


