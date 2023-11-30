import uncompyle6
import hidden_4

def print_hidden_names(module):
    names = [name for name in dir(module) if not name.startswith('__')]
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_hidden_names(hidden_4)
