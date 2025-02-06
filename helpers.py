# helper functions for todo list

def get_selection():
    """Get the user's selection for marking an item complete or for removing an item"""
    selection = input("Which item would you like to mark as complete?"  
                      " Enter a number or 'c' to cancel: ")
    return selection


def reorder(index, todo_list):
    """reorder the items 'position' on the list after an item removal"""
    position = index + 1
    for i in range(index, len(todo_list)):
        todo_list[i]['position'] = position
        position += 1
        
def print_list(todo_list):
    """Print the todo list"""                                                      
    for item in todo_list:                                                      
        print(f"{item['position']}. {item['description']}\t\t{item['status']}")
