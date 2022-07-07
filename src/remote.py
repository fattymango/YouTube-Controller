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

        ''' 
                    Switch Cases 
                                            '''
                        
        self.__COMMANDS={

        1   :   self.toggle_play,
        2   :   self.toggle_caption,
        3   :   self.toggle_fullscreen,
        4   :   self.toggle_mute,
        5   :   self.forward_10s,
        6   :   self.backward_10s,
        7   :   self.set_quality,
        8   :   self.search,
        9   :   self.select_video,
        10  :   self.get_recommendations,
        11  :   self.refresh,
        }
       
    def toggle_play (self):
        print(self.utils.execute_action(BUTTONS["TOGGLE_PLAY"]))
    def toggle_caption (self):
        print(self.utils.execute_action(BUTTONS["TOGGLE_CAPTION"]))   
    def toggle_fullscreen (self):
        print(self.utils.execute_action(BUTTONS["TOGGLE_FULLSCREEN"]))
    def toggle_mute (self):
        print(self.utils.execute_action(BUTTONS["TOGGLE_MUTE"]))
    def forward_10s (self,iter=1):
        for _ in range(0,iter):
            print(self.utils.execute_action(BUTTONS["FORWARD"]))
    def backward_10s(self,iter=1):
        for _ in range(0,iter):
            print(self.utils.execute_action(BUTTONS["BACKWARD"]))
    
    def set_quality(self):
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
                break
        
    
    def refresh (self):
        self.__driver.refresh()

    def search(self):

        q = input (' Enter the search phrase.\n')
        self.utils.search(q)
        self.STATE = SEARCH_STATE

    def __get_current_window_state(self):
        url = self.__driver.current_url
        
        try:
            indicator = url.split('/')[3][0]
            state = "SEARCH" if indicator == "r" else "WATCH"
            
        except:
            state = "HOME"
        return state

    def select_video(self):
        
        while True:
            index = int(input (' Enter the video\'s index.[1..n]\n'))
            if index-1 in range(0,5):
                self.utils.select_video(self.__get_current_window_state(),index-1)
                break
        
        
    def get_recommendations(self):
        payload = self.utils.get_recommended_videos()
        for video in payload:
            print('\nVIDEO INFO\n'+
            video['title']+'\n'+
            video['channel']+'\n'+
            video['views']+'\nEND OF VIDEO INFO'
            )
        
        return payload

    def __commands_printer (self):

        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''\n")
        print(
             '........... ENTER THE COMMAND NUMBER ...........\n\n'+
             '1. Play / Pause\n'+
             '2. Caption\n'+
             '3. FullScreen / Minimize\n'+
             '4. Mute / UnMute\n'+
             '5. Forward 10 Seconds\n'+
             '6. backward 10 Seconds\n'+
             '7. Select Quality\n'+
             '8. Search\n'+
             '9. Select Video\n'+
             '10. Get Recommndations\n'+
             '11. Refresh\n'
        )
        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        return len(self.__COMMANDS)
    
    
    def main(self):
        inp = ""
        while str(inp).capitalize() != 'Q' :
            l = self.__commands_printer()
            while True:
                inp = int(input())
                if inp in range(1,l+1):
                    self.__COMMANDS[inp]()
                    break
            # self.clear()
                  
    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')
    def __del__(self):
        self.__driver.quit()
