def validate_dict(rules, data):
    for key, prefix, middle, suffix in rules:
        if key in data:
            value = data[key]
            if (value.startswith(prefix) and
                middle in value[1:-1] and
                value.endswith(suffix)):
                continue
            else:
                return False
        else:
            return False
    return True

s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}

rezultat = validate_dict(s, d)
print(rezultat)