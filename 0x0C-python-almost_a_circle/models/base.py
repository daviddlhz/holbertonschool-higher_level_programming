#!/usr/bin/python3
'''Base module'''


import json


class Base:
    '''class Base'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''initialization contructor with attributes'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''return of dictionary to JSON string'''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes Json string representation of list_objs to a file'''
        file_name = "{}.json".format(cls.__name__)
        new_list = []
        if list_objs is not None:
            for obj in list_objs:
                new_list.append(cls.to_dictionary(obj))
        with open(file_name, mode='w', encoding='utf-8')as f:
            f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        '''return list of Json string representation'''
        if json_string is None or len(json_string) < 1:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''return instance with all attributes'''
        if cls.__name__ == "Rectangle":
            temp = cls(1, 1)
        if cls.__name__ == "Square":
            temp = cls(1)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        '''return list of instances'''
        new = []
        file_name = "{}.json".format(cls.__name__)
        try:
            with open(file_name, 'r') as f:
                new = cls.from_json_string(f.read())
            for i, j in enumerate(new):
                new[i] = cls.create(**new[i])
        except:
            pass
        return new
