#!/usr/bin/python3
"""student to JSON"""


class Student:
    """class Student
    """
    def __init__(self, first_name, last_name, age):
        """Instantiation of attributes for student
        Arguments:
            first_name {str} -- first name of student
            last_name {str} -- second name of student
            age {int} -- age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """prints certain keys and values
        Keyword Arguments:
            attrs {str} -- specified attribute (default: {None})
        Returns:
            dict -- a new dictioary with wanted keys and values
        """
        if attrs is None:
            return self.__dict__
        dic = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dic[key] = value
        return dic

    def reload_from_json(self, json):
        """reloads values of instance
        Arguments:
            json {dict} -- dictionary with students info
        """
        for key, value in json.items():
            setattr(self, key, value)
