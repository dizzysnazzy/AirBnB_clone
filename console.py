#!/usr/bin/python3
""" the console """

import cmd

class HBNBCommand(cmd.Cmd):
    """the hbnb console"""
    prompt = '(hbnb)'

    def emptyline(self):
        """implements an empty line and ENTER"""
        return False

    def do_quit(self, arg):
        """"implementation of quit command"""
        return True
    
    def do_EOF(self, arg):
        """implemenatation of EOF to exit"""
        return True

    def do_create(self, arg):
        """creates new instance of BaseModel"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name is missing **")
            return False
        if args[0] in classes:
            instance = classes[args[0]]()
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """prints string representation of an instance based on class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name is missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """deletes an instance based on class name and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name is missng **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key models.storage.all():
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """prints string representation of all instances based or not on the class name"""
        args = shlex.split(arg)
        list_obj = []
        if len(args) == 0:
            for value in models.storage.all().values():
                list_obj.append(str(value))
            print("[", end="")
            print(", ".join(list_obj), end="")
            print("]")
        elif args[0] in classes:
            for key in models.storage.all():
                if args[0] in key:
                    list_obj.append(str(models.storage.all()[key]))
            print("[", end="")
            print(", ".join(list_obj), end="")
            print("]")
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """updates an instance based on class name and id by updating attribute"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** clsaa name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(models.storage.all()[key], args[2], args[3])
                            models.storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
