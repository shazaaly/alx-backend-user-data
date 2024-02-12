#!/usr/bin/env python3

import base64

binary_data = b'Hello World!\n'
print(binary_data)

encoded = base64.b64encode(binary_data)
print(encoded)