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
        return (
            os.popen(self.command)
            .read().strip()
        )
orig_path = os.getcwd()
executor = Executor("ls|wc -l")
print(os.getcwd())
print(executor())
Executor.chdir("/tmp/")
print(os.getcwd())
print(executor())
executor.chdir(orig_path)
print(os.getcwd())
