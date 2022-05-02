import os
from lib import *

if __name__ == "__main__":
    path = input("Which file do you wish to compress ? ")
    while not os.path.exists(path):
        print("This file doesn't exist, please try again")
        path = input("Which file do you wish to compress ? ")

    with open(path, "r") as file:
        file_text = file.read()
        characters, weights = get_letter_frequencies(file_text)
    original_size = os.path.getsize(path)

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
    #print(final_tree.toJSON())
    character_codes = final_tree.depth_first_traversal()

    alphabet_file_name = path.replace(".txt", "") + "_freq.txt"
    compressed_file_name = path.replace(".txt", "") + "_comp.bin"

    write_alphabet_frequency_file(alphabet_file_name, characters, weights)
    new_size = write_compressed_file(compressed_file_name, character_codes, file_text)

    print("File compressed successfully")

    # Display compression rate
    compression_rate = 1 - new_size/original_size
    print(f"Compression rate : {compression_rate*100}%")

    # Display Average bit count
    average = 0
    for i in character_codes:
        average += len(i[1])
    average = average / len(character_codes)
    print(f"Average bit count : {average}")
