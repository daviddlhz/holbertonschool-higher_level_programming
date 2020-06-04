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

    def to_json(self):
        """Convert the class student to dict
        Returns:
            dict -- dictionary of object student
        """
        return self.__dict__
