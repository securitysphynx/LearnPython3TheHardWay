from sys import argv
# os.path.exists() returns True if path refers to an existing path or an open file descriptor. On some platforms, this function may return False if permission is not granted to execute os.stat() on the file. Can now be an integer: True is returned if it is an open file descriptor, False otherwise. Accepts a path-like object.
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

#We could do these two on one line
in_file = open(from_file)
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready? hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print("Allright. All done.")

out_file.close()
in_file.close()