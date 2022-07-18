
from src import YoutubeController


def test_driver():
    global driver
    controller = YoutubeController("https://www.youtube.com/")
    driver = controller.get_driver()
    assert driver != None

def test_load_page():
    assert driver.current_url == "https://www.youtube.com/"

def test_tabs():
    assert len(driver.window_handles) == 1

def test_teardown():
    driver.close()
    driver.quit()
    