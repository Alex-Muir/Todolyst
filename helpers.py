import argparse
import json

# helper functions for todo list


# BASIC HELPERS
def get_selection(prompt):
    """Get the user's selection for marking an item complete or for removing an item"""
    selection = input(prompt)
    return selection

        
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
    
    
    
