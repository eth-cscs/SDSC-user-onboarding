#!/usr/bin/env python3

import os
import argparse
import torchvision


parser = argparse.ArgumentParser(description='Fetch CIFAR10 dataset.')
parser.add_argument('--output', required=True)
args = parser.parse_args()

if os.path.isdir(args.output) and len(os.listdir(args.output)) > 0:
    raise RuntimeError(f"--output parameter {args.output} should be an empty directory")

# Downloading dataset
dataset_train = torchvision.datasets.CIFAR10(root=args.output, train=True, download=True)
dataset_test = torchvision.datasets.CIFAR10(root=args.output, train=False, download=True)
print(f"Finished fetching training and test dataset to {args.output}:\n{dataset_train}\n{dataset_test}")
