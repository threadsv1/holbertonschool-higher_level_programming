#!/usr/bin/python3
"""
Locked Class Model
"""
class LockedClass:
    """
    with no class or object attribute, that prevents the user from dynamically creating new instance attributes, except if the new instance attribute is called
    """
    __slots__ = "first_name"
