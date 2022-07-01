# YouTube Controller
YouTube controller is a remote controller that uses Selenium and Chrome driver to control the YouTube website and video player.

>**Warning**
This is a the first version of the project, not user-friendly.


# How it Works?
YouTube controller uses Chrome driver to open the YouTube website  control it using Selenium library, which locates specific elements and send specific keys to perform a specific action.

>**Note**
The Remote API is still under construction, which will allow connection between smartphones and PC.


# Upcoming Features 
- ### Remote API
    
      API that connects the smartphone and the PC through a channel 
      
- ### Mobile Application 
      Which will interact with the API and excute commands remotly.
- ### Functions
    
      More functions are under construction, and more bug fixes and optimization.
      
- ### Session Save
      Session save will keep track of user's account and history which will make the experience better.   
    
 
# Classes
in this project there are 3 main classes as follows.

## YouTubeController()
    
    This class initializes the Chrome driver and sets it up, and loads the YouTube page ready to use.
    
#### Class Functions  
| Function | Description |
| --- | --- |
| ```__setup``` | Initiates the driver with the options. |
| ```__load_page ```| Loads the YouTube website. |
|``` get_driver``` | Returns  the driver after setup. |

## Utility()
    This class is the lower layer that does all of the hard work and interact with the driver.
    
 #### Class Functions     
| Function | Description |
| --- | --- |
| ```execute_action(action)```| Performs a simple command through a shortcut. <br/> Takes ```action``` which specified in ```Keys.py```.|
| ``` set_quality(quality) ``` | Sets the quality of the video. <br/> Takes ```quality``` which specified in ```Keys.py```. |
| ``` search(q) ``` | Searches for video. <br/> Takes a query  ```q``` to search for. |
| ``` select_video(index) ``` | Selects a video of the search results. Takes  ```index``` the index of the video. |


## Remote()
    This class acts like an intermediate between the driver and the utility class, which excutes
    functions while the driver is running.

# Issues
- Some functions are unstable and not efficient.
- Selenium ```WebElement.click()``` sometimes miss clicks the video and clicks the channel link instead (doesn't occur when fullscreen)
- Remote main still vulnerable and buggy.
- Not User-Friendly.
