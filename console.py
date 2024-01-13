#!/usr/bin/python3
"""This is the console module"""

import cmd
import sys
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("")  # Print a newline before exiting
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            if class_name == 'User':
                new_instance = User()
            else:
                new_instance = eval(arg)()

            new_instance.save()
            print(new_instance.id)
        except TypeError as e:
            print("** {}".format(str(e)))
        except Exception as e:
            print("** An unexpected error occurred: {}".format(str(e)))


    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        obj_list = []

        if not args:
            for obj_id, obj in storage.all().items():
                obj_list.append(str(obj))
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return
            obj_list = [str(obj) for obj_id,obj  in storage.all().items() if class_name in obj_id]

        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        obj = storage.all()[key]
        if hasattr(obj, attribute_name):
            try:
                # Attempt to cast attribute_value to the type of the attribute
                attribute_value = type(getattr(obj, attribute_name))(attribute_value)
                setattr(obj, attribute_name, attribute_value)
                obj.save()
            except Exception as e:
                print("** {}".format(str(e)))
        else:
            print("** attribute doesn't exist **")
        

if __name__ == '__main__':
    if sys.stdin.isatty():
        HBNBCommand().cmdloop()
    else:
        for line in sys.stdin:
            HBNBCommand().onecmd(line.strip())

