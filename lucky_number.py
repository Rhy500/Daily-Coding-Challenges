def get_lucky_number(name):
    first, last = name.split()
    vowels = "aiueo"

    def count_letters(word):
        word = word.lower()
        v = sum(1 for c in word if c in vowels)
        c = sum(1 for c in word if c.isalpha() and c not in vowels)
        return v, c

    v1, c1 = count_letters(first)
    v2, c2 = count_letters(last)

    small = min(v1, v2) * min(c1, c2) * min(len(first), len(last))
    large = max(v1, v2) * max(c1, c2) * max(len(first), len(last))
    result = large - small
    return 13 if result == 0 else result

print(get_lucky_number("John Doe"))
print(get_lucky_number("Olivia Lewis")) 
print(get_lucky_number("James Wilson")) 
print(get_lucky_number("Elizabeth Hernandez")) 
print(get_lucky_number("Mike Walker")) 
print(get_lucky_number("Chloe Perez")) 