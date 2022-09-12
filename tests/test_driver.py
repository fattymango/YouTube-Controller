from src import YouTubeController
from src.YouTubeController.youtubecontroller import YoutubeController


def test_driver():
    global driver
    global controller
    controller = YoutubeController("https://www.youtube.com/",True)
    driver = controller.get_driver()
    assert driver != None

def test_load_page():
    assert driver.current_url == "https://www.youtube.com/"

def test_teardown():
    controller.close_driver()
    