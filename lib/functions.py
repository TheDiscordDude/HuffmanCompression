def get_letter_frequency(string : str) -> tuple:
    characters = list(set(string))
    weights = []
    for c in characters :
        weights.append(string.count(c))

    zipped = zip(weights, characters)
    sorted_pairs = sorted(zipped)
    tuples = zip(*sorted_pairs)
    weights, characters = [ list(x) for x in tuples]

    return characters, weights
