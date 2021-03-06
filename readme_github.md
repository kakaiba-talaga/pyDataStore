# pyDataStore

Persistent and portable serialized data store.

A Python `dict` *object* that has been `dump`-ed can be `load`-ed or retrieved in the future.

To secure the *data*, it is using the `base64` package when encoding it in *Base64*, which is the default encoding, and `pycryptodome` package when encoding it in *AES*. Then, `pickle` to serialize the `dict` object.

## Requirements

This requires **Python** `>=3.5`, `<3.10`.

### Python Packages

- [pycryptodome](https://pypi.org/project/pycryptodome/) >= 3.10.1

## Installation

- Install the package in *Development* mode:

    ```bash
    pip install -e .
    ```

- Install the package through PyPI:

    ```bash
    pip install pyDataStore
    ```

## Usage

As this will be using **Python 3**, we have to set the *shebang* to the appropriate executable.

```bash
#!/usr/bin/env python3
```

To use `pyDataStore`, we have to import it first.

```python
from pyDataStore import Cipher, DataStore
```

Then, we can use this sample `dict` *object*.

```python
# Sample dict object.
objDict = {"object": "test_datastore", "data": {"user": "dummy-user", "pass": "123qwe456asd789zxc"}}
```

There is a **required format** for the `dict` *object*.

```python
{
    "object": "OBJECT_NAME",
    "data": {
        "DATA_KEY": "DATA_VALUE",
        "DATA_KEY": "DATA_VALUE",
        ...
    }
}
```

Otherwise, this will throw an `Exception`.

```text
Exception: This dict object has an invalid format.
```

### Base64 Encoding

- Using the default data store file.

    ```python
    print(f"Raw: {objDict}")

    # Create an instance that will store the data in a file named data.store (default).
    # Default encoding is set to Base64.
    ds64 = pyDataStore()

    # This is the same as the above.
    # ds64 = pyDataStore(fileDataStore="data.store", cipher=Cipher.Base64)

    # Dump or store the dictionary object.
    ds64.dump(objDict)

    # At this point, the objDict dict object is already encoded.

    # Based64 Encoded.
    print(f"Base64: {objDict}")

    # Retrieve the stored encoded dict object.
    data64 = ds64.load("test_datastore")

    print(f"Decoded: {data64}")
    ```

### AES Encoding

- Using a custom data store file.

    ```python
    print(f"Raw: {objDict}")

    # Create an instance that will store the data in a file named aes.store.
    # Encoding is set to AES.
    dsAES = pyDataStore(fileDataStore="aes.store", cipher=Cipher.AES, aesKey="SPECIFY_AN_AES_KEY_HERE")

    # Dump or store the dictionary object.
    dsAES.dump(objDict)

    # At this point, the objDict dict object is already encoded.

    # AES Encoded.
    print(f"AES: {objDict}")

    # Retrieve the stored encoded dict object.
    dataAES = dsAES.load("test_datastore")

    print(f"Decoded: {dataAES}")
    ```

## Test Scripts

You can use the test scripts under [./test](https://github.com/kakaiba-talaga/pyDataStore/blob/main/tests/readme.md).

---

## Packaging

To be able to make the project installable from a Package Index like *PyPI*, we need to create a Distribution *(AKA "Package")* for it.

Before you can build *wheels* and *source distribution* for the project, we need to install the build package:

```bash
pip install build
```

### Distribution

Minimally, a *source distribution* should be created.

```bash
python3 -m build --sdist
```

A *source distribution* is unbuilt *(it???s not a Built Distribution)* and requires a build step when installed by `pip`. Even if the distribution is pure Python *(contains no extensions)*, it still involves a build step to build out the installation metadata from `setup.py`.

### Wheels

We should also create a *wheel* for the project. A *wheel* is a built package that can be installed without needing to go through the build process. Installing *wheels* are substantially faster for the end-user compared to installing from a source distribution.

```bash
python3 -m build --wheel
```

The *wheel* package will detect that the code is pure Python and build a *wheel* that is named such that it is usable on any Python 3 installation.

## Uploading to PyPI

When we ran the command to create our distribution, a new directory `./dist` was created under the project???s root directory. That???s where we'll find our distribution file(s) to upload.

**NOTE:**

*These files are only created when we execute the command to create the distribution. This means that with **ANY** changes to the source files or configurations in `setup.py` file, the distribution files are needed to be rebuilt again before we can distribute the changes to PyPI.*

Before trying to upload the distribution, check to see if the *brief / long descriptions* provided in `setup.py` are valid. This can be done by running a `twine` check on package files:

```bash
pip install twine
```

```bash
twine check dist/*
```

When both the *source distribution* and *wheel* have `PASSED`, you are now ready to upload it.

```bash
twine upload dist/*

Uploading distributions to https://upload.pypi.org/legacy/
Enter your username: __token__
Enter your password: 
```

The *username* should be set to `__token__`.
The *password* should be set to the PyPI **API Token**.

---

## Contribute

Community contributions are encouraged! Feel free to report bugs and feature requests to the [issue tracker](https://github.com/kakaiba-talaga/pyDataStore/issues) provided by *GitHub*.

## License

`pyDataStore` is an Open-Source Software *(OSS)* and is available for use under the [GNU GPL v3](https://github.com/kakaiba-talaga/pyDataStore/blob/main/LICENSE) license.
