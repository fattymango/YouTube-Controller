from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from YouTubeController.status import Status

from .keys import *
from .utils import Utils

class Remote:

    '''
        
        Remote Class that interact with the Selenium driver 
            and perform operations on it, using the utils
                class.
                                                            '''

    def __init__(self,driver : webdriver) -> None:
        self.__driver = driver
        self.utils = Utils(self.__driver)
        self.status = Status(self.__driver)

    def set_driver(self,driver):
        self.__driver = driver
        self.utils.set_driver(self.__driver)
        self.status.set_driver(self.__driver)
    def destroy_driver(self):
        self.__driver = None
        self.utils.destroy_driver()
        self.status.destroy_driver()
    def get_status(self,flag = True,wait = False,encode = True):
        return self.status.get_status(flag,wait,encode)
    def volume_up(self): 
        return self.utils.execute_action(Keys.ARROW_UP)
    def volume_down(self): 
        return self.utils.execute_action(Keys.ARROW_DOWN)
    def paly_back_speed_up(self):
        return self.utils.execute_action(SHIFTBUTTONS["PLAY_BACK_UP"],shift=True)
    def paly_back_speed_down(self):
        return self.utils.execute_action(SHIFTBUTTONS["PLAY_BACK_DOWN"],shift=True)
    def start_of_video(self):
        return self.utils.execute_action(Keys.HOME)   
    def end_of_video(self):
        return self.utils.execute_action(Keys.END)   
    def toggle_auto_play (self):
        return self.utils.toggle_auto_play()
    def toggle_play (self):
        return self.utils.execute_action(BUTTONS["TOGGLE_PLAY"])
    def toggle_caption (self):
        return self.utils.execute_action(BUTTONS["TOGGLE_CAPTION"])
    def toggle_fullscreen (self):
        return self.utils.execute_action(BUTTONS["TOGGLE_FULLSCREEN"])
    def toggle_mute (self):
        return self.utils.execute_action(BUTTONS["TOGGLE_MUTE"])
    def forward_10s (self,iter=1):
        for _ in range(0,iter):
            return self.utils.execute_action(BUTTONS["FORWARD"])
    def backward_10s(self,iter=1):
        for _ in range(0,iter):
            return self.utils.execute_action(BUTTONS["BACKWARD"])
    def playback_up(self,iter=1):
        for _ in range(0,iter):
            return self.utils.execute_action(BUTTONS["PLAYBACK_UP"])
    def playback_down(self,iter=1):
        for _ in range(0,iter):
            return self.utils.execute_action(BUTTONS["PLAYBACK_DOWN"])
    def go_to_url(self,url):
        return self.utils.go_to_url(url)
    def next_video(self):
        return self.utils.execute_action(SHIFTBUTTONS["NEXT_VIDEO"],shift=True)
    def prev_video(self):
        return self.utils.execute_action(SHIFTBUTTONS["PREV_VIDEO"],shift=True)
    def like_video(self):
        return self.utils.like_video()
    def dislike_video(self):
        return self.utils.dislike_video()
    def toggle_subscribe(self):
        return self.utils.toggle_subscribe()
    
    def set_quality(self,quality):
        
        while True:
            state = self.status.get_current_window_state()
            if state == "WATCH":
                Q = {
                    1:"HIGHEST",
                    2:"LOWEST",
                    3:"AUTO"
                }
                
                return self.utils.set_quality(Q[int(quality)])
            return False
                
        
    
    def refresh (self):
        self.__driver.refresh()

    def search(self,q = ' '):
        return self.utils.search(q)
        

    

    def select_video(self,index = None):
        if not index : 
            while True:
                index = int(input (' Enter the video\'s index.[1..n]\n'))
                if index-1 in range(0,5):
                    break
        self.utils.select_video(self.self.status.get_current_window_state(),int(index)-1)
        
        
    
        

    
        
        

