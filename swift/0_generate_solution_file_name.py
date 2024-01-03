import argparse
import os

parser = argparse.ArgumentParser(description='Generate file by provided string. Generation replaces symbols and spaces to underscore')
parser.add_argument('filename', metavar='Filename', type=str, nargs='+')

args = parser.parse_args()

filename_array = args.filename
filtered_string_with_extension = "_".join(filename_array).replace(".", "") + ".swift"
print(filtered_string_with_extension)
