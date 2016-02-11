#!/usr/bin/env sh

rm -rf ./data/cifar100-dtrain-100
rm -rf ./data/cifar100-dtest-100 

python ./scripts/process.py ./data/cifar100-raw/train ./data/cifar100-raw/test True  100

mv ./dtrain ./data/cifar100-dtrain-100
mv ./dtest ./data/cifar100-dtest-100   
