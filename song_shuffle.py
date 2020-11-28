import sys
import os.path
import random

eol = '\n'
NOK = 1
OK = 0

def song_print(song): 
    """Prints songs paragraphs, puts new line between paragraphs
    """
    head = True
    for par in song: 
        if head: head = False
        else: print()
        for line in par: print(line)     

def song_shuffle(infile):
    """ Prints shuffled paragraphs from infile using new line as delimiter 
    """
    f = open(infile, 'r')
    master_list = []
    sub_list = []

    for line in f: 
        if line == eol:
            master_list.append(sub_list)
            sub_list=[]
        else:
            sub_list.append(line.rstrip(eol))
    if sub_list != []: master_list.append(sub_list)

    f.close()

    random.shuffle(master_list)
    song_print(master_list)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('one argument expected')
        sys.exit(NOK)

    infile = sys.argv[1]
    if not os.path.exists(infile):
        print('file not found')
        sys.exit(NOK)

    song_shuffle(infile)
    sys.exit(OK)