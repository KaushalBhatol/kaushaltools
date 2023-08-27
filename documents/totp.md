# Time-Based One-Time Password (totp) Library

This library provides a class for generating and managing Time-Based One-Time Passwords (TOTP). It includes methods to generate TOTP keys, create 2FA URLs, display and save QR codes, scan QR codes, generate OTPs, and authenticate using OTPs.

## Installation

Install the library using the following command:

```bash
pip install kaushaltools
```

## Usage

Import the `totp` class from the library without creating instance:

```python
from kaushaltools import totp

totp.functions()
```

## Functions

Function                                                  | function
--------------------------------------------------------|-----------------
[Generating a TOTP Key](#generating-a-totp-key)         | `generate_key()`

## Generating a TOTP Key

* It's all upon you, Weather you want to give peramerters or not.
* Also you can decide which parameter you want to give.
* If parameters are not provided, It take default configration to genrate key.
* These function return key in String form.

### Parameters

variable            | type  | is null   | rule
--------------------|-------|-----------|---------
num_characters      | int   | True      | int > 31
prefix              | Str   | True      |
suffix              | Str   | True      |

### Return

* These function __return key in String__ formate.

### Usage

Code:

```python
from kaushaltools import totp

key = totp.generate_key(num_characters=32, prefix="first", suffix="Last")

print("Generated TOTP key:", key)
```

Output:

```bash
Generated TOTP key: FIRSTNAMU2VSDPEXWZRTT45HQYKILAST
```
