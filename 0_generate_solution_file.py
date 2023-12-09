import argparse
import os

parser = argparse.ArgumentParser(description='Generate file by provided string. Generation replaces symbols and spaces to underscore')
parser.add_argument('filename', metavar='Filename', type=str, nargs='+')

args = parser.parse_args()

filename_array = args.filename
filtered_string_with_extension = "_".join(filename_array).replace(".", "") + ".py"
print(filtered_string_with_extension)

if os.path.isfile(filtered_string_with_extension):
    print("File for such path already exists")
else:
    f = open(filtered_string_with_extension, "w")
    f.write('"""\n\n"""\n\n"""\n\n"""\n')
    f.close()