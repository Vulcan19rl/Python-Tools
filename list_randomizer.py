# simple list randomizer
# randomizes the order of the lines in a text file and creates a new text file with the new order in it
# author: Owen Russell-Lanning

import sys
import os
import random

# takes path to text file in and the path to output to
def main(in_path, out_path):
    
    lines = read_in_list(in_path)
    random.shuffle(lines) #randomize list
    write_list(lines, out_path)


# returns a list of lines from a text file as a list of strings
def read_in_list(in_path):
    if not os.path.exists(in_path):
        raise FileNotFoundError("File at in path does not exist")
    else:
        with open(in_path) as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            return lines

#writes a list of strings to a new file
def write_list(ls, out_path):
    if os.path.exists(out_path):
        result = input("Overwrite existing file? (y/n):")
        if(result.lower() != "y"):
            print("Exiting randomizsation")
            return
    
    #write to file
    with open(out_path, 'w') as file:
        for s in ls:
            file.write("%s\n" % s)





        


if __name__ == "__main__":
    if(len(sys.argv) < 3):
        print("Not enough inputs given. Please specify an input path and an output path")
    else:
        main(sys.argv[1], sys.argv[2])
