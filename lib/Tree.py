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
        freq = self.get_frequency() + other.get_frequency()
        new_tree = Tree(freq, self, other, None)
        return new_tree

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def depth_first_traversal(self, result=[], constructor=""):
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
    return tree.frequency
