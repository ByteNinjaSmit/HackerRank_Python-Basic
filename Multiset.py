#!/bin/python3

import math
import os
import random
import re
import sys


class Multiset:
    def __init__(self):
        self.elements = {}

    def add(self, val):
        if val in self.elements:
            self.elements[val] += 1
        else:
            self.elements[val] = 1

    def remove(self, val):
        if val in self.elements:
            if self.elements[val] > 1:
                self.elements[val] -= 1
            else:
                del self.elements[val]

    def __contains__(self, val):
        return val in self.elements

    def __len__(self):
        return sum(self.elements.values())

# Example usage:
multiset = Multiset()

# Process operations
num_operations = int(input())
result = []

for _ in range(num_operations):
    operation = input().split()
    command = operation[0]

    if command == "add":
        val = int(operation[1])
        multiset.add(val)
    elif command == "remove":
        val = int(operation[1])
        multiset.remove(val)
    elif command == "query":
        val = int(operation[1])
        result.append(val in multiset)
    elif command == "size":
        result.append(len(multiset))

# Print results
for res in result:
    print(res)

