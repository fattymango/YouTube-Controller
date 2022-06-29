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
                            
        self.__SEARCH_COMMANDS={
            1:self.select_video,
            2:self.search}

        self.__PLAYING_COMMANDS={
        1:self.toggle_play,
        2:self.toggle_caption,
        3:self.toggle_fullscreen,
        4:self.toggle_mute,
        5:self.forward_10s,
        6:self.backward_10s,
        7:self.set_quality,
        8:self.search,
        9:self.refresh}
        self.STATE = SEARCH_STATE
        self.states ={
            0: [self.serach_commands,self.__SEARCH_COMMANDS],
            1: [self.playing_video_commands,self.__PLAYING_COMMANDS]}
    
    def toggle_play (self):
        self.utils.execute_action(TOGGLE_PLAY)
    def toggle_caption (self):
        self.utils.execute_action(TOGGLE_CAPTION)   
    def toggle_fullscreen (self):
        self.utils.execute_action(TOGGLE_FULLSCREEN)   
    def toggle_mute (self):
        self.utils.execute_action(TOGGLE_MUTE)
    def forward_10s (self,iter=1):
        for i in range(0,iter):
            self.utils.execute_action(FORWARD)
    def backward_10s(self,iter=1):
        for i in range(0,iter):
            self.utils.execute_action(BACKWARD)
    
    def set_quality(self):
        Q = {
            1:HIGHEST,
            2:LOWEST,
            3:AUTO
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

    def select_video(self):
        
        while True:
            index = int(input (' Enter the video\'s index.[1..n]\n'))
            if index-1 in range(0,5):
                self.utils.select_video(index-1)
                break
        self.STATE = PLAYING_STATE
        


    def playing_video_commands (self):
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
             '9. Refresh\n'
        )

        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        return len(self.__PLAYING_COMMANDS)
    
    def serach_commands(self):
        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''\n")

        print(
             '........... ENTER THE COMMAND NUMBER ...........\n\n'+
             '1. Select Video\n'+
             '2. Search\n'
        )

        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''\n")
        return len(self.__SEARCH_COMMANDS)

    

        

    def main(self):
        inp = ""
        l = self.states[self.STATE][0]()
        while str(inp).capitalize() != 'Q' :
            
            while True:
                inp = int(input())
                if inp in range(1,l+1):
                    self.states[self.STATE][1][inp]()
                    break
            self.clear()
            l = self.states[self.STATE][0]()        



    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')
    def __del__(self):
        self.__driver.quit()