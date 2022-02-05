#!/usr/bin/env python3
# staticmethod

import os

class Executor:
    def __init__(self, command):
        self.command = command
    @staticmethod
    def chdir(path):
        os.chdir(path)
    def __call__(self):
        os.system(self.command)
orig_path = os.getcwd()
print(orig_path)
executor = Executor("ls|wc -l")
Executor.chdir("/tmp/")
print(executor())
print(os.getcwd())
executor.chdir(orig_path)
print(os.getcwd())
print(executor())
