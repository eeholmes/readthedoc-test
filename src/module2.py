"""
Module1 - the first module
"""

__version__ = "0.1.0"

class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass

def first_function(kind=None):
    """
    Return a list of random ingredients as strings.
    
    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]

def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.
    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]

def another_function(kind=None, arg2=None):
    """
    Return a list of random ingredients as strings.
    
    :param kind: Optional "kind" of ingredients.
    :param arg2: Optional.
    :type kind: list[str] or None
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]
