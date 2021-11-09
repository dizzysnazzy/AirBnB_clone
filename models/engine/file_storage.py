#!/usr/bin/python3
"""
Contains the FileStorage class
"""
import json

class FileStorage:
    """serializes instances to JSON and desirializes JSON to instancess"""

    # string - path to store JSON file
    __file_path = "file.json"
    # dictionary - store all objects by <class name>.id
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to JSON file"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file)

    def reload(self):
        """deserializes JSON file to __objects if __file_path exists"""
        try:
            with open(self.__file_path, 'r') as file:
                json_o = json.load(file)
            for key in json_o:
                self.__objects[key] = classes[json_o[key]["__class__"]](**json_o[key])
        except:
            pass
