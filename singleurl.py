import argparse
import os
import sys
from selenium import webdriver

assert os.environ.has_key('RWD_URL')
assert os.environ.has_key('RWD_PORT')
assert os.environ.has_key('RWD_USERNAME')
assert os.environ.has_key('RWD_ACCESSKEY')

parser = argparse.ArgumentParser(description='RWD client for single URL measurements')
parser.add_argument('url')
parser.add_argument('-b', '--browser', choices=['chrome', 'firefox', 'ie'], required=True)
parser.add_argument('-s', '--screenshot', default='screenshot.png')

args = parser.parse_args()

command_executor = os.environ['RWD_URL'] % (os.environ['RWD_USERNAME'],
        os.environ['RWD_ACCESSKEY'], os.environ['RWD_PORT'])

desired_capabilities = {
    'name': 'Single URL snapshot: %s' % args.url,
    'browserName': args.browser,
}

print "Connecting to RWD server: " + command_executor;
driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=command_executor)
driver.implicitly_wait(10)

print "Requesting URL: " + args.url
driver.get(args.url)
print "Done."
driver.quit()
