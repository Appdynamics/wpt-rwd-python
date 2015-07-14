from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def get_chrome_caps(browser_args):
    chrome_options = Options()
    if browser_args:
        for arg in browser_args:
            chrome_options.add_argument("--" + arg)
    return chrome_options.to_capabilities()

def get_firefox_caps(profile_dir):
    firefox_capabilities = DesiredCapabilities.FIREFOX.copy()
    if (profile_dir):
        firefox_capabilities['firefox_profile_dir'] = profile_dir
    return firefox_capabilities

def get_internetexplorer_caps():
    return DesiredCapabilities.INTERNETEXPLORER.copy()

def build_capabilities(args):
    desired_capabilities = None
    browser = args.browser

    if browser == "chrome":
        desired_capabilities = get_chrome_caps(args.browser_args)
    elif browser == "firefox":
        desired_capabilities = get_firefox_caps(args.firefox_profile_dir)
    elif browser in ie_browsers:
        desired_capabilities = get_internetexplorer_caps()
        desired_capabilities['initialBrowserUrl'] = 'about:blank'
    else:
        raise UnSupportedBrowser(browser);

    desired_capabilities['wptLockStep'] = "true"

    return desired_capabilities;

