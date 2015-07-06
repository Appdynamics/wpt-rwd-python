# Python RWD clients for Webpagetest

This repository contains remote webdriver clients writtent in python and
designed to be used in the remote webdriver enabled version of webpagetest

## Requirements
Install python dependencies (may require sudo)
```sh
pip install --no-cache-dir -r requirements.txt
```

Set environment variables with connection parameters to the RWD server
```sh
# Example with Sauce Labs
export RWD_URL="http://%s:%s@ondemand.saucelabs.com:%s/wd/hub"
export RWD_PORT=80
export RWD_USERNAME=YOUR_USERNAME
export RWD_ACCESSKEY=YOUR_ACCESSKEY
```

## Capabilities
The following RWD capabilities are left unspecified on purpose, the RWD server
on the WPT agent node chooses the appropriate value
- platform (OS platform)
- version (Browser version)

Other capabilities (resolution, proxy, ...) may need to be supported in the future

## singleur.py
Fetch a single URL snapshot, i.e. single measurement, on the AppDynamics Synthetic Monitoring Platform

Usage:
```sh
python singleurl.py -b chrome -s /path/to/screenshot.png http://ibm.com
```

# Copyright
Copyright (c) 2015 AppDynamics Inc.
