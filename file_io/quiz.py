f=open('data.txt', 'r')
#Prints the text as one single string
lines = f.read()
# Prints a list of strings
# lines = f.readlines()
f.close()
print(lines)