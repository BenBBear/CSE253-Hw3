#!/usr/bin/env sh

rm -rf ./data/cifar-dtrain
rm -rf ./data/cifar-dtest  

python ./scripts/process.py ./data/cifar100-raw/train ./data/cifar100-raw/test False

mv ./dtrain ./data/cifar-dtrain
mv ./dtest ./data/cifar-dtest  
