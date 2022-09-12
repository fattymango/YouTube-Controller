
from time import sleep
from src import YoutubeController,Remote

def test_remote():
    global driver
    global remote
    global controller
    controller = YoutubeController('https://www.youtube.com/',True)
    driver = controller.get_driver()
    remote = Remote(driver)
    
    assert remote != None


def test_open_video():
    assert remote.go_to_url('https://www.youtube.com/watch?v=Z-48u_uWMHY&list=RD_ST6ZRbhGiA&index=10&ab_channel=KendrickLamarVEVO')
    sleep(2)
    return remote.get_status(flag=False,wait = True, encode= False)['page_status']['state'] == "watch"
    
        

def test_play():
    assert  remote.toggle_play() == True

def test_set_quality():
    assert remote.set_quality(1) == True
def test_mute():
    assert  remote.toggle_mute() == True

def test_forward():
   assert  remote.forward_10s() == True

def test_backward():
   assert  remote.backward_10s() == True

def test_volume_up():
   assert  remote.volume_up() == True

def test_volume_down():
   assert  remote.volume_down() == True

def test_paly_back_speed_up():
   assert  remote.paly_back_speed_up() == True

def test_paly_back_speed_down():
   assert  remote.paly_back_speed_down() == True

def test_start_of_video():
   assert  remote.start_of_video() == True

def test_end_of_video():
   assert  remote.end_of_video() == True

def test_auto_play():
   assert  remote.toggle_auto_play() == True

def test_playback_up():
   assert  remote.playback_up()    == True

def test_playback_down():
   assert  remote.playback_down()    == True


def test_search():
    assert remote.search("The Weeknd") == True
    sleep(5)
    return remote.get_status(flag=False,wait = True, encode= False)['page_status']['state']   == "search" 
         
def test_teardown():
    controller.close_driver()