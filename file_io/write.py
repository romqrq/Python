f=open('newfile.txt', 'w') #we can use 'r', 'w' or 'a': read, write and append
# f.write("Hello\n")
lines = ['Hello', 'World', 'Welcome', 'To', 'File IO']
#without "text = ...." it prints all words together with no spaces
text = '\n'.join(lines)
f.writelines(text)
f.close()