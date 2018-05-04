str1 = "dudu bangbangda"
str2 = str1[3:8]
str3 = ""
print(str2)

for i in str1:
    str3 += i+'<T>'

print(str3)

str4 = "abababab"
str4 = str4.translate(str4.maketrans('a','s'))
print(str4)
