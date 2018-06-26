#!/usr/bin/python
import sys
import glob
import os
import shutil
from shutil import copyfile
import numpy.random as rand
'''
Splits a dataset into an 80/20 train/test set by sampling from a binomial
distribution with each datapoint deciding which set it belongs to.
'''
#this is concatenating the folder and using the results
'''
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: splitdata inputFname trainFname testFname\n" +
              "   Creates a random 80/20 train/test set")
        sys.exit(1)
    (fname, train_fname, test_fname) = sys.argv[1:]

    try:
        train = open(train_fname, 'w')
        test = open(test_fname, 'w')
        f = open(fname, 'r')

        for l in f:
            if rand.binomial(1, 0.8):
                train.write(l)
            else:
                test.write(l)
    finally:
        train.close()
        test.close()
        f.close()
        directory = os.path.dirname(file_path)
	try:
	    os.stat(directory)
	except:
	    os.mkdir(directory)
'''
glob.glob("/Users/sriramreddy/Downloads/523/augmented_data_set/")
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: splitdata inputFname trainFname testFname\n" +
              "   Creates a random 80/20 train/test set")
        sys.exit(1)
    (fname, train_fname, test_fname) = sys.argv[1:]
    try:
        os.stat(train_fname)
        os.stat(train_fname)
    except:
        os.mkdir(train_fname)
        os.mkdir(test_fname)

    try:
        for l in glob.glob(fname+"/*"):
            if rand.binomial(1, 0.8):
                shutil.copy2(l, train_fname)
                #copyfile(l, train_fname)
            else:
                shutil.copy2(l, test_fname)
                #copyfile(l, test_fname) It allows to be a folder
    finally:
        print("done")
