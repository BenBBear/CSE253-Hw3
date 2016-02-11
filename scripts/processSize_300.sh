#!/usr/bin/env sh

rm -rf ./data/cifar100-dtrain-300
rm -rf ./data/cifar100-dtest-300

python ./scripts/process.py ./data/cifar100-raw/train ./data/cifar100-raw/test True  300

mv ./dtrain ./data/cifar100-dtrain-300
mv ./dtest ./data/cifar100-dtest-300
