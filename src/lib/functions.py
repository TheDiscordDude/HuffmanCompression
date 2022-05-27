from typing import List


def get_letter_frequencies(text: str) -> tuple:
    """
    Scans the string passed in argument to get all the letters and their number of appearance in the string

    :param text: The string that we need to examine
    :return: 2 arrays : the first one is the characters and the second array is the frequencies of these characters
    """
    # We get all the different characters in the text :
    characters = list(set(text))

    # We then set the frequencies
    frequencies = []
    for c in characters:
        frequencies.append(text.count(c))

    # Sorting values by frequency
    zipped = zip(frequencies, characters)
    sorted_pairs = sorted(zipped)

    # Sorting values by character
    # We split the sorted pairs into arrays with the same weight
    arrays = {}
    for i in sorted_pairs:
        if i[0] in arrays.keys():
            arrays[i[0]] += [i]
        else:
            arrays[i[0]] = [i]
    # then we sort all the arrays individually
    characters = []
    frequencies = []
    for v in arrays.items():
        sorted_pairs = sorted(v[1], key=lambda tup: tup[1])
        for pair in sorted_pairs:
            characters.append(pair[1])
            frequencies.append(pair[0])

    if "\n" in characters:
        i = characters.index("\n")
        characters[i] = "\\n"
    return characters, frequencies


def write_compressed_file(file_name: str, character_codes: list, text: str) -> int:
    """
    Writes the bin file corresponding to the compressed file

    :param text: the text we need to compress
    :param file_name: the name of the output file
    :param character_codes: the list of the characters with their bin code
    :return: the length of the file in bytes.
    """
    with open(file_name, "wb") as f:
        content = ""
        for c in text:
            for c2 in character_codes:
                if c == c2[0] or (c == "\n" and c2[0] == "\\n"):
                    content += c2[1]

        byte_length = len(content) // 8 + (1 if len(content) % 8 != 0 else 0)

        while len(content) != byte_length * 8:
            content = content + "0"

        byte_content = int(content, base=2).to_bytes(byte_length, "big")
        f.write(byte_content)
        return byte_length


def write_alphabet_frequency_file(file_name: str, characters: List[str], frequencies: List[int]) -> None:
    """
    Writes the alphabet file with the frequency of each character

    :param file_name: the name of the output file
    :param characters: the characters used in the text
    :param frequencies: the frequencies of each character
    """
    with open(file_name, "w") as f:
        content = str(len(characters)) + "\n" + "\n".join(f"{c} {w}" for c, w in zip(characters, frequencies))
        f.write(content)
