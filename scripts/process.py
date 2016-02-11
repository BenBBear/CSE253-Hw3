from __future__ import division
import lmdb
import cPickle
import numpy as np
import caffe
import sys
from collections import defaultdict

TOTAL = 32*32.0
width = 32
height = 32



path_train = sys.argv[1]
path_test = sys.argv[2]
gcm = sys.argv[3]
imageNumber = int(sys.argv[4])

if gcm == 'False':
    gcm = False
else:
    gcm = True

ftest = open(path_test, 'rb')
ftrain = open(path_train, 'rb')
dtest = cPickle.load(ftest)
dtrain = cPickle.load(ftrain)

Counting = defaultdict(lambda :0)

def global_contrast_normalize(X, scale=1., subtract_mean=True, use_std=False, sqrt_bias=0., min_divisor=1e-8):
    X = np.reshape(X,(32,32))
    scale = float(scale)
    assert scale >= min_divisor
    # Note: this is per-example mean across pixels, not the
    # per-pixel mean across examples. So it is perfectly fine
    # to subtract this without worrying about whether the current
    # object is the train, valid, or test set.
    mean = X.mean(axis=1)
    if subtract_mean:
        X = X - mean[:, np.newaxis]  # Makes a copy.
    else:
        X = X.copy()

    if use_std:
        # ddof=1 simulates MATLAB's var() behaviour, which is what Adam
        # Coates' code does.
        ddof = 1

        # If we don't do this, X.var will return nan.
        if X.shape[1] == 1:
            ddof = 0

        normalizers = np.sqrt(sqrt_bias + X.var(axis=1, ddof=ddof)) / scale
    else:
        normalizers = np.sqrt(sqrt_bias + (X ** 2).sum(axis=1)) / scale

    # Don't normalize by anything too small.
    normalizers[normalizers < min_divisor] = 1.

    X /= normalizers[:, np.newaxis]  # Does not make a copy.

    X = np.reshape(X,(int(TOTAL)))
    return X


def process(dbName, dtrain, gcm=False, imageNumber=False):
    size = 4
    if gcm:
        size = 10
    traindb = lmdb.open(dbName, map_size=dtrain['data'].nbytes * size)
    with traindb.begin(write=True) as txn:
        for i in range(len(dtrain['data'])):
            image = dtrain['data'][i]  ## 1024,1024,1024
            label = dtrain['fine_labels'][i]

            if imageNumber != -1:
                if Counting[label] >= imageNumber:
                    continue
                else:
                    Counting[label] += 1

            datum = caffe.proto.caffe_pb2.Datum()
            datum.channels = 3
            datum.height = 32
            datum.width = 32
            if gcm:
                data = image
                R = data[:1024]
                G = data[1024:2048]
                B = data[2048:3072]
                data = np.zeros(int(TOTAL*3), dtype='f')
                data[:1024] = global_contrast_normalize(R)
                data[1024:2048] = global_contrast_normalize(G)
                data[2048:3072] = global_contrast_normalize(B)
            else:
                data = image

            datum.data = data.tostring()
            datum.label = int(label)
            str_id = '{:08}'.format(i)
            txn.put(str_id.encode('ascii'), datum.SerializeToString())


process('dtrain', dtrain, gcm=gcm, imageNumber=imageNumber)
process('dtest', dtest, gcm=gcm, imageNumber=imageNumber)
ftest.close()
ftrain.close()
## For Mirror and Crop, they could be accomplished easily with Caffe
