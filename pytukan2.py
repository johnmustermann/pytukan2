"""
Tukan Main
"""

__version__ = "0.1.0"


class ReferenceError(Exception):
    """Raised if the kind is invalid."""
    pass


class RunAnalysisTest:
    """ 
    This is an example class to see how to use readthedocs
    
    Parameters
    ----------
    input1 : float
        Just a random input
    input2 : array
        Another random input
    """
    def __init__(self, input1, input2):
        self.attr1 = self.do_something(input1)
        self.attr2 = input2
    
    def do_something(self, input1):
        """ 
        An example function
        
        returns
        -------
        input3 : float
            input1 + 3
        """
        return input1 + 3
        
def get_random_settings():
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]
