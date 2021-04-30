import json

# Reads a json file and returns the value from a given key
def get_value_from_json(key, filename):
    with open(filename) as file:
        dictionary = json.load(file)

        try:
            return dictionary[key]
        except KeyError:
            raise Exception('Could not find value with the given key.')


# Reads and returns a json file
def open_json(filename):
    with open(filename) as dictionary:
        json_dict = json.load(dictionary)
        return json_dict
