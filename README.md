# Project Description
This is the first step towards building a full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

#Files and Directories
- models directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.

- tests directory will contain all unit tests.

- console.py file is the entry point of our command interpreter.

- models/base_model.py file is the base class of all our models. It contains common elements:

- attributes: id, created_at and updated_at

- methods: save() and to_json()

- models/engine directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py**


#Description of the command interpreter
- Its exactly the same as the shell but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

  - Create a new object (ex: a new User or a new Place)
  - Retrieve an object from a file, a database etc
  - Do operations on objects (count, compute stats, etc)
  - Update attributes of an object
  - Destroy an object

# How to start it, How to use it
##Execution
Your shell should work like this in interactive mode:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all    create   help  show
BaseModel  EOF   Review  User   count  destroy  quit  update

(hbnb)
(hbnb)
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project(simple shell) in C)
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
Amenity    City  Place   State  all    create   help  show
BaseModel  EOF   Review  User   count  destroy  quit  update
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
#Usage
Start the console in interactive mode:
```bash
$ ./console.py
(hbnb)
```
Use help to see the available commands:
```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```
Quit the console:
```bash
(hbnb) quit
$
```
