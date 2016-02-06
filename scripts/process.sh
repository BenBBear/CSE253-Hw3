#!/usr/bin/env sh

rm -rf ./data/cifar100-dtrain
rm -rf ./data/cifar100-dtest  

python ./scripts/process.py ./data/cifar100-raw/train ./data/cifar100-raw/test False

mv ./dtrain ./data/cifar100-dtrain
mv ./dtest ./data/cifar100-dtest  
