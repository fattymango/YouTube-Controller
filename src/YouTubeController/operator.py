from email import message
import os
from .remote import Remote
from network import Server


class Operator:

    def __init__(self, driver) -> None:
        self.driver = driver
        self.remote = Remote(driver)
        self.server = Server(self.remote)
        ''' 
                    Switch Cases 
                                            '''

        self.__COMMANDS = {
            0:  self.remote.get_recommendations,
            1:  self.remote.toggle_play,
            2:  self.remote.toggle_caption,
            3:  self.remote.toggle_fullscreen,
            4:  self.remote.toggle_mute,
            5:  self.remote.forward_10s,
            6:  self.remote.backward_10s,
            7:  self.remote.refresh,
            8:  self.remote.set_quality,
            9:  self.remote.select_video,
            10: self.remote.search,
        }

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

    def main(self):
        for message,option in self.server.main():
            if int(message) > 7:
                self.__COMMANDS[int(message)](option)
            else:
                self.__COMMANDS[int(message)]()
            print(message)
            
            # self.server.send_response('success')
        # inp = ""
        # while str(inp).capitalize() != 'Q' :
        #     l = self.__commands_printer()
        #     while True:
        #         inp = int(input())
        #         if inp in range(1,l+1):
        #             self.__COMMANDS[inp]()
        #             break
        #     # self.clear()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __del__(self):
        self.remote.__del__()
