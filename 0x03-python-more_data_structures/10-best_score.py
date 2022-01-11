#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    new_dict = dict(sorted(a_dictionary.items(), key=lambda x: x[1]))
    highest = next(reversed(new_dict.keys()))

    return highest
