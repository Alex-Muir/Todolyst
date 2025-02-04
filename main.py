import argparse

from to_do_lyst import TodoList

# A simple command line to-do list using argparse


my_todo_list = TodoList()
my_todo_list.add_item("Make a bunch of money")
my_todo_list.print_list()


