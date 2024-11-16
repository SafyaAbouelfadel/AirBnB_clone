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
                arg_list.append(x)
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

    def create(self):
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
        print(eval(list_args[0])().id)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
