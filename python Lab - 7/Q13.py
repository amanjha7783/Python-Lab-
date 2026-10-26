original = {'a': 5, 'b': 15, 'c': 8, 'd': 20}

new = {key: value for key, value in original.items() if value > 10}
print(new)