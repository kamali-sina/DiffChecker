import os
import sys

class DiffChecker:
    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2
    
    def check(self):
        file1 = open(self.path1)
        file2 = open(self.path2)
        lines1 = file1.readlines()
        lines1 = list(map(lambda x: x.strip(), lines1))
        lines2 = file2.readlines()
        lines2 = list(map(lambda x: x.strip(), lines2))
        file1.close()
        file2.close()
        errors = 0
        for line in lines1:
            if (line not in lines2):
                print(f'<<<{line}')
                errors += 1
            else:
                ind = lines2.index(line)
                lines2.pop(ind)
        if (len(lines2) == 0 and errors == 0):
            print('the two filles are identical')
            return
        for line in lines2:
            print(f'>>>{line}')

argv = sys.argv
if (len(argv) < 3):
    print('\nError: not enough arguments were provided!\n\nUsasge: python3 <filepath1> <filepath2>\n')
    exit(1)

checker = DiffChecker(argv[1], argv[2])
checker.check()