def update_dictionary(d, key, value):
    new_key = int(key)*2
    if key in d:
        d[key] += [value]
    if key not in d:
        if new_key not in d:
            d[new_key] = [value]
        else:
            d[new_key] += [value]
