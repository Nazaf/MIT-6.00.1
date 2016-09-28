count = 0

#s is the variable containing a string of characters
for i in range(len(s)):
    if s[i].startswith('b') and s[i:i+3]=='bob':
        count+=1
print("Number of times bob occurs is: ", count)
