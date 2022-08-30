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
        Utility Class acts as a lower layer for The Remote class,
            contains all the functionalities that operates 
                on Selenium driver.                         

                                                                '''



    def __init__(self,driver : webdriver) -> None:

        self.__driver = driver
        self.action = ActionChains(self.__driver)

    def get_status(self):
        payload = {}
        try:
            play = self.__driver.find_element_by_css_selector(SELECTORS["PLAY"]).get_attribute("title")
            mute = self.__driver.find_element_by_css_selector(SELECTORS["MUTE"]).get_attribute("title")
            ctime = self.__driver.find_element_by_css_selector(SELECTORS["CURRENT_TIME"]).text
            ftime = self.__driver.find_element_by_css_selector(SELECTORS["FULL_TIME"]).text
            u2play = self.__driver.find_element_by_css_selector(SELECTORS["AUTO_PLAY"]).get_attribute("aria-checked")
            
            play = True if play == "Pause (k)" else False
            mute = True if mute == "Unmute (m)" else False
            u2play = True if u2play == "true" else False
            payload = {
                "Playing" : play,
                "Muted" : mute,
                "AUTO_PALY": u2play,
                "Current_time" : ctime,
                "Full_time": ftime

            }
     
        except Exception as e:
            print(e)
        return payload

    def execute_action(self,action,shift = False):

        '''
            Function performs all the basic command using its 
                shortcut, such as (play (K), Mute (M)...etc)
                                                                '''
                                                                
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.ID, TAGS["PLAYER_CONTAINER"]))
            )
            if shift:
                self.action.send_keys(Keys.SHIFT+action)
            else :
                self.action.send_keys(action)

            self.action.perform()
            return self.get_status()
        except Exception:
            print(Exception)
            return False
            
    def like_video(self):
        try:
            button = WebDriverWait(self.__driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS["LIKE_BUTTON"]))
            )
            
            button.click()
            return True
        except: return False

    def dislike_video(self):
        try:
            button = WebDriverWait(self.__driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS["DISLIKE_BUTTON"]))
            )
            
            button.click()
            return True
        except: return False

    def subscribe(self):
        try:
            button = WebDriverWait(self.__driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, SELECTORS["SUBSCRIBE"]))
            )
            
            button.click()
            return True
        except: return False    
    def set_quality (self,quality):
        try:
            WebDriverWait(self.__driver, 5).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, SELECTORS["OPTIONS_BUTTON"]))
            )
            self.__driver.execute_script(SCRIPTS["SETTINGS"])
        
            self.__driver.execute_script(SCRIPTS["QUALITY"])
            time.sleep(.3)
            
            self.__driver.execute_script(quality)
            return True    
            
        except Exception:
                print("im the problem")
                return False    

        
        

    def search(self,q):
        try:
            search = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.XPATH, XPATHS["SEARCH"]))
            )
            time.sleep(.1)
            search.clear()
            search.send_keys(str(q))
            search.send_keys(Keys.RETURN)
            return True
        except Exception:
            print(Exception)
            return False
        
    def __click_search_result_video(self,index):
        try : 
            container = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.XPATH, XPATHS["VIDEOS_CONTAINER"]))
            )
            time.sleep(2)
            container.find_elements_by_tag_name(TAGS["VIDEO_PLAYER"])[index].find_element_by_css_selector('#video-title > yt-formatted-string').click()
            return True
        except Exception:
            return False
    
    def __click_recommended_video(self,index):
        try:
            container =  WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME,'ytd-watch-next-secondary-results-renderer'))
                )
            container.find_elements_by_tag_name('ytd-compact-video-renderer')[index].click()
            return True
        except Exception:
            return False

    def __click_home_video(self,index):
        try:
            WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME,'ytd-rich-grid-row'))
                )
            containers = self.__driver.find_elements_by_tag_name('ytd-rich-grid-row')
            containers[0].find_elements_by_tag_name('ytd-rich-item-renderer')[index].click()
            return True
        except Exception:
            return False
    

    def select_video(self,state,index):
        try:
            {
                'HOME'  :  self.__click_home_video,
                'SEARCH':  self.__click_search_result_video,
                'WATCH' :  self.__click_recommended_video

             }[state](index)
            
        except Exception:
            
            return False
    
    def get_home_videos(self):
        payload = []
        try:
            self.action.send_keys(Keys.PAGE_DOWN).send_keys(Keys.PAGE_UP)
            containers=WebDriverWait(self.__driver, 10).until(
                 EC.presence_of_all_elements_located((By.TAG_NAME,'ytd-rich-grid-row'))
                )
            
            for i in range(2):
                container = containers[i].find_elements_by_tag_name('ytd-rich-item-renderer')
                
                for video in container:
                    
                    x = video.text.split('\n')
                    
                    payload.append({

                    'duration' : x[0],
                    'title' : x[1],
                    'channel' : x[2],
                    'views' : x[3],
                    'date' : x[4]     

                    })
            
            
        except Exception:
            print(Exception)
        return payload
    
    def get_recommended_videos(self):
        payload = []
        videos = self.__driver.find_element_by_tag_name('ytd-watch-next-secondary-results-renderer').find_elements_by_tag_name('ytd-compact-video-renderer')
        
        for i in range(0,5):
            x = videos[i].text.split('\n')
            payload.append({

             'duration' : x[0],
             'title' : x[1],
             'channel' : x[2],
             'views' : x[3],
             'date' : x[4]   

            })
        
        return payload
    