#!/usr/bin/python3
"""
A command line interpreter for the AirBnB clone
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        HBNBC - a console class for the the airbnb clone
        program
    """
    prompt = "(hbnb) "
    
    __classes_list = {
        BaseModel.__name__: BaseModel,
        User.__name__: User,
        State.__name__: State,
        City.__name__: City,
        Place.__name__: Place,
        Amenity.__name__: Amenity,
        Review.__name__: Review
    }
    
    def parse(arg, id=" "):
        """
        Returns a list conatning the parsed arguments from the string
        """

        parg_list = arg.split(id)
        arg_list = []

        for k in parg_list:
            if k != '':
                arg_list.append(k)
        return arg_list

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
        
    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """Do nothins when receiving an empty line."""
        pass
    
    def do_create(self, arg):
        """
        Usage: create <class>

        Creates a new instance and print its id
        """
        arg_list = HBNBCommand.parse(arg)
        if (len(arg_list) == 0):
            print("** class name missing **")
            return False
            
        if arg_list[0] not in HBNBCommand.__classes_list:
            print("** class doesn't exist **")
            return False
        print(eval(arg_list[0])().id)
        storage.save()

    def do_show(self, arg):
        """
        Usage: show <class> <id> or <class>.show(<id>)
        
        Prints the string representation of 
        an instance based of an id
        """
        arg_list = HBNBCommand.parse(arg)
        objt = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        elif len(arg_list) == 1:
            print("** instance id missing **")
            return False
        elif arg_list[0] not in HBNBCommand.__classes_list:
            print("** class doesn't exist **")
            return False
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in objt:
            print("** no instance found **")
            return False
        print(objt["{}.{}".format(arg_list[0], arg_list[1])])
        
    def do_destroy(self, arg):
        """
        Usage: destroy <class> <id> or <class>.distroy(<id>)

        Deletes an instance based on the class name and id
        """
        arg_list = HBNBCommand.parse(arg)
        objt = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__classes_list:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in objt:
            print("** no instance found **")
            return False
        del objt["{}.{}".format(arg_list[0], arg_list[1])]
        storage.save()
        
    def do_all(self, arg):
        """
        Usage: all | all <class> | <class>.all()

        Prints all string representation of all instances
        based or not on the class name. 
        """
        arg_list = HBNBCommand.parse(arg)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__classes_list:
            print("** class doesn't exist **")
            return False
        list_objs = []
        if len(arg_list) == 0:
            print([obj.__str__() for o in storage.all().values()])
        elif len(arg_list) > 0:
            for o in storage.all().values():
                if arg_list[0] == o.__class__.__name__:
                    list_objs.append(o.__str__())
            print(list_objs)

    def do_update(self, arg):
        """
        Usage: update <class name> <id> <attribute name> "<attribute value>" or
        <class>.update(<id>, <attribute name>, "<attribute value>") or
        <class>.update(<id>, <dictionary>).

        Update the instance of a given id by adding
        or updating a given attribute.
        """
        # to-do

     def do_count(self, arg):
        """
        Usage: count <class> or <class>.count()

        Retrive the number of instances of a given class.
        """
        arg_list = HBNBCommand.parse(arg)
        count = 0
        for obj in storage.all().values():
            if arg_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

        def default(self, arg):
        """Handle commands that are not recognized.

        Args:
            arg (str): The unrecognized command.

        Returns:
            bool: False if the command is not recognized.
        """
        # to-do


if __name__ == '__main__':
    HBNBCommand().cmdloop()
