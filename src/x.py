from YouTubeController.keys import YOUTUBE,TAGS
from YouTubeController.operator import Operator
from YouTubeController.status import Status
from YouTubeController.youtubecontroller import YoutubeController


'''
    This is the main file to excute the application.
        Requires Selenium.driver from YoutubeController
            to be passes to the Remote and calling 
                main().
                                                        '''

if __name__ == '__main__':
    driver = YoutubeController(YOUTUBE)

    s = Status(driver=driver.get_driver()) 
    driver = driver.get_driver()
    while True:
        input('arnool')
        driver.get('https://www.youtube.com/watch?v=Wt88GMJmVk0')
        # print(driver.find_element_by_xpath("").text)
        # print(s.get_status())

