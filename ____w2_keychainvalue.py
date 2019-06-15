import os
import tempfile
import argparse 
import json

storage_file = os.path.join(tempfile.gettempdir(), 'storage.json')

if not os.path.isfile(storage_file):
    storage = dict()
else:
    with open(storage_file) as f:
        storage = json.load(f)

def store(*args, **kwargs):
    with open(storage_file, 'w') as f:
        json.dump(storage, f)

def addendum(key, value):
    if key not in storage:
        storage[key] = list()
        storage[key].append(value)
    else:
            storage[key].append(value)
            
def get(key):
    if key in storage:
        return storage[key]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', help='The key', action='store', dest='key', required=True)
    parser.add_argument('--val', help='Value to the key', action='store', dest='value', required=False)
    args = parser.parse_args()

    if args.value == None:
        if args.key in storage:
            print(', '.join(storage.get(args.key)))
        else:
            return

    else:
        print("The key is {} and the value is {}".format(args.key, args.value))
        addendum(args.key, args.value)
        store(storage)
    
if __name__ == "__main__":
    main()
