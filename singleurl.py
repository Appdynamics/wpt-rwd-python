from module.cliparser import build_parser
from module.buildcap import build_capabilities
from selenium import webdriver

parser = build_parser('RWD client for single URL measurements');
parser.add_argument('--test-url', required=True)
args = parser.parse_args()

desired_capabilities = build_capabilities(args)
desired_capabilities['name'] = 'Single URL snapshot: %s' % args.test_url

print("Connecting to RWD server: " + args.server_url)
driver = webdriver.Remote(desired_capabilities=desired_capabilities,
                          command_executor=args.server_url)

driver.implicitly_wait(10)

print("Requesting URL: " + args.test_url)
driver.get(args.test_url)

driver.quit()
print("Done.")
