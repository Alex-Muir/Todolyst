import argparse

import helpers as h

# A simple command line to-do list using argparse

FILENAME = 'todo_list.txt'

def main():    
    todo_list = h.load(FILENAME)

    # set up parser and arguments
    parser = argparse.ArgumentParser(description="A simple CLI todo list written in python")
    h.set_up_parser(parser)
    args = parser.parse_args()

    # add a new item to the list
    if args.add:
        for desc in args.add:
            desc = desc.strip()
            item = {
                'description': desc,
                'status': 'Incomplete'
                }
            todo_list.append(item)
        h.save(FILENAME, todo_list, h.get_message('a'))

    # clear the list
    if args.clear:
        todo_list.clear()
        h.save(FILENAME, todo_list, h.get_message('c'))

    # mark an item complete
    if args.toggle:
        if todo_list:
            h.print_list(todo_list)
            index = h.get_valid_selection(h.get_prompt('t'), len(todo_list))
            if index is not None:
                h.toggle_status(index, todo_list)
                h.save(FILENAME, todo_list, h.get_message('t'))        
        else: 
            print("The list is empty")
        
    # remove an item
    if args.remove:
        if todo_list:
            h.print_list(todo_list)
            index = h.get_valid_selection(h.get_prompt('r'), len(todo_list))
            if index is not None:
                todo_list.pop(index)
                h.save(FILENAME, todo_list, h.get_message('r'))
        else:
            print("The list is empty")
    
    # move completed items to the bottom of the list
    if args.move_to_bottom:
        if todo_list:
            h.completed_to_bottom(todo_list)
            h.save(FILENAME, todo_list, h.get_message('m'))
        else:
            print("The list is empty")

    # clear completed items from the list
    if args.clear_complete:
        if todo_list:
            todo_list[:] = [item for item in todo_list if item['status'] == 'Incomplete']
            h.save(FILENAME, todo_list, h.get_message('C'))
        else:
            print("The list is empty")

    # print the list
    if args.print:
        if todo_list:
            h.print_list(todo_list)
        else:
            print("The list is empty")


if __name__ == "__main__":
    main()
