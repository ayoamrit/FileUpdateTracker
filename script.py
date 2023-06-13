import os

def monitor_folder(folder_path):
    # Create a dictionary with file names as keys and None as values
    # for the initial state
    before = dict([(f, None) for f in os.listdir(folder_path)])
    
    # Loop
    while True:
        
        # Create a dictionary with file names as keys and None as values 
        # for the current state
        after = dict([(f, None) for f in os.listdir(folder_path)])
        
        #Find the files that were added since the last interaction
        added_files = [f for f in after if not f in before]
        
        if added_files:
            # Folder updated, perform actions here
            print("Folder updated")
            # Add your custom code here to handle the updates
        before = after

# Specify the folder path to monitor
folder_path = "D://ayoamrit"

# Call the monitor_folder function to start monitoring the folder
monitor_folder(folder_path)