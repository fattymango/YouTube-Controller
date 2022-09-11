'''
    Static Keys and Paths that are used in the application.
                                                                '''

'''                                               Links                                                  '''
YOUTUBE     =   "https://www.youtube.com"

'''                                                                                                      '''

'''                                             FILEPATHS                                                '''


EXTENSION   =   "\\YouTubeController\\driver\\adblock\\adblock"
DRIVER      =   "\\YouTubeController\\driver\\chromedriver.exe"

'''                                                                                                      '''

BUTTONS = {
"TOGGLE_PLAY"               :   "K"
,"TOGGLE_CAPTION"           :   "C"
,"TOGGLE_FULLSCREEN"        :   "F"
,"TOGGLE_MUTE"              :   "M"
,"FORWARD"                  :   "L"
,"BACKWARD"                 :   "J"
,"PLAYBACK_UP"              :   ">"
,"PLAYBACK_DOWN"            :   "<"
}


SHIFTBUTTONS = {
"PREV_VIDEO"                 :   "P"
,"NEXT_VIDEO"                :   "N"
,"PLAY_BACK_UP"              :   ">"
,"PLAY_BACK_DOWN"            :   "<"
}


XPATHS = {
    "SEARCH"                        :   '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input'
    ,"SEARCH_RESULTS"               :   "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]"

    
    ,"SETTINGS_CONTAINER"           :   '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[29]'
    
    ,"SUGGESTED_VIDEOS_CONTAINER"   :   '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[10]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-item-section-renderer/div[3]'
    ,"SUGGESTED_VIDEO_TITLE"        :   '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[10]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-compact-video-renderer[1]/div[1]/div/div[1]/a/h3/span'
    ,"SETTINGS_BUTTON"              :   '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[31]/div[2]/div[2]/button[4]'
    ,"CHANNEL_NAME"                 :   "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/div[1]/ytd-channel-name/div/div/yt-formatted-string/a"
    }


SCRIPTS = {
    "SETTINGS"      :   'document.querySelector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-button.ytp-settings-button").click();'
    ,"QUALITY"      :   'document.querySelector("#ytp-id-17 > div > div > div:last-child").click();'
    ,"HIGHEST"      :   'document.querySelector("#ytp-id-17 > div > div.ytp-panel-menu > div:nth-child(1)").click()'
    ,"LOWEST"       :   'n = document.querySelector("#ytp-id-17 > div > div.ytp-panel-menu").childNodes.length - 1;selector = "#ytp-id-17 > div > div.ytp-panel-menu > div:nth-child("+n.toString()+")";document.querySelector(selector).click();'
    ,"AUTO"         :    'document.querySelector("#ytp-id-17 > div > div.ytp-panel-menu").lastElementChild.click()'
    ,"QUALITY_SECOND"      :   'document.querySelector("#ytp-id-18 > div > div > div:last-child").click();'
    ,"HIGHEST_SECOND"      :   'document.querySelector("#ytp-id-18 > div > div.ytp-panel-menu > div:nth-child(1)").click()'
    ,"LOWEST_SECOND"       :   'n = document.querySelector("#ytp-id-18 > div > div.ytp-panel-menu").childNodes.length - 1;selector = "#ytp-id-18 > div > div.ytp-panel-menu > div:nth-child("+n.toString()+")";document.querySelector(selector).click();'
    ,"AUTO_SECOND"         :    'document.querySelector("#ytp-id-18 > div > div.ytp-panel-menu").lastElementChild.click()'
    ,"AUTO_PLAY"     :  'document.querySelector("#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(1)").click()'
    }

SELECTORS = {
    "MUTE"                 :    '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > span > button'
    ,"PLAY"                :    '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > button'
    ,"CURRENT_TIME"        :    '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span:nth-child(2) > span.ytp-time-current'
    ,"FULL_TIME"           :    '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span:nth-child(2) > span.ytp-time-duration' 
    ,"LIKE_BUTTON"         :    '#segmented-like-button > ytd-toggle-button-renderer > yt-button-shape > button'
    ,'DISLIKE_BUTTON'      :    '#segmented-dislike-button > ytd-toggle-button-renderer > yt-button-shape > button'
    ,'SUBSCRIBE'           :    '#subscribe-button > ytd-subscribe-button-renderer > yt-button-shape > button' 
    ,'UNSUBSCRIBE'         :    '#confirm-button > yt-button-shape > button > yt-touch-feedback-shape > div > div.yt-spec-touch-feedback-shape__fill'
    ,'AUTO_PLAY'           :    '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button:nth-child(1) > div > div'
    ,'SUBTITLE'            :    '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-subtitles-button.ytp-button'
    ,'FULLSCREEN'          :    '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-right-controls > button.ytp-fullscreen-button.ytp-button'
    ,'TITLE'               :    '#title > h1 > yt-formatted-string'
    ,'CHANNEL'             :    '#text > a'
    ,'VIEWS'               :    '#formatted-snippet-text > span:nth-child(1)'
}

TAGS = {
"PLAYER_CONTAINER"             :   'player-container'
,"SEARCH_VIDEO_PLAYER"         :   'ytd-video-renderer'
,"SUGGESTED_VIDEO"             :   'ytd-compact-video-renderer'
,"CHANNEL_CONTAINER"           :   'ytd-video-owner-renderer'
,"VIDEO_PLAYER"                :   '#movie_player > div.html5-video-container > video'
}

