# pylint: disable=C0103,missing-docstring
import sys
import datetime
import pathlib
import argparse
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

parser = argparse.ArgumentParser()
parser.add_argument("daysStart", help="Number of days previous to today", type=int)
parser.add_argument("daysEnd", help="Number of days previous to dayStart", type=int)
parser.parse_args()

def get_image(imagedate):
    """ getImage function """
    opts = Options()
    opts.headless = True
    assert opts.headless
    browser = Chrome(options=opts)
    browser.set_window_size(2880,1800)
    url = "https://covid19map.yesexactly.com/index_death.php?date={0}".format(imagedate)
    browser.get(url)
    try:
        WebDriverWait(browser, 30).until(EC.visibility_of_element_located((By.ID, "maploaded")))
    finally:
        browser.save_screenshot("screenshots/%s.png" % imagedate)
        browser.quit()

def main():
    """ main function """
    dayStart = int(sys.argv[1])
    dayEnd = int(sys.argv[2])
    for days in range (dayStart, dayEnd):
        image_range = datetime.datetime.now() - datetime.timedelta(days)
        image_name = image_range.strftime("%Y-%m-%d")
        filepath = pathlib.Path('screenshots/%s.png' % image_name)
        if filepath.exists():
            print("%s exists" % filepath)
        else:
            get_image(image_name)
            print("Downloaded %s" % image_name)
    print("Finished!")

if __name__ == "__main__":
    main()
