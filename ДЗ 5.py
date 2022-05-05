import string

inp = input()

letters_list = string.ascii_letters + 'a'
start_ind = string.ascii_letters.index(inp[0])
end_ind = string.ascii_letters.index(inp[-1]) + 1

print(letters_list[start_ind:end_ind])
    
