"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

with open('./foo.txt', 'r') as file:
	for line in file:
		print(line)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

print('\n---\n')

with open('./bar.txt', 'w') as file:
	file.write('this is an arbitrary line of content\n')
	file.write('this is another arbitrary line of content\n')
	file.write('this is yet ANOTHER arbitrary line of content')

with open('./bar.txt', 'r') as file:
	for line in file:
		print(line)
