import argparse
import json

# helper functions for todo list


# BASIC HELPERS
def get_valid_selection(prompt, length):
    """Get a valid selection from the user"""
    while True:
        selection = input(prompt)
        if selection.lower() == 'c':
            return None
        try:
            selection = int(selection)
        except ValueError:
            print("Invalid input. Enter a valid position number")
        else:
            if selection < 1 or selection > length:
                print("Invalid input. Enter a valid position number")
            else:
                return selection - 1


def get_prompt(argument):
    """Return the proper prompt based on the argument"""
    # toggle
    if argument == 't':
        prompt = "Which item's status would you like to toggle?"
    
    # remove
    if argument == 'r':
        prompt = "Which item would you like to remove?"

    prompt += " Enter a number or 'c' to cancel: "
    return prompt


def get_message(argument):
    """Return the proper message based on the argument"""
    # add item
    if argument == 'a':
        message = "Item has been added"
    # clear list
    elif argument == 'c':
        message = "The list has been cleared"
    # clear completed
    elif argument == 'C':
        message = "Completed items have been cleared"
    # move completed to bottom
    elif argument == 'm':
        message = "Completed items have been moved to the bottom"
    # remove item
    elif argument == 'r':
        message = "Item has been removed"
    # toggle item's status
    elif argument == 't':
        message = "Item's status had been toggled"
    return message


def print_list(todo_list):
    """Print the todo list"""                                                      
    for i in range(len(todo_list)):                                                      
        print(f"{i+1}. {todo_list[i]['description']}\t\t{todo_list[i]['status']}")

# FILE HELPERS
def save(filename, todo_list, message='your list has been saved'):
    """Write the todo list to a file"""               
    try:                                                                        
        with open(filename, 'w') as f:                                          
            json.dump(todo_list, f)                                             
    except FileNotFoundError:                                                   
        print("There seems to be an error with 'todo_list.txt'")                
    else:                                                                       
        print(message) 


def load(filename):
    """
    Read the todo list from a file, if the file exists. If it doesn't exist
    assume the program has not been run, initialize the todo list, and write
    it to a file
    """                                                           
    try:                                                                        
        with open(filename, encoding='utf-8') as f:                             
            todo_list = json.load(f)                                            
    except FileNotFoundError:                                                   
        todo_list = []                                                          
        save(filename, todo_list, '')                                            
    return todo_list  


# TODO_LIST HELPERS
def toggle_status(index, todo_list):
    """Toggle the completion status of an item in the list"""
    if todo_list[index]['status'] == 'Incomplete':
        todo_list[index]['status'] = 'Complete'
    else:
        todo_list[index]['status'] = 'Incomplete'


def completed_to_bottom(todo_list):
    """Move the completed items to the bottom of the list"""
    incomplete = [item for item in todo_list if item['status'].lower() == 'incomplete']
    complete = [item for item in todo_list if item['status'].lower() == 'complete']
    todo_list[:] = incomplete + complete
    

# PARSER HELPERS
def set_up_parser(parser):
    """Add arguments to the parser"""
    parser.add_argument("-a", "--add", help="add an item to your to-do list")
    parser.add_argument("-c", "--clear", help="clear your todo list", 
                        action="store_true")
    parser.add_argument("-C", "--clear_complete", 
                        help="remove completed items from the todo_list", 
                        action="store_true")
    parser.add_argument("-m", "--move_to_bottom", 
                        help="move completed items to the bottom of the list",
                        action="store_true")
    parser.add_argument("-p", "--print", help="print your todo list", 
                        action="store_true")
    parser.add_argument("-r", "--remove", help="remove an item from the todo list",
                        action="store_true")
    parser.add_argument("-t", "--toggle", help="toggle item status",
                        action="store_true")
    
    
    
