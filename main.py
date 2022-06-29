from src.keys import YOUTUBE
from src.remote import Remote
from src.youtubecontroller import YoutubeController


'''
    This is the main file to excute the application.
        Requires Selenium.driver from YoutubeController
            to be passes to the Remote and calling 
                main().
                                                        '''


driver = YoutubeController(url=YOUTUBE).get_driver()

remote = Remote(driver)

remote.main()

