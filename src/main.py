import os
from .remote import Remote
from .keys import SEARCH_STATE
class Operater:
    def __init__(self,driver) -> None:
        self.driver = driver
        self.remote = Remote(driver)
        
        ''' 
            Switch Cases 
                            '''
                                    
        self.__SEARCH_COMMANDS={
            1:self.remote.select_video,
            2:self.remote.search
            }

        self.__PLAYING_COMMANDS={
            1:self.remote.toggle_play,
            2:self.remote.toggle_caption,
            3:self.remote.toggle_fullscreen,
            4:self.remote.toggle_mute,
            5:self.remote.forward_10s,
            6:self.remote.backward_10s,
            7:self.remote.set_quality,
            8:self.remote.search,
            9:self.remote.refresh
            }
        self.states ={

            0: [self.serach_commands,self.__SEARCH_COMMANDS],
            1: [self.playing_video_commands,self.__PLAYING_COMMANDS]
        }

        self.STATE = SEARCH_STATE


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

    
    def clear(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def operate(self):
    
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