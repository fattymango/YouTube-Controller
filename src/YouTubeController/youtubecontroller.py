import time
import pathlib
import psutil
import os
import requests
import subprocess


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager




from .keys import *



class YoutubeController:
    '''
                                            
        A class that implements Selenium driver and setup
            YouTube on it.                                    
                                                            '''
    def __init__(self,url,testing:bool=False) -> None:
        self.__url = url
        self.__driver = self.__setup(testing)
        self.__load_page()
        self.__driver.set_window_position(0,0)
        self.__driver.maximize_window()
        self.__driver.fullscreen_window()
    def __setup(self,testing=False):
        
        if testing:
            options = webdriver.ChromeOptions()
            options.add_argument('load-extension=' + str(pathlib.Path().resolve()).replace('\\','\\\\')+EXTENSION)
            options.add_argument('--ignore-ssl-errors=yes')
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Remote(options=options)
        else : 
            if self.__check_instance_running():
                
                if not self.__check_instance_port():
                    subprocess.call("TASKKILL /F /IM chrome.exe", shell=False)
                    self.__create_new_instance()
            chrome_options = Options()
            chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            
            driver = webdriver.Chrome(ChromeDriverManager(print_first_line=False).install(),options=chrome_options,)
            
            
        
        return driver
    
    def __check_instance_port(self):
        try:
            requests.get("http://127.0.0.1:9222/")
            return True
        except:
            return False

    def __check_instance_running(self):
        return "chrome.exe" in (i.name() for i in psutil.process_iter())
        
    def __create_new_instance(self):
       os.system('start chrome.exe --remote-debugging-port=9222')
    def __load_page(self):
        self.__driver.switch_to.new_window('window')
        self.__driver.maximize_window()
        self.__driver.set_window_position(-10000,0)
        self.__driver.get("https://www.youtube.com/")
        self.__driver.get(self.__url)
        time.sleep(.1)
        
    def get_driver(self):
        return self.__driver
    


        
        

    def initialize_driver (self):
        self.__driver = self.__setup(False)
        self.__load_page()
        self.__driver.set_window_position(0,0)
        self.__driver.maximize_window()
    
    def close_driver(self):
        self.__driver.close()
        self.__driver.quit()
        self.__driver = None