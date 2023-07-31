# File I/O (input/output) mode
#   r - read
#   w - write (覆盖)
#   a - append (追加)

# (1) open file for read/write/append
file = open('sonnet.txt', 'r')

# (2) process the file, reading all content in this case
content = file.read()
print(content)

# (3) close the file
file.close()

# (1) open file for read/write/append
file = open('mypoem.txt', 'w')

# (2) process the file, writing content in this case
file.write('I am a poet\n')
file.write('I am a poet\n')
file.write('I am a poet\n')

# (3) close the file
file.close()

# automatic resource management 自动资源管理
with open('sonnet.txt', 'r') as file:
    content = file.read()
    print(content)

# as soon as the block ends, the file is closed automatically
