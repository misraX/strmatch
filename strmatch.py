class Finder(object):
    def __init__(self, string_list):
        """
        Example:
        >>> string_list = ['hello', 'world']
        >>> finder_cls = Finder(string_list)

        :param string_list: list of strings
        """
        self.string_list = string_list

    def find(self, value):
        """
        Finds string in a list of strings.

        The find method main functionality is evaluating the intersection of two sets.

        The process:

        1. Iterating over the string_list
        2. Check if there is an intersection between the matcher and the value,
           the intersection length must be equal to the length of the value's set.
        3. While True add it to the list.

        Complexity of set intersection = O(min(len(s), len(t))

        :param value: str
        :return: list
        """
        return [matcher for matcher in self.string_list if
                set.intersection(set(matcher), set(value)).__len__() == set(value).__len__()]
