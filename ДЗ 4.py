import string

inp = '     Should, *&$&^(*I. subscribe? Yes!'

new_str_list = ''.join([i for i in inp if i not in string.punctuation]).split()
new_str = ''.join([i.title() for i in new_str_list])

print('#' + new_str if len(new_str) <= 139 else '#' + new_str[:139])













