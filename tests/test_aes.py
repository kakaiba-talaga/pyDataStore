#!/usr/bin/env python3

from pyDataStore import Cipher, DataStore


objDict = {"object": "test_datastore", "data": {"user": "dummy-user", "pass": "123qwe456asd789zxc"}}

print(f"Raw: {objDict}")

# Create an instance that will store the data in a file named AES.store.
# Encoding is set to AES.
dsAES = DataStore(fileDataStore="aes.store", cipher=Cipher.AES, aesKey="SPECIFY_AN_AES_KEY_HERE")

# Dump or store the dictionary object.
dsAES.dump(objDict)

# At this point, the objDict dict object is already encoded.

# AES Encoded.
print(f"AES: {objDict}")

# Retrieve the stored encoded dict object.
dataAES = dsAES.load("test_datastore")

print(f"Decoded: {dataAES}")
print()

print(f"Version: {dsAES.__version__}")
print(f"Author: {dsAES.__author__}")
print(f"License: {dsAES.__license__}")
print()
