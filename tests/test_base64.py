#!/usr/bin/env python3

import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from datastore import Cipher, pyDataStore


objDict = {"object": "test_datastore", "data": {"user": "dummy-user", "pass": "123qwe456asd789zxc"}}

print(f"Raw: {objDict}")

# Create an instance that will store the data in a file named base64.store.
# Default encoding is set to Base64.
ds64 = pyDataStore(fileDataStore="base64.store", cipher=Cipher.Base64)

# This is the default where the data will be stored in a file named data.store and will be encoded in Base64.
#ds64 = pyDataStore()

# Dump or store the dictionary object.
ds64.dump(objDict)

# Based64 Encoded.
print(f"Base64: {objDict}")

# Retrieve the stored encoded dict object.
data64 = ds64.load("test_datastore")

print(f"Decoded: {data64}")
print()

print(f"Version: {ds64.version()}")
print(f"Author: {ds64.author()}")
print(f"License: {ds64.license()}")
print()
