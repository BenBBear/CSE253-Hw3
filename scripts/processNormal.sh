#!/usr/bin/env sh

rm -rf ./data/cifar100-dtrain-normalize

rm -rf ./data/cifar100-dtest-normalize  

python ./scripts/process.py ./data/cifar100-raw/train ./data/cifar100-raw/test True

mv ./dtrain ./data/cifar100-dtrain-normalize

mv ./dtest ./data/cifar100-dtest-normalize  
