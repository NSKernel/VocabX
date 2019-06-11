# 
import numpy
import pandas
import sys
import os
import readchar

df = pandas.read_csv("wordlist.csv", sep = ',', header = None)
word_list = df.values
numpy.random.shuffle(word_list)
zeros = numpy.zeros(word_list.shape[0],dtype=numpy.int)
zeros = numpy.atleast_2d(zeros)
zeros = zeros.reshape(word_list.shape[0], 1)
word_list = numpy.hstack((word_list, zeros))
done_array = numpy.ndarray([])
done_array = numpy.array([], dtype=numpy.str).reshape(0, 3)

while word_list.shape[0] != 0:
    os.system('clear')
    print("")
    entry = word_list[0]
    word_list = numpy.delete(word_list, 0, axis=0)
    print("  Word: [", end = "")
    print(done_array.shape[0], end = "")
    print("/", end = "")
    print(word_list.shape[0] + done_array.shape[0] + 1, end = "")
    print("]\n")
    print("  ",end="")
    if (entry[2] == 2):
        print("*", end = "")
    print(entry[0])
    print("")
    print("  Do you know it?", end="")
    sys.stdout.flush()
    str = readchar.readkey()
    os.system('clear')
    print("")
    print("  Word: [", end = "")
    print(done_array.shape[0], end = "")
    print("/", end = "")
    print(word_list.shape[0] + done_array.shape[0] + 1, end = "")
    print("]\n")
    print("  ",end="")
    if (entry[2] == 2):
        print("*", end = "")
    print(entry[0])
    print("")
    print("  The meaning is:\n")
    print("  ",end="")
    print(entry[1],end="")
    sys.stdout.flush()
    if (str == "q"):
        os.system("clear")
        print("Exiting VocabX...")
        break
    if (str == "y"):
        print("\n")
        print("  Are you sure you know it?",end="")
        sys.stdout.flush()
        str = readchar.readkey()
        if (str == 'y'):
            if (entry[2] == 2):
                entry[2] = 1
                if (word_list.shape[0] <= 10 or str == 'l'):
                    word_list = numpy.vstack([word_list, entry])
                else:
                    word_list = numpy.insert(word_list, 9, entry, axis=0)
            else:
                if (entry[2] == 1):
                    entry[2] = 0
                    word_list = numpy.vstack([word_list, entry])
                else:
                    done_array = numpy.vstack([done_array, entry])
        else:
            if (str == "l"):
                # add to later
                print(" -> ",end="")
                sys.stdout.flush()
                entry[2] = 0
                word_list = numpy.vstack([word_list, entry])
            else:
                entry[2] = 2
                print(" x  ",end="")
                sys.stdout.flush()
                if (word_list.shape[0] <= 10):
                    word_list = numpy.vstack([word_list, entry])
                else:
                    word_list = numpy.insert(word_list, 9, entry, axis=0)
    else:
        if (str == "l"):
            # add to later
            print(" -> ",end="")
            sys.stdout.flush()
            entry[2] = 0
            word_list = numpy.vstack([word_list, entry])
        else:
            entry[2] = 2
            print(" x  ",end="")
            sys.stdout.flush()
            if (word_list.shape[0] <= 10):
                word_list = numpy.vstack([word_list, entry])
            else:
                word_list = numpy.insert(word_list, 9, entry, axis=0)
        readchar.readkey()

os.system("clear")
print("Congratulations! You have finished the word list!")