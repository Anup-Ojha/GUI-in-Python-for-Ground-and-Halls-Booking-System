import sys,keyword
print('python',sys.version)
print('python Interpreter Version',sys.executable)
print('python Module Search Path:',sys.path)
for dir in sys.path:
    print(dir)

print('Python Keyords:')
for word in keyword.kwlist:
    print(word)
