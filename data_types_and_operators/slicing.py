hi_str = "Hello world!"
print(hi_str)

print(len(hi_str))

print("Get first character...")
print(hi_str[0])

print("Get last character...")
print(hi_str[-1])
print(hi_str[11])

print("Third character to 5th character")
# formula for slicing: hi_str[<starting index>:<ending index>]
print(hi_str[2:5])

print("index 6 to end")
print(hi_str[6:])

# 0 1 2 3 4 5 6 7 8 9 10 11
# H e l l o   w o r l  d  !
#                   -3-2 -1

print("3rd last character to the end")
print(hi_str[-3:])

print("beginning until 5th index")
print(hi_str[:5])

