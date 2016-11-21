"""
run an estimator against command line data

Intentionally generic so it can be used in many examples. 
This is why interpreting the labels is left to the reader.
"""

import argparse
import pickle
import numpy as np

def run():
    parser = argparse.ArgumentParser("predict rain based on measurements")
    args = parser.add_argument("pickle", type=argparse.FileType('rb'))
    # arbitary number of float parameters
    args = parser.add_argument("params", nargs='+', type=float)
    args = parser.parse_args()
    estimator = pickle.load(args.pickle)
    print ("using estimator %s " % str(estimator))
    data = np.array(args.params)
    class_ = estimator.predict(data)
    print("predicted: %d" % class_)

if __name__ == "__main__":
    run()
