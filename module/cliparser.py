import argparse

def build_parser(desc):
    parser = argparse.ArgumentParser(description=desc)

    ie_browsers = [ 'ie 10', 'ie 11' ]
    browsers =  ['chrome', 'firefox', 'internet explorer'] + ie_browsers

    parser.add_argument('--server-url', required=True)
    parser.add_argument('--browser', choices=browsers, required=True)
    parser.add_argument('--screenshot', default='screenshot.png')
    parser.add_argument('--firefox-profile-dir')
    parser.add_argument('browser_args', nargs='*')

    return parser;
