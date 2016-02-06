#!/usr/bin/env sh
mkdir data
wget "https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz"
tar xvf cifar-100-python.tar.gz 
mv cifar-100-python data/cifar100-raw
rm cifar-100-python.tar.gz