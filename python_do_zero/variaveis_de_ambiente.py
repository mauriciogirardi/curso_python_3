import os

print(os.environ['HOME'])
print(os.environ['SHELL'])
print(os.getenv('HOME'))

FILE_NAME = 'files/menu.csv'

print(os.path.getctime(FILE_NAME))
print(os.path.getmtime(FILE_NAME))
print(os.path.getatime(FILE_NAME))
print(os.path.isfile(FILE_NAME))
print(os.path.isdir(FILE_NAME))
print(os.path.islink(FILE_NAME))
print(os.path.ismount(FILE_NAME))
