import marshal

def print_hidden_names():
    with open("hidden_4.pyc", "rb") as file:
        magic_number = file.read(4)
        timestamp = file.read(4)
        code_object = marshal.load(file)

        names = [name for name in code_object.co_names if not name.startswith("__")]
        for name in sorted(set(names)):
            print(name)

if __name__ == "__main__":
    print_hidden_names()
