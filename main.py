import os
from lib import *

if __name__ == "__main__":
    #path = input("Which file do you wish to compress ? ")
    path = "textesimple.txt"
    while not os.path.exists(path):
        print("This file doesn't exist, please try again")
        path = input("Which file do you wish to compress ? ")

    with open(path, "r") as file:
        characters, weights = get_letter_frequency(file.read())
        forest = []
        for character, weight in zip(characters, weights):
            forest.append(Tree(weight, None, None, character))

        while len(forest) > 1:
            first_tree = forest.pop(0)
            second_tree = forest.pop(0)
            fusion_tree = first_tree + second_tree

            forest.append(fusion_tree)
            forest = sorted(forest, key=sort_tree)

        final_tree = forest[0]
        character_codes = final_tree.depth_first_traversal()
        print(character_codes)
        alphabet_file_name = path.replace(".txt", "") + "_freq.txt"
        with open(alphabet_file_name, "w") as f:
            content = str(len(character_codes)) + "\n" + "\n".join(f"{c} {w}" for c, w in zip(characters, weights))
            print(content)
            f.write(content)

