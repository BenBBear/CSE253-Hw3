#!/usr/bin/env sh

rm -rf ./data/cifar-dtrain-normalize

rm -rf ./data/cifar-dtest-normalize  

python ./scripts/process.py ./data/cifar100-raw/train ./data/cifar100-raw/test True

mv ./dtrain ./data/cifar-dtrain-normalize

mv ./dtest ./data/cifar-dtest-normalize  
