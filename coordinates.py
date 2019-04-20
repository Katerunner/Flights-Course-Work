import ctypes


# Implements the Array ADT using array capabilities of the ctypes module.

class Node:
    def __init__(self, type, value):
        assert type == "lat" or type == "lon", "Type must be 'lar' or 'lon'"
        self.type = type
        self.value = value

    def __str__(self):
        return str(self.value)

class Corray:
    # Creates an array with size elements.
    def __init__(self, lat = None, lon = None):
        self._size = 2
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * 2
        self._elements = PyArrayType()
        # Initialize each element.
        self['lat'] = lat
        self['lon'] = lon

    # Returns the size of the array.
    def __len__(self):
        return 2

    # Gets the contents of the index element.
    def __getitem__(self, index):
        assert index == "lat" or index == "lon", "Array subscript out of range"
        if index == "lat":
            return self._elements[0].value
        else:
            return self._elements[1].value

    # Puts the value in the array element at index position.
    def __setitem__(self, index, value):
        assert index == "lat" or index == "lon", "Array subscript out of range"
        if index == "lat":
            self._elements[0] = Node("lat", value)
        else:
            self._elements[1] = Node("lon", value)

    # Clears the array by setting each element to the given value.
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value

    # Returns the array's iterator for traversing the elements.
    def __iter__(self):
        return _ArrayIterator(self._elements)


# An iterator for the Array ADT.
class _ArrayIterator:
    def __init__(self, the_array):
        self._array_ref = the_array
        self._cur_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_index < len(self._array_ref):
            entry = self._array_ref[self._cur_index]
            self._cur_index += 1
            return entry
        else:
            raise StopIteration