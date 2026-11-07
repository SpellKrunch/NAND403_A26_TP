import os 
import sys 

# find the local folder where the files are located
absolute_file_path = os.path.abspath(__file__)
absolute_folder_path = os.path.dirname(absolute_file_path)
print(absolute_folder_path)

# gives this folder to the python path for importing 
sys.path.append(absolute_folder_path)

import importlib
import UI
importlib.reload(UI)
import Functions
importlib.reload(Functions)


def main():
    global tool_window
    try:
        tool_window.close()
    except Exception:
        pass
    tool_window = UI.RandomAnimator()
    tool_window.show()
    UI.other()
main()




