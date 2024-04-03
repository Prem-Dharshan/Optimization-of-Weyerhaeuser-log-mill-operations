# Optimization of Weyerhaeuser's Log Mill Operations

## Introduction
This repository contains the code and documentation for optimizing Weyerhaeuser's log mill operations. The goal is to enhance efficiency, reduce waste, and improve overall productivity. Below are the instructions for setting up the project environment using a virtual environment (venv) and installing the necessary dependencies.

## Prerequisites
Before proceeding, ensure you have the following installed on your system:
- **Python 3.12+**: Make sure you have Python installed. If not, download and install it from the [official Python website](https://www.python.org/downloads/).
- **Git**: Install Git if you haven't already. You can find installation instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Setting Up the Virtual Environment
1. **Clone the Repository**:
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to store the project.
   - Run the following command to clone the repository:
     ```
     git clone https://github.com/Prem-Dharshan/Optimization-of-Weyerhaeuser-log-mill-operations.git
     ```

2. **Create a Virtual Environment**:
   - Change into the project directory:
     ```
     cd weyerhaeuser-optimization
     ```
   - Create a virtual environment named `.venv` (you can choose a different name if you prefer):
     ```
     python -m venv .venv
     ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```
     .venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source .venv/bin/activate
     ```
    - If you are using GIT Bash:
      ```
      source .venv\Scripts\activate
      ```

## Installing Dependencies
1. **Install Required Packages**:
   - While the virtual environment is active, install the project dependencies listed in `requirements.txt`:
   
     ```
     pip install -r requirements.txt
     ```

## Usage
Now that your environment is set up, you can run the optimization scripts and analyze the results by running the `main.py` for the given dataset in the [Case Study](About/Case_Study_Operations_Research_by_Hamdy_A_Taha.pdf)

```bash
  python src/main.py
```
or 

```bash
  python3 src/main.py
```

## main.py
1. **Overview**:
The main.py file contains the primary logic for calculating revenue and optimal crosscut combinations in Weyerhaeuser's log mill operations. It interacts with input data, processes it using dynamic programming, and outputs revenue and crosscutting calculations.

2. **Functions**:
**calculateRevenue(data1, M: int, I: int, N: int, cost: float)**

- Description: Calculates revenue and optimal crosscut combinations.
- Parameters:
    data1: Dictionary containing revenue data for each mill.
    M: Number of mills.
    I: Length of logs.
    N: Maximum number of crosscut combinations.
    cost: Cost of crosscutting.
- Returns: None

Steps:
Initializes tables for storing calculations for each mill.
Iterates through possible crosscut combinations, calculating revenue.
Updates maximum revenue and associated crosscut combinations.
Prints revenue and crosscutting calculations.

**read_excel_data(filename)**
- Description: Reads input data from an Excel file.
- Parameters:
   filename: Name of the Excel file containing revenue data.
- Returns: Dictionary containing revenue data for each mill.

Steps:
Reads data from the specified Excel file.
Parses data into a dictionary format.

**main()**
- Description: Main function for executing revenue calculation.
- Parameters: None
- Returns: None

3. **Usage:**
- Input Data Preparation:
    Prepare an Excel file containing revenue data for each mill.
- Execution:
    Run the main.py file.
       Enter the filename of the Excel file when prompted.
       Provide the required input values (number of mills, length of logs, maximum crosscut combinations, cost of crosscutting).
- Output:
    The program will display revenue and crosscutting calculations for each mill.
- Example Usage:
python main.py

4. **Dependencies**:
    pandas: For reading data from Excel files.
    prettytable: For displaying tabular data in a visually appealing format.
    prettytable.colortable: For adding color themes to tables.

## generate_revenue_data.py
1. **Overview**:
The generate_revenue_data.py script generates simulated revenue data for testing purposes. It creates a matrix representing revenue values for different crosscut combinations of logs based on specified parameters.

2. **Functions**:
**generate_revenue_data(I, N)**
- Description: Generates simulated revenue data matrix.
- Parameters:
   I: Length of logs.
   N: Maximum number of crosscut combinations.
- Returns: List of lists representing revenue data matrix.

3. **Usage:**
- Script Execution:
Run the script generate_revenue_data.py.
Enter the values of I (length of logs) and N (maximum number of crosscut combinations) when prompted.
- Output:
The script will display the simulated revenue data matrix.
- Example Usage:
python generate_revenue_data.py

4. **Dependencies**:
random: For generating random revenue values.
pprint: For pretty-printing the generated revenue data.
typing: For type hints.
PrettyTable: For displaying tabular data.
ColorTable and Themes from prettytable.colortable: For adding color themes to tables.


## Contributing
If you'd like to contribute to this project, feel free to submit pull requests or open issues. We welcome your ideas and improvements! 

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
