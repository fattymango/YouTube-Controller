

import json
from time import sleep

import datetime
from YouTubeController.keys import SELECTORS, XPATHS,TAGS

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Status:
    def __init__(self,driver) -> None:
        self.__driver = driver
        self.__is_on = True
        self.last_current_video_status_payload  = {}
        self.__latest_url = ''
        self.__last_collected = None
    def check_new_url(self):
        print(self.__latest_url ,self.__driver.current_url)
        flag = self.__latest_url == self.__driver.current_url
        print (flag)
        self.__latest_url =  self.__driver.current_url
        return not flag
    def minute_passed(self):
        if self.__last_collected == None:
            self.__last_collected = datetime.datetime.now()
            return True
        elif abs((self.__last_collected-datetime.datetime.now()).total_seconds()) >= 60:
            self.__last_collected = datetime.datetime.now()
            return True
        else:
            return False
    def get_status(self,suggestions = True,wait = False,encode = True):
        payload = {}
        try:
            payload['is_on'] = str(self.__is_on).lower()
            if(self.__is_on):
                if wait : sleep(1.5)
                payload['page_status' ]= self.page_status()
                payload['new_video_status'] = False
                payload['video_status'] = self.last_current_video_status_payload
                if  suggestions : payload ['suggestions'] = self.suggested_videos()
                if (self.check_new_url() or self.minute_passed()):
                    self.__last_collected = datetime.datetime.now()
                    WebDriverWait(self.__driver, 7).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,SELECTORS['TITLE'])))
                    payload['video_status'] = self.current_video_status() 
                    payload['new_video_status'] = True
                
                
                    

        except Exception as e:
            pass
            # print(e)

        return json.dumps(payload) if encode  else  payload
    def set_driver(self,driver):
        self.__driver = driver
        self.__is_on = True
    def destroy_driver(self):
        self.__driver = None
        self.__is_on = False
    def __clean_string(self,string : str):
        return string.replace('\'',"").replace('\"',"")  
    def suggested_videos(self):
        body = self.__driver.find_element_by_tag_name('body')
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_UP)
        body.send_keys(Keys.PAGE_UP)
        body.send_keys(Keys.PAGE_UP)
        body.send_keys(Keys.PAGE_UP)
        body.send_keys(Keys.PAGE_UP)
        body.send_keys(Keys.PAGE_UP)
        body.send_keys(Keys.PAGE_UP)
        body.send_keys(Keys.PAGE_UP)
        return{

            "HOME" : self.__get_home_videos,
            "WATCH" : self.__get_recommended_videos,
            "SEARCH" : self.__get_search_results

        }[self.get_current_window_state()]()
        
    def page_status(self):
        payload = {}
        try:
            state = self.get_current_window_state()
            url = self.__driver.current_url
            payload = {
                "state": self.__clean_string(str(state).lower()), 
                "url" :  self.__clean_string(str(url))
            }
     
        except Exception as e:
            pass
            # print(e)
        return payload
    def __get_text(self,selector):
        
        try:
            value = self.__driver.find_element_by_css_selector(SELECTORS[selector]).text
        except:
            # print(selector)
            value = None
        return value
    def __get_attribute(self,selector,attribute):
        try: 
            value = self.__driver.find_element_by_css_selector(SELECTORS[selector]).get_attribute(attribute)
        except:
            # print(selector)
            value = None
        return value
    def __get_true_value(self,var, expression,value):
        try:    
            return value if var == expression else not value
        except:
            return None
    def current_video_status(self):
        container = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, TAGS["VIDEO_PLAYER"]))
            ).send_keys(',')
        payload = {}
        if not self.get_current_window_state() == 'WATCH':return payload
        try:
            
            ctime = self.__get_text("CURRENT_TIME") 
            ftime = self.__get_text("FULL_TIME") 
            
            title = self.__get_text("TITLE") 
            views = self.__get_text("VIEWS") 
            subscribed = self.__get_text("SUBSCRIBE") 
            url = self.__driver.current_url
            subtitle_pressed,subtitle_available = self.__check_subtitle()
            play = self.__get_attribute("PLAY","title") 
            mute = self.__get_attribute("MUTE","title") 
            fullscreen = self.__get_attribute("FULLSCREEN","title")
            like = self.__get_attribute("LIKE_BUTTON","aria-pressed")
            dislike = self.__get_attribute("DISLIKE_BUTTON","aria-pressed") 
            au2play = self.__get_attribute("AUTO_PLAY","aria-checked")
            try: 
                channel_img = self.__driver.find_element_by_tag_name(TAGS['CHANNEL_CONTAINER']).find_element_by_id('img').get_attribute('src')
                channel = self.__driver.find_element_by_xpath(XPATHS["CHANNEL_NAME"]).text
            except:
                channel_img = None
                channel = None
            
            
            payload = {
                "playing" :             self.__clean_string (str(self.__get_true_value(play,"Pause (k)",True )).lower()),
                "muted" :               self.__clean_string (str(self.__get_true_value(mute,"Unmute (m)",True )).lower()),
                "full_screen":          self.__clean_string (str(self.__get_true_value(fullscreen,"Full screen (f)",False )).lower()),
                "current_time" :        self.__clean_string (str(ctime)),
                "full_time":            self.__clean_string (str(ftime)),
                "title" :               self.__clean_string (str(title)),
                "views" :               self.__clean_string (str(views)),
                "auto_play":            self.__clean_string (str(self.__get_true_value(au2play,"true",True )).lower()),
                "subtitle_pressed":     self.__clean_string (str(subtitle_pressed).lower()),
                "subtitle_available":   self.__clean_string (str(subtitle_available).lower()),
                "subscribed" :          self.__clean_string (str(self.__get_true_value(subscribed,"Subscribed",True )).lower()),
                "like"  :               self.__clean_string (str(like).lower()),
                "dislike"  :            self.__clean_string (str(dislike).lower()),
                "channel"  :            self.__clean_string (str(channel)),
                "channel_img":          self.__clean_string (str(channel_img)),
                "url" :                 self.__clean_string (str(url)),
                "thumbnail":            self.__clean_string (str(self.__get_video_thumbnail(url)))
            } 
            # print(payload)
            self.last_current_video_status_payload = payload
        except Exception as e:
            print
            # print(e)
        return payload


    def __get_search_results(self):
        query = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.XPATH, XPATHS["SEARCH"]))
            ).get_attribute("value")
        payload = self.__videos_serializer('ytd-item-section-renderer','ytd-video-renderer')
        payload["query"] = query
        return payload
    def __get_recommended_videos(self):
        return self.__videos_serializer('ytd-item-section-renderer','ytd-compact-video-renderer')
    def __get_home_videos(self):
        return self.__videos_serializer('ytd-rich-grid-row','ytd-rich-grid-media')
    def __videos_serializer(self,videos_container,video_tag):
        payload = []
        data=[]

        try:
            container = self.__driver.find_elements_by_tag_name(video_tag)
            for video in container:
                try:
                    thumbnail_container = video.find_element_by_tag_name("a")
                    # print(f'thumbnail_container ={thumbnail_container}')
                    url = thumbnail_container.get_attribute('href')
                    # print(f'url ={url}')
                    thumbnail = thumbnail_container.find_element_by_tag_name('img').get_attribute('src')
                    # print(f'thumbnail ={thumbnail}')
                    x = video.text.split('\n')
                    # print(f'text ={x}')
                    data.append({
                    'url' : self.__clean_string(url),
                    'duration' : self.__clean_string(x[0]),
                    'title' : self.__clean_string(x[1]),
                    'channel' : self.__clean_string(x[2]),
                    'views' : self.__clean_string(x[3]),
                    'thumbnail' : self.__clean_string(thumbnail)     

                    })
                except Exception as e:
                    print(e)
            payload = {
                'length' : len(data),
                'data'  : data
            }
        except Exception as e:
            print(e)
        return payload
  

    def __check_subtitle(self):
        try:
            is_pressed = True if self.__driver.find_element_by_css_selector(SELECTORS["SUBTITLE"]).get_attribute("aria-pressed")== "true" else False
            if is_pressed : return is_pressed,True
            else: 
                is_available = True if self.__driver.find_element_by_css_selector(SELECTORS["SUBTITLE"]).get_attribute("title") == "Subtitles/closed captions (c)" else False
                return is_pressed,is_available
        except : return True,True
    def __get_video_thumbnail(self,url):
        
        thumbnail =url[url.index('v=')+2:url.index('v=')+13] 
        thumbnail = "https://img.youtube.com/vi/here/maxresdefault.jpg".replace("here",thumbnail)
        return thumbnail
 
    def get_current_window_state(self):
        url = self.__driver.current_url
        
        try : 
            indicator = url.split('/')[3][0]
            if indicator == "r": state = "SEARCH"
            elif indicator == "w" : state = "WATCH"
        except : state = "HOME"

        return state