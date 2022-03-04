#!/usr/bin/python3
"""
Locked Class Model
"""


class LockedClass:
    """
    that prevents the user from dynamically creating new instance attributes
    """
    __slots__ = "first_name"
