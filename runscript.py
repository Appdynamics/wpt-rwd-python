import sys
import unittest
import xmlrunner
import inspect
from module.cliparser import build_parser
from module.buildcap import build_capabilities
from selenium import webdriver

# exit codes
SCRIPT_ERROR = 3
TEST_UNSTABLE = 2
TEST_FAILED = 1
TEST_PASSED = 0
ret = TEST_PASSED

parser = build_parser('RWD client for running a script');

# path where the user script is located
parser.add_argument('--path', required=True)

args = parser.parse_args()

desired_capabilities = build_capabilities(args)
desired_capabilities['name'] = 'Script: %s' % args.path

print("Connecting to RWD server: " + args.server_url)
driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=args.server_url)

# reset args list to have a pristine environment to execute the script
sys.argv = ['test'];

# For Unit Tests: script should not consider itself as main in order to prevent 
# the provided script to run the testrunner by itself.
globalScope = globals().copy();
globalScope['__name__'] = 'script';

localScope = {'driver': driver}

# with lock step, 'get' can take more time then a usual RWD call.
# Setting page load timeout to a negative value will wait forever for the page to
# load without throwing an exception
driver.set_page_load_timeout(-1);

try:
    execfile(args.path, globalScope, localScope);
except Exception as e:
    print str(e)
    if (isinstance(e, AssertionError)):
        # assertion = script failed
        ret = TEST_FAILED
    else:
        ret = SCRIPT_ERROR

# automatically load all test classes to feed in test runner
testSuite = unittest.TestSuite()
for item in localScope.itervalues():
    if (inspect.isclass(item) and issubclass(item, unittest.TestCase)):
        testSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(item))

# If a suite was defined, run it
if (testSuite.countTestCases() > 0):
    testRunner = xmlrunner.XMLTestRunner(verbosity=2, output='reports')

    results = testRunner.run(testSuite)
    if len(results.failures) > 0:
        ret = TEST_FAILED
    elif len(results.errors) > 0:
        ret = SCRIPT_ERROR

# quit but don't report errors. The browser might be already closed.
try:
    driver.quit()
except Exception, e:
    pass

exit(ret)
