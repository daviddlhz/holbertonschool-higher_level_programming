#!/usr/bin/python3
"""[Class Base]
"""


import json

class Base:
    """[Initialization variables]
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """[Method constructor]

        Args:
            id ([number]): [id of instances]. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """[method list of dictionaries to json]
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method save json
        """
        lists = []
        if len(list_objs) is not 0:
            for i in list_objs:
                lists.append(i.to_dictionary())
        dicts = cls.to_json_string(lists)

        with open(cls.__name__ + ".json", "w+") as my_file:
            my_file.write(dicts)

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is [None, ""]:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
            tmp.update(**dictionary)
            return tmp
        if cls.__name__ == "Square":
            tmp = cls(1)
            tmp.update(**dictionary)
            return tmp

    @classmethod
    def load_from_file(cls):
        """
        Method returns a list of instances
        """
        try:
            with open(cls.__name__ + ".json", "r") as my_file:
                read = my_file.read()
                lists = Base.from_json_string(read)
                create = []
                for i in lists:
                    create.append(cls.create(**i))
                return create
        except IOError:
            return []
