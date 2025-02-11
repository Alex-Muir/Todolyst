# To-Do Lyst
## A simple command line to-do list written in python
With To-Do Lyst you can create a simple list to stay organized and create clear, 
daily goals. You can add items to your list, remove them, toggle an item's 
completion status, change completed items' position on the list, remove completed
items, print the list, and clear the list
### Requirements
Python 3.6+
### Instructions
1. Clone the repository or download the zip (and extract it)
2. Navigate into the To-Do Lyst folder
### Usage
To get argument and option list:  
python3 main.py -h  
![Screenshot of help output](images/help.png)  

To add an item to the list:  
python3 main.py -a "Your item"  
![Screenshot of new Items added to the list](images/add.png)  

To print the list:  
python3 main.py -p  
![Screenshot of print option and output](images/print.png)  

To remove an item from the list:  
python3 main.py -r  
![Screenshot of remove option and output](images/remove.png)  

To toggle the completion status of an item:  
python3 main.py -t  
![Screenshot of the toggle option and output](images/toggle.png)  

To move the completed items to the bottom of the list:  
python3 main.py -m  
![Screenshot of the move-completed-to-bottom option and output](images/move_completed_to_bottom.png)  

To clear completed items:  
python3 main.py -C  
![Screenshot of the clear-completed option and output](images/clear_completed.png)  

To clear the list:  
python3 main.py -c  
![Screenshot of the clear-list option and output](images/clear_list.png)  

You can also run multiple options at the same time  

To add items to you list and print  
python3 main.py -a "Item 1" "Item 2" "Item 3" "Item 4" "Item 5" -p  
![Screenshot of add and print option together and output](images/add_and_print.png)  

To clear completed items and print:  
python3 main.py -C -p  
![Screenshot of clear-completed and print options and output](images/move_clear_print.png)  
