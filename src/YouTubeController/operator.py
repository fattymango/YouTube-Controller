import os

from .youtubecontroller import YoutubeController
from .remote import Remote
from network import Server


class Operator:

    def __init__(self, controller : YoutubeController) -> None:
        self.controller = controller
        self.remote = Remote(self.controller.get_driver())
        self.server = Server(self.remote)
        self.__COMMANDS = {
            0:   self.__keep_connection,
            1:   self.__keep_connection,
            3:   self.__destroy_driver,
            4:   self.__start_driver,

            11:  self.remote.toggle_play,
            12:  self.remote.toggle_caption,
            13:  self.remote.toggle_fullscreen,
            14:  self.remote.toggle_mute,
            15:  self.remote.forward_10s,
            16:  self.remote.backward_10s,
            17:  self.remote.refresh,
            18:  self.remote.playback_up,
            19:  self.remote.playback_down,
            20:  self.remote.next_video,
            21:  self.remote.prev_video,
            22:  self.remote.like_video,
            23:  self.remote.dislike_video,
            24:  self.remote.toggle_subscribe,
            25:  self.remote.start_of_video,
            26:  self.remote.end_of_video,
            27:  self.remote.toggle_auto_play,
            28:  self.remote.playback_up,
            29:  self.remote.playback_down,
            30:  self.remote.volume_up,
            31:  self.remote.volume_down,
            51:  self.remote.set_quality,
            52:  self.remote.select_video,
            53:  self.remote.go_to_url, 
            54:  self.remote.search
            
        }
        ''' 
                    Switch Cases 
                                            '''

    def __keep_connection(self):
        return True
    def __destroy_driver(self):
        self.controller.close_driver()
        self.remote.destroy_driver()

    def __start_driver(self):
        self.controller.initialize_driver()
        self.remote.set_driver(self.controller.get_driver())
    def __set_quality(self):
        while True:
            quality = int(
                input('Choose Quality.\n' + '1. Highest.\n' + '2. Lowest.\n' +
                      '3. Auto.\n'))
            if quality in range(1, 4):
                return self.remote.set_quality(quality)

   
                

    def __search(self):
        q = input(' Enter the search phrase.\n')
        return self.remote.search(q)

    def __commands_printer(self):

        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''\n")
        print('........... ENTER THE COMMAND NUMBER ...........\n\n' +
              '1. Play / Pause\n' + '2. Caption\n' +
              '3. FullScreen / Minimize\n' + '4. Mute / UnMute\n' +
              '5. Forward 10 Seconds\n' + '6. backward 10 Seconds\n' +
              '7. Select Quality\n' + '8. Search\n' + '9. Select Video\n' +
              '10. Get Recommndations\n' + '11. Refresh\n')
        print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
        return len(self.__COMMANDS)

    def main(self,debug = False):
        if not debug:
            for message,option in self.server.main():
                if int(message) > 50:
                    self.__COMMANDS[int(message)](option)
                else:
                    self.__COMMANDS[int(message)]()
                
            
        else:
            
            inp = ""
            while str(inp).capitalize() != 'Q' :
                l = self.__commands_printer()
                while True:

                    inp = int(input())                   
                    self.__COMMANDS[inp]()
                    
                # self.clear()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __del__(self):
        self.__destroy_driver()  

