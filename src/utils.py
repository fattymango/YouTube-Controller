import time

from .keys import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utils:

    '''
        Utility Class as a lower layer for The Remote class,
            contains all the functionalities that operates 
                on Selenium driver.                         

                                                                '''



    def __init__(self,driver : webdriver) -> None:

        self.__driver = driver
        self.action = ActionChains(self.__driver)

    def execute_action(self,action):

        '''
            Function perform all the basic command using its 
                shortcut, such as (play (K), Mute (M)...etc)
                                                                '''
                                                                
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.ID, PLAYER_CONTAINER))
            )
        except Exception:
            print(Exception)
            return False
            
        self.action.send_keys(action)
        self.action.perform()

    def set_quality (self,quality):
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.ID, PLAYER_CONTAINER))
            )
            self.__driver.execute_script(SETTINGS)

            try:
                WebDriverWait(self.__driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, SETTINGS_CONTAINER))
                )
                self.__driver.execute_script(QUALITY)
                time.sleep(.3)
                self.__driver.execute_script(quality)    
            except Exception:
                print(Exception)
            
        except Exception:
            print(Exception)
            return False
        
        

    def search(self,q):
        try:
            search = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.XPATH, SEARCH))
            )
            time.sleep(.1)
            search.clear()
            search.send_keys(str(q))
            search.send_keys(Keys.RETURN)

        except Exception:
            print(Exception)
            return False
        

    def select_video(self,index):
        try:
            # Locate videos container
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.XPATH, VIDEOS_CONTAINER))
            )
            time.sleep(2)
            #Locate the video and click it
            search =self.__driver.find_element_by_xpath(VIDEO_CHOICE)
            x = search.find_elements_by_tag_name(VIDEO_PLAYER)
            x[index].click()
        except Exception:
            print(Exception)
            return False