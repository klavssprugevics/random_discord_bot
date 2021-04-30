import json
    
def get_secret(key):
    with open('secrets.json') as secrets_file:
        secrets = json.load(secrets_file)

        try:
            return secrets[key]
        except KeyError:
            raise Exception("Couldn't find secret with given key.")