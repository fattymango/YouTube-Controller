import os
from .remote import Remote

class Operator:
    def __init__(self,driver) -> None:
        self.driver = driver
        self.remote = Remote(driver)
        ''' 
                    Switch Cases 
                                            '''
                        
        self.__COMMANDS={

        1   :   self.remote.toggle_play,
        2   :   self.remote.toggle_caption,
        3   :   self.remote.toggle_fullscreen,
        4   :   self.remote.toggle_mute,
        5   :   self.remote.forward_10s,
        6   :   self.remote.backward_10s,
        7   :   self.remote.set_quality,
        8   :   self.remote.search,
        9   :   self.remote.select_video,
        10  :   self.remote.get_recommendations,
        11  :   self.remote.refresh,
        }
    
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
        self.remote.__del__()

        