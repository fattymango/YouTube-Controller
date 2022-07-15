
from YouTubeController.keys import YOUTUBE
from YouTubeController.operator import Operator
from YouTubeController.youtubecontroller import YoutubeController


'''
    This is the main file to excute the application.
        Requires Selenium.driver from YoutubeController
            to be passes to the Remote and calling 
                main().
                                                        '''


driver = YoutubeController(url=YOUTUBE)
op = Operator(driver.get_driver())
op.main()
# remote = Remote(driver.get_driver())

# remote.main()
