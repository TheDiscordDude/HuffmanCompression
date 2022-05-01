def get_letter_frequency(string: str) -> tuple:
    """

    :param string:
    :return:
    """
    characters = list(set(string))
    weights = []
    for c in characters:
        weights.append(string.count(c))

    # Sorting values by weight
    zipped = zip(weights, characters)
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
    weights = []
    for v in arrays.items():
        sorted_pairs = sorted(v[1], key=lambda tup: tup[1])
        for pair in sorted_pairs:
            characters.append(pair[1])
            weights.append(pair[0])

    return characters, weights


def write_compressed_file(file_name: str, character_codes: list, text:str) -> int:
    """

    :param file_name:
    :param character_codes:
    :return:
    """
    with open(file_name, "wb") as f:
        content = ""

        for c in text:
            for c2 in character_codes:
                if c == c2[0]:
                    content+=c2[1]


        byte_length = len(content) // 8 + (1 if len(content) % 8 != 0 else 0)

        byte_content = int(content, base=2).to_bytes(byte_length, "big")

        f.write(byte_content)

        return byte_length


def write_alphabet_frequency_file(file_name: str, characters, weights) -> None:
    """

    :param file_name:
    :param characters:
    :param weights:
    """
    with open(file_name, "w") as f:
        content = str(len(characters)) + "\n" + "\n".join(f"{c} {w}" for c, w in zip(characters, weights))
        f.write(content)
