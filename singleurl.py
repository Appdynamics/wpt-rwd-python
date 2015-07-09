import argparse
import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_chrome_caps(browser_args):
    chrome_options = Options()
    if browser_args:
        for arg in browser_args:
            chrome_options.add_argument("--" + arg)
    return chrome_options.to_capabilities()
    
def get_firefox_caps(profile_dir):
    raise NotYetImplemented()

parser = argparse.ArgumentParser(description='RWD client for single URL measurements')

parser.add_argument('--server-url', required=True)
parser.add_argument('--test-url', required=True)
parser.add_argument('--browser', choices=['chrome', 'firefox', 'ie'], required=True)
parser.add_argument('--screenshot', default='screenshot.png')
parser.add_argument('--firefox-profile-dir')
parser.add_argument('browser_args', nargs='*')

args = parser.parse_args()

browser = args.browser.lower()

desired_capabilities = None
if browser == "chrome":
    desired_capabilities = get_chrome_caps(args.browser_args)
elif browser == "firefox":
    desired_capabilities = get_firefox_caps(args.firefox_profile_dir)
else:
    raise UnSupportedBrowser(browser);

desired_capabilities['name'] = 'Single URL snapshot: %s' % args.test_url
desired_capabilities['lockStep'] = "true"

print("Connecting to RWD server: " + args.server_url)
driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=args.server_url)

driver.implicitly_wait(10)

print("Requesting URL: " + args.test_url)
driver.get(args.test_url)

print("Done.")
driver.quit()
