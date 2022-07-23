from time import sleep
from src import YoutubeController,Remote

def test_remote():
    global driver
    global remote
    
    controller = YoutubeController("https://www.youtube.com/watch?v=klZNvJArVSE&ab_channel=BennytheButcher")
    driver = controller.get_driver()
    remote = Remote(driver)
    
    assert remote != None


def test_start_video():
    for i in range(0,20):
        if  remote.get_current_window_state() == "WATCH":
            return True
        else : sleep(.5)
    assert False

def test_play():
    sleep(.2)
    status_before = remote.get_status()["Playing"]
    sleep(.2)
    status = remote.toggle_play()["Playing"]
    assert status_before != status


def test_mute():
    status_before = remote.get_status()["Muted"]
    status = remote.toggle_mute()["Muted"]
    assert status_before != status

def test_forward():
    status_before = remote.get_status()["Current_time"]
    status = remote.forward_10s()["Current_time"]
    assert status_before != status

def test_backward():
    status_before = remote.get_status()["Current_time"]
    status = remote.backward_10s()["Current_time"]
    assert status_before != status

def test_search():
    
    
    remote.search("The Weeknd")
    assert remote.get_current_window_state() == "SEARCH"

def test_select_video():
    remote.select_video(2)
    assert remote.get_current_window_state() == "WATCH"

def test_recommendations():
    sleep(2)
    assert len(remote.get_recommendations()) != 0

def test_teardown():
    driver.close()
    driver.quit()
    