# Background Processes Exporter

A Python script to export details of all background processes running on your system to a CSV file. This tool allows you to sort processes based on various attributes, such as name, PID, user, or status.

## Features
- Exports all running background processes to a CSV file.
- User-selectable sorting options:
  - Alphabetical (Process Name)
  - By PID
  - By User
  - By Status
- Saves the output file to the Desktop for easy access.

## Requirements
- Python 3.6 or higher
- The `psutil` library for retrieving process details

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/background_processes_exporter.git
   cd background_processes_exporter

## Install dependencies:
   ```bash
    pip install psutil

# Usage

## Run the script
  ```bash
  python export_background_processes.py

## Follow the prompt to choose the sorting option:

Choose the sorting type for the processes:
1. Alphabetical (Name)
2. By PID
3. By User
4. By Status
Enter the number corresponding to your choice:

## Output

The script will generate a CSV file named background_processes.csv on your Desktop.

## Contributing

Feel free to open an issue or submit a pull request for any improvements or bug fixes.

##License

This project is licensed under the MIT License. See the LICENSE file for details.
