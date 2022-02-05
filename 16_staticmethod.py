#!/usr/bin/env python3
import os
class Executor:
    def __init__(self, command):
        self.command = command
    @staticmethod
    def chdir(path):
        os.chdir(path)

orig_path = os.getcwd()
print(orig_path)
Executor.chdir("/tmp/")
print(os.getcwd())
Executor("test").chdir(orig_path)
print(os.getcwd())
