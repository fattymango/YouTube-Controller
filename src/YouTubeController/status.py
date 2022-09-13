

import json
from time import sleep
from YouTubeController.keys import SELECTORS, XPATHS,TAGS

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
class Status:
    def __init__(self,driver) -> None:
        self.__driver = driver
        self.__is_on = True
    def get_status(self,flag = True,wait = False,encode = True):
        payload = {}
        try:
            if(self.__is_on):
                if wait:
                    sleep(1.5)
                
                if  flag:  
                    WebDriverWait(self.__driver, 7).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,SELECTORS['TITLE'])))

                    payload = {
                    'is_on' : str(self.__is_on).lower(),
                    'page_status' : self.page_status(),
                    'video_status' : self.current_video_status(),  
                    'suggestions' : self.suggested_videos()
                    }
                else:
                    payload = {
                    'is_on' : str(self.__is_on).lower(),
                    'page_status' : self.page_status(),
                    'video_status' : self.current_video_status(),  
                    
                    }
            else:
                payload = {
                    'is_on' : str(self.__is_on).lower(),
                    }
        except Exception as e:
            print(e)

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
            print(e)
        return payload
    def __get_text(self,selector):
        
        try:
            value = self.__driver.find_element_by_css_selector(SELECTORS[selector]).text
        except:
            print(selector)
            value = None
        return value
    def __get_attribute(self,selector,attribute):
        try: 
            value = self.__driver.find_element_by_css_selector(SELECTORS[selector]).get_attribute(attribute)
        except:
            print(selector)
            value = None
        return value
    def __get_true_value(self,var, expression,value):
        try:    
            return value if var == expression else not value
        except:
            return None
    def current_video_status(self):
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
     
        except Exception as e:
            print(e)
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
        return self.__videos_serializer('ytd-rich-grid-row','ytd-rich-item-renderer')
    def __videos_serializer(self,videos_container,video_tag):
        payload = []
        try:
            
            containers=WebDriverWait(self.__driver, 10).until(
                 EC.presence_of_all_elements_located((By.TAG_NAME,videos_container))
                )
            data = []
            
            for i in range(15):
                try:
                    container = containers[i].find_elements_by_tag_name(video_tag)
                    
                    for video in container:
                        try:
                            thumbnail_container = video.find_element_by_id('thumbnail')
                            url = thumbnail_container.get_attribute('href')
                        
                            thumbnail = thumbnail_container.find_element_by_id('img').get_attribute('src')
                            
                            x = video.text.split('\n')
                            
                            data.append({
                            'url' : self.__clean_string(url),
                            'duration' : self.__clean_string(x[0]),
                            'title' : self.__clean_string(x[1]),
                            'channel' : self.__clean_string(x[2]),
                            'views' : self.__clean_string(x[3]),
                            'thumbnail' : self.__clean_string(thumbnail)     

                            })
                        except : pass
                except : pass
            payload = {
                'length' : len(data),
                'data'  : data
            }
        except Exception:
            pass
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