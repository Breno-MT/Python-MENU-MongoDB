# Python MongoDB Menu (wip)

# Setup
- Must have Python 3.9 above.
- Must have MongoDB Atlas Cloud running.

# Usage
- Use Python Venv or any other Env that you already use with Python.
- To install it dependencies to work just.
```
To create Python env:
python -m venv venv
```

- Run the venv
```
source venv/bin/activate for Linux
venv/Scripts/activate.bat for Windows
```
- Then run the following command:
```
python -m pip install -r requirements.txt
```
- Run the following commands:
```
python pymongo_index.py
python app.py
```
### Running the first command does the following:
#### It creates a index on MongoDB to reduces the files it has to look for when used certain types of query!
#### Which in this case is "name" and "code"

# About
- It's a project based on my previous one. <a href="https://github.com/Breno-MT/Python-MongoDB">Click Here</a> to learn more about it.
- Note: README is in Portuguese-Brazilian!!!
- The reason that I made this project was, I didn't feel comfortable enough to use only the terminal to make CRUD with MongoDB so, I created a script for that lol

<img height=383 width=803 src="pymongo_image.png">
