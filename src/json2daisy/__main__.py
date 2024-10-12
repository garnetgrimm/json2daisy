import os
import sys
from .json2daisy import generate_header_from_file, generate_header_from_name


if __name__ == '__main__':
    for source in sys.argv[1:]:
        if os.path.exists(source) and os.path.isfile(source):
            header, info = generate_header_from_file(source)

        outfile = source.replace('.json', '.h')
        with open(outfile, 'w') as file:
            file.write(header)

        print(f'Generated Daisy C++ header in "{outfile}"')
