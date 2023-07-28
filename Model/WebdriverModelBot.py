from selenium import webdriver
from selenium_stealth import stealth
from time import sleep


class Navegador:
    def __init__(self, userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36", headless = False):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_extension("./Extensoes/cp.zip")

        if headless == True:
            chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.set_window_size(500, 950)
        self.driver.set_page_load_timeout(8)
        sleep(1)

        stealth(
            self.driver,
            user_agent=userAgent,
            languages=["pt-BR", "pt"],
            vendor="Amazon Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )