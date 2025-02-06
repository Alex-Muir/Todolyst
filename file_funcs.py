import json

# helper functions for working with files

def write_to_file(filename, todo_list, message='your list has been saved'):
    """Write the todo list to a file"""               
    try:                                                                        
        with open(filename, 'w') as f:                                          
            json.dump(todo_list, f)                                             
    except FileNotFoundError:                                                   
        print("There seems to be an error with 'todo_list.txt'")                
    else:                                                                       
        print(message) 


def read_from_file(filename):
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
        write_to_file(todo_list, '')                                            
    return todo_list  
