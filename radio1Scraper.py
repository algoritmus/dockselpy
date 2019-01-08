import os
import logging

from pyvirtualdisplay import Display
from selenium import webdriver

logging.getLogger().setLevel(logging.INFO)

BASE_URL = 'http://www.example.com/'


def chrome_example():
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info('Initialized virtual display..')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')

    chrome_options.add_experimental_option('prefs', {
        'download.default_directory': os.getcwd(),
        'download.prompt_for_download': False,
    })
    logging.info('Prepared chrome options..')

    browser = webdriver.Chrome(chrome_options=chrome_options)
    logging.info('Initialized chrome browser..')

    browser.get(BASE_URL)
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    browser.quit()
    display.stop()


def firefox_example():
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info('Initialized virtual display..')

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('browser.download.folderList', 2)
    firefox_profile.set_preference('browser.download.manager.showWhenStarting', False)
    firefox_profile.set_preference('browser.download.dir', os.getcwd())
    firefox_profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')

    logging.info('Prepared firefox profile..')

    browser = webdriver.Firefox(firefox_profile=firefox_profile)
    logging.info('Initialized firefox browser..')

    browser.get(BASE_URL)
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)
    
    getTrackInfo(browser)
    
    browser.quit()
    display.stop()


def phantomjs_example():
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info('Initialized virtual display..')

    browser = webdriver.PhantomJS()
    logging.info('Initialized phantomjs browser..')

    browser.get(BASE_URL)
    logging.info('Accessed %s ..', BASE_URL)

    logging.info('Page title: %s', browser.title)

    browser.quit()
    display.stop()

def getTrackInfos(browser):
    tracks = browser.find_elements_by_class_name('track')
    
    for track in tracks:
        trackInfo = track.find_element_by_class_name('track-info')
        author = trackInfo.find_element_by_class_name('author').text
        title = trackInfo.find_element_by_class_name('title').text
        
        trackTime = track.find_element_by_class_name('track-time')
        tt = trackTime.find_element_by_tag_name('span').text
        logging.info('TrackInfo: %s-%s,%s',author,title,tt)
    
    


if __name__ == '__main__':
    chrome_example()
    #firefox_example()
    #phantomjs_example()
