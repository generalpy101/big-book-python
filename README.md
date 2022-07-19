# Big Book of small ***Python*** Projects

This repo is contains projects for a book named *"Big Book of Small Python Projects"* by **A.L Sweigart**.

Thanks for this book!!

[Book Link](https://inventwithpython.com/bigbookpython/)


## Project Structure

```
- main_directory
  - project1
    - venv
    - src
    - requirements.txt
  - project2
    - venv
    - src
    - requirements.txt
```

- Each project will have its own [Virtual Environment](https://realpython.com/python-virtual-environments-a-primer/) which will help us to keep each project's dependencies separated.
- Virtual environment folder is named venv.
- Project's source code will be in src directory.
- Main code will be in main.py file.
- Rest of the code will be in directories like utils (if any) and directories for assets like images will be named accordingly.
- Each project will contain requirements.txt file in its root directory for requirements.
- Folder name for project will be in format `p{number}-{name}`.


## Local setup 

First install python. Get [python](https://www.python.org/downloads/) .

Python [setup guide](https://realpython.com/installing-python/) .

Note that python must be *added to path* so that command line commands can be executed.

Version I am using is : **3.10**

Clone this repo.

After installing python and cloning this repo steps for setup are :

- Change directory to project main directory.

  ```bash
  # Assuming you are in repo home directory
  cd p{number}-{name}
  ```
- Create a virtual environment.
  
  ```bash
  # Syntax : python -m venv {virtual_env_name}
  python -m venv venv 
  ```
- Install required libraries.
  
  ```bash 
  pip install -r requirements.txt
  ```
- Change to project's source code directry (which is src here)
  
  ```bash
  # While in project directory
  cd src
  ```
- Run main.py file.

  ```bash
  # Supply command line arguments if any.
  # If there are any cmd arguments and you fail to supply them,
  # program will notify you. 
  python main.py
  ```