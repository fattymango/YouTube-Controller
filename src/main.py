



'''
    This is the main file to excute the application.
        Requires Selenium.driver from YoutubeController
            to be passes to the Remote and calling 
                main().
                                                        '''


from YouTubeController.youtubecontroller import YoutubeController

from YouTubeController.keys import YOUTUBE

from YouTubeController.operator import Operator


driver = YoutubeController(YOUTUBE)
op = Operator(driver)
op.main(debug=False)
# remote = Remote(driver.get_driver())

# remote.main()
