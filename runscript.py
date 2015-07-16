import sys
import unittest
import inspect
from module.cliparser import build_parser
from module.buildcap import build_capabilities
from selenium import webdriver

parser = build_parser('RWD client for running a script');
parser.add_argument('--path', required=True)
args = parser.parse_args()

desired_capabilities = build_capabilities(args)
desired_capabilities['name'] = 'Script: %s' % args.path

print("Connecting to RWD server: " + args.server_url)
driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=args.server_url)

# reset args list to have a pristine environment
sys.argv = ['test'];

# script should not consider itself as main
globalScope = globals().copy();
globalScope['__name__'] = 'script';

localScope = {driver: driver}
execfile(args.path, globalScope, localScope);

# automatically load all test classes
testSuite = unittest.TestSuite()
for item in localScope.itervalues():
    if (inspect.isclass(item) and issubclass(item, unittest.TestCase)):
        testSuite.addTest(unittest.TestLoader().loadTestsFromTestCase(item))

# If a suite was defined, run it
if (testSuite.countTestCases() > 0):
    unittest.TextTestRunner(verbosity=2).run(testSuite)

# quit but don't report errors. The browser might be already closed.
try:
    driver.quit()
except Exception, e:
    pass
