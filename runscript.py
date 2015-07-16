import sys
import unittest
import inspect
from module.cliparser import build_parser
from module.buildcap import build_capabilities
from selenium import webdriver

# exit codes
ERROR = 3
UNSTABLE = 2
FAILED = 1
PASSED = 0
ret = PASSED

parser = build_parser('RWD client for running a script');
parser.add_argument('--path', required=True)
args = parser.parse_args()

desired_capabilities = build_capabilities(args)
desired_capabilities['name'] = 'Script: %s' % args.path

print("Connecting to RWD server: " + args.server_url)
driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=args.server_url)

# reset args list to have a pristine environment to execute the script
sys.argv = ['test'];

# script should not consider itself as main
globalScope = globals().copy();
globalScope['__name__'] = 'script';

localScope = {driver: driver}

try:
    execfile(args.path, globalScope, localScope);
except Exception as e:
    print str(e)
    if (isinstance(e, AssertionError)):
        # assertion = script failed
        ret = FAILED
    else:
        ret = ERROR

# automatically load all test classes to feed in test runner
testSuite = unittest.TestSuite()
for item in localScope.itervalues():
    if (inspect.isclass(item) and issubclass(item, unittest.TestCase)):
        testSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(item))

# If a suite was defined, run it
if (testSuite.countTestCases() > 0):
    testRunner = unittest.TextTestRunner(verbosity=2)
    results = testRunner.run(testSuite)
    if len(results.failures) > 0:
        ret = FAILED
    elif len(results.errors) > 0:
        ret = ERROR

# quit but don't report errors. The browser might be already closed.
try:
    driver.quit()
except Exception, e:
    pass

exit(ret)
