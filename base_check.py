def is_valid_number(n, base):
    if base < 2 or base > 36:
        return False
    
    for ch in n.upper():
        if '0' <= ch <= '9':
            value = ord(ch) - ord('0')
        elif 'A' <= ch <= 'Z':
            value = ord(ch) - ord('A') + 10
        else:
            return False
        
        if value >= base:
            return False
    return True

print(is_valid_number("10101", 2))
print(is_valid_number("10201", 2))
print(is_valid_number("76543210", 8))
print(is_valid_number("9876543210", 8)) 
print(is_valid_number("9876543210", 10))
print(is_valid_number("ABC", 10)) 
print(is_valid_number("ABC", 16))
print(is_valid_number("Z", 36))
print(is_valid_number("ABC", 20)) 
print(is_valid_number("4B4BA9", 16)) 
print(is_valid_number("5G3F8F", 16)) 
print(is_valid_number("5G3F8F", 17)) 
print(is_valid_number("abc", 10)) 
print(is_valid_number("abc", 16)) 
print(is_valid_number("AbC", 16)) 
print(is_valid_number("z", 36))