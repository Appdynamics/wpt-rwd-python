import sys
import unittest
import xmlrunner
import inspect
from module.cliparser import parse
from module.buildcap import build_capabilities
from selenium import webdriver

# exit codes
SCRIPT_ERROR = 3
TEST_UNSTABLE = 2
TEST_FAILED = 1
TEST_PASSED = 0
ret = TEST_PASSED

args = parse()

desired_capabilities = build_capabilities(args)

print("Connecting to RWD server: " + args.server_url)
driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=args.server_url)


# with lock step, 'get' can take more time then a usual RWD call.
# Setting page load timeout to a negative value will wait forever for the page to
# load without throwing an exception
driver.set_page_load_timeout(-1);

driver.implicitly_wait(10)

if args.test_url:
    print('[%(id)s] Single URL measurement on %(url)s' % { 'id': args.id, 'url': args.test_url});
    r = driver.get(args.test_url)
else:
    print('[%s] Running a script' % args.id)

    # reset args list to have a pristine environment to execute the script
    sys.argv = ['test'];

    testSuite = unittest.TestSuite()
    scriptScope = {'driver': driver, 'testSuite': testSuite}

    try:
        execfile(args.filepath, scriptScope, scriptScope);
    except Exception as e:
        print str(e)
        if (isinstance(e, AssertionError)):
            # assertion = script failed
            ret = TEST_FAILED
        else:
            ret = SCRIPT_ERROR

    # automatically load all test classes to feed in test runner
    for item in scriptScope.itervalues():
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
