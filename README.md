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

## runscript.py
Execute a python selenium script passed as an argument. The script will have
the `driver` object in it's local scope.

A script can be a free form python script like:
```python
driver.get('http://appdynamics.com')
driver.quit();
```

Or one or more TestCase classes (from unittest). In this case, runscript will act as a
test runner and will output a verbose text result on the stdout and generate an
XML report (JUnit) per TestCase in `./reports`. A typical TestCase would look
like:

```python
import unittest

class TestStringMethods(unittest.TestCase):
  def setUp(self):
      # do the Selenium navigation here
      driver.get('http://appdynamics.com')

  def test_banner_on_page(self):
      self.assertTrue(driver... )

  def test_check_data(self):
      # more tests
      pass

if __name__ == '__main__':
    unittest.main()
```

Usage:
```sh
python runscript.py --server-url http://user:pass@provider.com:port -b chrome --browser chrome --path ~/tmp/my_script.py
```

# Copyright
Copyright (c) AppDynamics, Inc, and its affiliates
2015
All rights reserved.
