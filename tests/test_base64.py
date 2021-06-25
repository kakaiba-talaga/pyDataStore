#!/usr/bin/env python3

from pyDataStore import Cipher, DataStore


objDict = {"object": "test_datastore", "data": {"user": "dummy-user", "pass": "123qwe456asd789zxc"}}

print(f"Raw: {objDict}")

# Create an instance that will store the data in a file named base64.store.
# Default encoding is set to Base64.
ds64 = DataStore(fileDataStore="base64.store", cipher=Cipher.Base64)

# This is the default where the data will be stored in a file named data.store and will be encoded in Base64.
# ds64 = DataStore()

# Dump or store the dictionary object.
ds64.dump(objDict)

# At this point, the objDict dict object is already encoded.

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
