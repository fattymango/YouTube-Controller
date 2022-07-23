
import time

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from .remote import Remote
from .keys import *



class YoutubeController:
    '''
                                            
        A class that implements Selenium driver and setup
            YouTube on it.                                    
                                                            '''
    def __init__(self,url) -> None:
        self.__driver = self.__setup()
        self.remote = Remote(self.__driver)
        self.__url = url
        self.__load_page()
        self.__driver.set_window_position(0,0)
        self.__driver.maximize_window()

    def __setup(self):
        '''
            For Automatic driver installation use this
            
                PATH = ChromeDriverManager().install()
                                                         '''
        
        '''
            For Manual driver installation provide 
                the exact location of the driver
                                                         '''
        
        chrome_options = Options()
        chrome_options.add_argument('load-extension=' + EXTENSION)
        
        driver =webdriver.Chrome(executable_path= DRIVER,chrome_options=chrome_options)
        
        # driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
        driver.create_options()
        driver.set_window_position(-10000,0)
        
        return driver
    
    def __load_page(self):

        time.sleep(3)
        if len(self.__driver.window_handles) ==2 :
            print("i have two tabs")
            self.__driver.switch_to.window(self.__driver.window_handles[1])
            self.__driver.close()
        else : print("i have one tab")
        self.__driver.switch_to.window(self.__driver.window_handles[0])
        self.__driver.get(self.__url)
        time.sleep(.1)
        
    def get_driver(self):
        self.__driver.find_element_by_id
        return self.__driver
    
    def test(self):
        
        while True:
            x = input("bla bla")
            if x :
                print(self.__driver.current_url.split('/')[3][0])
