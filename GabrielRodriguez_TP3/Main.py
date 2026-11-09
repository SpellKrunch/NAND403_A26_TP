import os 
import sys 

# find the local folder where the files are located
absolute_file_path = os.path.abspath(__file__)
absolute_folder_path = os.path.dirname(absolute_file_path)
print(absolute_folder_path)

# gives this folder to the python path for importing 
sys.path.append(absolute_folder_path)

# importing the UI and Function script (reload is used help the script update any changes)
import importlib
import UI
importlib.reload(UI)
import Functions
importlib.reload(Functions)

# main function 
def main():

    # global variable
    global tool_window

    # close any existing window before opening a new one
    try:
        tool_window.close()
    except Exception:
        pass

    # create and show the window 
    tool_window = UI.RandomAnimator()
    tool_window.show()

main()




