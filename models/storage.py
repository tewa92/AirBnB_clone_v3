#!/usr/bin/python3
"""
This module defines the Storage class for managing the saving, retrieval,
and deletion of various objects within a storage system.

The Storage class provides methods to interact with stored objects,
including saving new objects, retrieving existing ones by various criteria,
and deleting objects.
"""


class Storage:
    """
    Storage class for managing the saving, retrieval, and deletion of objects.

    This class provides methods to interact with stored objects, including
    saving new objects, retrieving existing ones by various criteria, and
    deleting objects.

    Attributes:
        data (dict): A dictionary to store objects with their unique identifiers.
    """

    def __init__(self):
        """
        Initialize the Storage object with a dictionary of empty lists for
        various entities.

        The `objects` attribute is a dictionary that holds lists of different
        entities:
        - "amenities": A list to store amenities objects.
        - "cities": A list to store city objects.
        - "places": A list to store place objects.
        - "reviews": A list to store review objects.
        - "states": A list to store state objects.
        - "users": A list to store user objects.

        This structure is used to manage and organize various entities within
        the storage system.
        """
        self.objects = {
            "amenities": [],
            "cities": [],
            "places": [],
            "reviews": [],
            "states": [],
            "users": []
        }

    def count(self, cls=None):
        """
        Count the number of objects in storage matching the given class name.
        """
        if cls:
            return len(self.objects[cls])
        else:
            return sum(len(objs) for objs in self.objects.values())

    def close(self):
        """Close the storage connection if necessary."""
        pass


storage = Storage()
