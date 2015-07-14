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

execfile(args.path, globals(), {driver: driver});

try:
    driver.quit()
except Exception, e:
    pass
