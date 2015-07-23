import argparse

def parse():
    parser = argparse.ArgumentParser('RWD client')

    ie_browsers = [ 'ie 10', 'ie 11' ]
    browsers =  ['chrome', 'firefox', 'internet explorer'] + ie_browsers

    # run id, optional
    parser.add_argument('--id')
    parser.add_argument('--server-url', required=True)
    parser.add_argument('--browser', choices=browsers, required=True)
    parser.add_argument('--screenshot', default='screenshot.png')
    parser.add_argument('--firefox-profile-dir')
    parser.add_argument('browser_args', nargs='*')

    group = parser.add_mutually_exclusive_group(required=True)
    # path where the user script is located
    group.add_argument('--filepath')
    # or URL to load for RWD client for single URL measurements
    group.add_argument('--test-url')

    return parser.parse_args()
