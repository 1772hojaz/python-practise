#!/usr/bin/python3
import marshal
import importlib.util

with open("hidden_4.pyc", "rb") as f:
    header_size = len(importlib.util.MAGIC_NUMBER) + 12
    f.read(header_size)
    code = marshal.load(f)

print(code.co_consts)

