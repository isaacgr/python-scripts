"""Calls ifconfig and splits the output into files according to the interface"""
import os
import subprocess
import argparse


def write_interfaces(filepath):
    interfaces = subprocess.check_output('ifconfig', shell=True)
    iface_list = interfaces.split('\n')
    devices = subprocess.check_output('ls /sys/class/net', shell=True).split()

    for device in devices:
        filepath = filepath + device + '.txt'
        with open(filepath, 'w+') as f:
            



def main():
    parser = argparse.ArgumentParser(description='Save ifconfig output to files')
    parser.add_argument('--filepath', help='Path to store the files')
    options = parser.parse_args()

    filepath = options.filepath

    if filepath is None:
        filepath = os.getcwd()

    write_interfaces(filepath)


if __name__ == '__main__':
    main()
