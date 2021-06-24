#!/usr/bin/env python3

import os, sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from datastore import Cipher, pyDataStore


objDict = {"object": "test_datastore", "data": {"user": "dummy-user", "pass": "123qwe456asd789zxc"}}

print(f"Raw: {objDict}")

# Create an instance that will store the data in a file named AES.store.
# Encoding is set to AES.
dsAES = pyDataStore(fileDataStore="aes.store", cipher=Cipher.AES, aesKey="SPECIFY_AN_AES_KEY_HERE")

# Dump or store the dictionary object.
dsAES.dump(objDict)

# AES Encoded.
print(f"AES: {objDict}")

# Retrieve the stored encoded dict object.
dataAES = dsAES.load("test_datastore")

print(f"Decoded: {dataAES}")
print()

print(f"Version: {dsAES.version()}")
print(f"Author: {dsAES.author()}")
print(f"License: {dsAES.license()}")
print()
