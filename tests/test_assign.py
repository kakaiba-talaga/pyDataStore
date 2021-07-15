objDict = {"object": "test_datastore", "data": {"user": "dummy-user", "pass": "123qwe456asd789zxc"}}

def assign_datastore():
    global dataStore, cipher
    from pyDataStore import Cipher, DataStore

    dataStore = DataStore
    cipher = Cipher.Base64

if __name__ == "__main__":
    assign_datastore()

    ds64 = dataStore(fileDataStore="assign.store", cipher=cipher)
    ds64.dump(objDict)

    print(f"Base64: {objDict}")

    data64 = ds64.load("test_datastore")

    print(f"Decoded: {data64}")
