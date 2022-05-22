import json


class Tree:
    def __init__(self, frequency: int, left=None, right=None, character: str = None):
        self.left = left
        self.right = right
        self.character = character
        self.frequency = frequency

    def get_frequency(self) -> int:
        """
        Gets the frequency of the current tree

        :return: The frequency
        """
        return self.frequency

    def __str__(self) -> str:
        return f"Tree:{{" \
               f"{self.frequency}," \
               f"{self.character}," \
               f"{self.left}," \
               f"{self.right}" \
               f"}}"

    def __add__(self, other):
        """
        It creates a parent for the 2 trees.
        The frequency of the new tree is the addition of the frequencies of the trees

        :param other: the other tree
        :return: the parent tree of the 2 trees
        """
        freq = self.get_frequency() + other.get_frequency()
        new_tree = Tree(freq, self, other, None)
        return new_tree

    def to_json(self) -> str:
        """
        Transforms the current Tree into a JSON structure

        :return: a string representing te JSON object
        """
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def depth_first_traversal(self, result=None, constructor=""):
        """
        Goes through the tree  with the depth first algorithm
        :param result: a parameter for recursive purposes. There is no need to precise put a value here
        :param constructor: a parameter for recursive purposes. There is no need to precise put a value here
        :return:a 2 dimensions array with the couple [letter, bin code] inside.
        """
        if result is None:
            result = []
            
        if self.left is None and self.right is None:
            return [(self.character, constructor)]

        new_result = []
        if self.left is not None:
            c = constructor + '0'
            new_result += self.left.depth_first_traversal(result, c)

        if self.right is not None:
            c = constructor + '1'
            new_result += self.right.depth_first_traversal(result, c)

        for r in new_result:
            if r not in result:
                result.append(r)

        return result
