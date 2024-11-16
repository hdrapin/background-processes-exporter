

#!/usr/bin/env python

"""A Python script to export details of all background processes running on your system to a CSV file. This tool allows you to sort processes based on various attributes, such as name, PID, user, or status."""

__author__ = "HD Rapin"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "HD Rapint"
__email__ = "hdrapin @@ proton.me"
__status__ = "Production"


import psutil
import datetime
import os
import csv

def get_desktop_path():
    """
    Get the path to the Desktop directory for the current user.
    :return: Path to the Desktop directory.
    """
    return os.path.join(os.path.expanduser("~"), "Desktop")

def get_sorting_preference():
    """
    Ask the user for the sorting preference.
    :return: The sorting key and order.
    """
    print("Choose the sorting type for the processes:")
    print("1. Alphabetical (Name)")
    print("2. By PID")
    print("3. By User")
    print("4. By Status")
    choice = input("Enter the number corresponding to your choice: ").strip()
    
    if choice == "1":
        return "Name"
    elif choice == "2":
        return "PID"
    elif choice == "3":
        return "User"
    elif choice == "4":
        return "Status"
    else:
        print("Invalid choice, defaulting to alphabetical sorting.")
        return "Name"

def export_background_processes_to_csv():
    """
    Export the list of all background processes with additional details to a CSV file
    saved on the Desktop, sorted by user's choice.
    """
    desktop_path = get_desktop_path()
    file_name = os.path.join(desktop_path, "background_processes.csv")
    
    try:
        processes = []
        
        for process in psutil.process_iter(['pid', 'name', 'username', 'create_time', 'status', 'num_threads']):
            try:
                pid = process.info['pid']
                name = process.info['name'] or "Unknown"
                user = process.info['username'] or "Unknown"
                status = process.info['status'] or "Unknown"
                num_threads = process.info['num_threads'] or 0
                create_time = datetime.datetime.fromtimestamp(
                    process.info['create_time']
                ).strftime("%Y-%m-%d %H:%M:%S") if process.info['create_time'] else "Unknown"
                
                # Collect process details
                processes.append({
                    "Name": name,
                    "PID": pid,
                    "User": user,
                    "Started": create_time,
                    "Threads": num_threads,
                    "Status": status
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        
        # Ask for sorting preference
        sorting_key = get_sorting_preference()
        
        # Sort processes by user's choice
        processes.sort(key=lambda x: str(x[sorting_key]).lower() if sorting_key != "PID" else int(x[sorting_key]))
        
        # Write to CSV
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["Name", "PID", "User", "Started", "Threads", "Status"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write the header
            writer.writeheader()
            
            # Write process details
            for process in processes:
                writer.writerow(process)
        
        print(f"Background processes have been exported to '{file_name}' successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    export_background_processes_to_csv()
