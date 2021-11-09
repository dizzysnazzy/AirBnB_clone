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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
