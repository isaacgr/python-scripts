"""Print the files containing the specified extension in a given filepath"""
import os
import sys
import argparse


def get_files(filepath, file_extension):
    """Get the filenames containing the given extension"""
    extension = '.' + file_extension if '.' not in file_extension else file_extension
    files = os.listdir(filepath)

    file_list = []
    for filename in files:
        if extension in filename:
            file_list.append(filename)

    return file_list


def main():
    parser = argparse.ArgumentParser(description='List files matching extension given')
    parser.add_argument('--filepath', help='Folder path to list files')
    parser.add_argument('--file-extension', help='Extension of the files to list')

    options = parser.parse_args()
    filepath = options.filepath

    if not options.filepath:
        filepath = os.path.dirname(os.path.realpath(__file__))

    if not options.file_extension:
        print 'No file extension listed'
        sys.exit(-1)

    files = get_files(filepath, options.file_extension)
    if not files:
        print '\nNo files with that extension'
        return
    print '\n' + ', '.join(files)


if __name__ == '__main__':
    main()
