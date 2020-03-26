from selenium import webdriver

def setGecko(executable_path, headless = False):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("permissions.default.desktop-notification", 2)
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    options.headless = headless
    driver = webdriver.Firefox(executable_path = executable_path, firefox_options = options, firefox_profile = fp)
    return driver
