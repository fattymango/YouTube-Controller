from selenium import webdriver

import os

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

    def get_status(self):
        return self.utils.get_status()    
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
    
    def set_quality(self):
        state = self.get_current_window_state()
        print(state)
        if not state == "WATCH":
            print("YOU CANT SET THE QUALITY WITHOUT A VIDEO OPENED.")
            return False
        Q = {
            1:SCRIPTS["HIGHEST"],
            2:SCRIPTS["LOWEST"],
            3:SCRIPTS["AUTO"]
        }
        while True:
            quality = int(input (

                'Choose Quality.\n'+
                '1. Highest.\n'+
                '2. Lowest.\n'+
                '3. Auto.\n'

            ))
            if quality in range(1,len(Q)+1):
                self.utils.set_quality(Q[quality])
                print(Q[quality])
                break
        
    
    def refresh (self):
        self.__driver.refresh()

    def search(self,q = None):
        if not q:
            q = input (' Enter the search phrase.\n')
        self.utils.search(q)
        

    

    def select_video(self,index = None):
        if not index : 
            while True:
                index = int(input (' Enter the video\'s index.[1..n]\n'))
                if index-1 in range(0,5):
                    break
        self.utils.select_video(self.get_current_window_state(),index-1)
        
        
    def get_recommendations(self):
        payload = self.utils.get_recommended_videos()
        for video in payload:
            print('\nVIDEO INFO\n'+
            video['title']+'\n'+
            video['channel']+'\n'+
            video['views']+'\nEND OF VIDEO INFO'
            )
        
        return payload
    def get_current_window_state(self):
        url = self.__driver.current_url
        
        try : 
            indicator = url.split('/')[3][0]
            if indicator == "r": state = "SEARCH"
            elif indicator == "w" : state = "WATCH"
        except : state = "HOME"
    
        
        return state
