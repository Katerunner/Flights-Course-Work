import ctypes


# Implements the Array ADT using array capabilities of the ctypes module.

class Node:
    """Represents Node for linked structure"""

    def __init__(self, type, value):
        """Initialization"""
        assert type == "lat" or type == "lon", "Type must be 'lar' or 'lon'"
        self.type = type
        self.value = value

    def __str__(self):
        """String representation"""
        return str(self.value)


class Corray:
    """Represents linked array for coordinates"""

    def __init__(self, lat=0, lon=0):
        self._size = 2
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * 2
        self._elements = PyArrayType()
        # Initialize each element.
        self['lat'] = lat
        self['lon'] = lon

    # Returns the size of the array.
    def __len__(self):
        """Returns len of the corray (always = 2)"""
        return 2

    # Gets the contents of the index element.
    def __getitem__(self, index):
        """Gets the contents of the index element"""
        assert index == "lat" or index == "lon", "Array subscript out of range"
        if index == "lat":
            return self._elements[0].value
        else:
            return self._elements[1].value

    # Puts the value in the array element at index position.
    def __setitem__(self, index, value):
        """Puts the value in the array element at index position"""
        assert index == "lat" or index == "lon", "Array subscript out of range"
        if index == "lat":
            self._elements[0] = Node("lat", value)
        else:
            self._elements[1] = Node("lon", value)
