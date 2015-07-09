# Python RWD clients for Webpagetest

This repository contains remote webdriver clients written in python and
designed to be used in the remote webdriver enabled version of webpagetest

## Requirements
Install python dependencies (may require sudo)
```sh
pip install --no-cache-dir -r requirements.txt
```

## Capabilities
The following RWD capabilities are left unspecified on purpose, the RWD server
on the WPT agent node chooses the appropriate value
- platform (OS platform)
- version (Browser version)

Other capabilities (resolution, proxy, ...) may need to be supported in the future

## singleur.py
Fetch a single URL snapshot, i.e. single measurement.

Usage:
```sh
python singleurl.py --server-url http://user:pass@provider.com:port -b chrome --browser chrome --test-url http://appdynamics.com
```

# Copyright
Copyright (c) AppDynamics, Inc, and its affiliates  
2015  
All rights reserved.
