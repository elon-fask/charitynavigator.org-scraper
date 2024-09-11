import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


import pandas as pd
import logging.config
import time
import json

logging.config.dictConfig({
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [PID %(process)d] [Thread %(thread)d] [%(levelname)s] [%(name)s] %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "default",
            "stream": "ext://sys.stdout"
        }
    },
    "root": {
        "level": "INFO",
        "handlers": [
            "console"
        ]
    }
})

LOGGER = logging.getLogger()


def run():

    URL = "https://www.charitynavigator.org/discover-charities/a-to-z-directory/"

    LOGGER.info("launching chrome web browser")
    driver.get(URL)
    time.sleep(100)

if __name__ == '__main__':
    
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--driver-type", default="chrome", choices=("chrome", "firefox"))
    # parser.add_argument("--webdriver-path", required=False, default=None)
    # parser.add_argument("--dont-quit", action="store_true")  
    # parser.add_argument("--headless", action="store_true")
    # args = parser.parse_args()
        
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options, 
                              #executable_path="/home/atora/github/upwork_bot/script/bin/chromedriver_linux"
                              )
    driver.set_window_size(1900, 1000)
    action_chains = ActionChains(driver)

    print("running script !")
    run()
    print("done")


