import json


class Tree:
    def __init__(self, frequency: int, left=None, right=None, character=None):
        self.left = left
        self.right = right
        self.character = character
        self.frequency = frequency

    def get_frequency(self):
        return self.frequency

    def __str__(self):
        return f"Tree:{{" \
               f"{self.frequency}," \
               f"{self.character}," \
               f"{self.left}," \
               f"{self.right}" \
               f"}}"

    def __add__(self, other):
        """
        It creates a parent for the 2 trees. The frequency of the new tree is the addition of the frequencies of the trees.
        :param other: the other tree
        :return: the parent tree of the 2 trees
        """
        freq = self.get_frequency() + other.get_frequency()
        new_tree = Tree(freq, self, other, None)
        return new_tree

    def toJSON(self):
        """
        Transforms the current Tree into a JSON structure
        :return: a string representing te JSON object
        """
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def depth_first_traversal(self, result=[], constructor=""):
        """

        :param result:
        :param constructor:
        :return:
        """
        if self.left is None and self.right is None:
            return [[self.character, constructor]]

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


def sort_tree(tree: Tree) -> int:
    """

    :param tree:
    :return:
    """
    return tree.frequency
