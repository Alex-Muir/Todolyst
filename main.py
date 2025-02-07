import argparse

import helpers as h

# A simple command line to-do list using argparse

def main():    
    filename = 'todo_list.txt'
    todo_list = h.load(filename)

    # set up parser and arguments
    parser = argparse.ArgumentParser()
    h.set_up_parser(parser)
    args = parser.parse_args()

    # add a new item to the list
    if args.add:
        item = {
            'description': args.add,
            'status': 'Incomplete'
            }
        todo_list.append(item)
        h.save(filename, todo_list)

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
        h.save(filename, todo_list, message)

    # mark an item complete
    if args.toggle:
        if todo_list:
            h.print_list(todo_list)
            while True:
                prompt = "Which item's status would you like to toggle?"
                prompt += " Enter a number or 'c' to cancel: "
                selection = h.get_selection(prompt)
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
                            h.toggle_status(selection-1, todo_list)
                            message = "item's status has been toggled"
                            h.save(filename, todo_list, message)
                            break
        else: 
            print("The list is empty")
        
    # remove an item
    if args.remove:
        if todo_list:
            h.print_list(todo_list)
            while True:
                prompt = "Which item would you like to remove?"
                prompt += " Enter a number or 'c' to cancel: "
                selection = h.get_selection(prompt)
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
                            message = "Item has been removed"
                            h.save(filename, todo_list, message)
                            break
        else:
            print("The list is empty")
    
    # move completed items to the bottom of the list
    if args.move_to_bottom:
        if todo_list:
            h.completed_to_bottom(todo_list)
            h.save(filename, todo_list)
        else:
            print("The list is empty")

    # clear completed items from the list
    if args.clear_complete:
        if todo_list:
            todo_list = [item for item in todo_list if item['status'] == 'Incomplete']
            h.save(filename, todo_list)
        else:
            print("The list is empty")


if __name__ == "__main__":
    main()
