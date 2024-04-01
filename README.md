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

## Contributing
If you'd like to contribute to this project, feel free to submit pull requests or open issues. We welcome your ideas and improvements! 

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
