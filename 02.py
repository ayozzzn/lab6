def count_case(s):
    result = {
        "Uppercase": sum(1 for c in s if c.isupper()),
        "Lowercase": sum(1 for c in s if c.islower())
    }
    return result

s = "Hello World! Python is Awesome."
print(count_case(s))
