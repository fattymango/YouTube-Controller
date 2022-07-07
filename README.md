# YouTube Controller
YouTube controller is a remote controller that uses Selenium and Chrome driver to control the YouTube website and video player.

>**Warning**
This is a the first version of the project, not user-friendly.


# How it Works?
YouTube controller uses Chrome driver to open the YouTube website  control it using Selenium library, which locates specific elements and send specific keys to perform a specific action.

>**Note**
The Remote API is still under construction, which will allow connection between smartphones and PC.

# Whats New.
- ## Status & Information:
  Status of the current video player and recommended videos are now sent whenever the user excutes a command, which will make the remote app more reliable and real-time.

- ## Classes optimization and structure:
  Major functions improvments, functions now are more reliable, structured and dynamically written.  

# Requirments
- ## Chrome Driver
  It's better to stick with the driver provided within the project, changing the driver may cause some errors and functions amy not work properly (YouTube changes its selectors depending on the   chrome version)
  
- ## Requirements.txt
  Requirements.txt contains all the packages needed to make this project work.
  ```
  pip install -r requirements.txt
  ```
- ## Development
  Development on this project has been done on :
  - Windows 10
  - Python - 3.9
  - Selenium - 4.1.2 

- # Contribution
  Any contibution on this project would be appreciated, if you face any issue you can open an issue and we will handle it ASAP.
  For more information do not hesitate to contact me (mkassab215@outlook.com).
# Upcoming Features 
- ### Remote API:
  API that connects the smartphone and the PC through a channel 
      
- ### Mobile Application: 
  Which will interact with the API and excute commands remotly.
- ### Functions & Features:
  More functions are under construction, and more bug fixes and optimization.
      
- ### Session Save:
  Session save will keep track of user's account and history which will make the experience better.   
    
 
# Classes
  In this project there are 3 main classes as follows.

## YouTubeController()
  This class initializes the Chrome driver and sets it up, and loads the YouTube page ready to use.
  

## Utility()
  This class is the lower layer that does all of the hard work and interact with the driver.
    

## Remote()
  This class acts like an intermediate between the driver and the utility class, which excutes
  functions while the driver is running.

# Issues
- ## Vulnerability & Bugs
  Many functions are buggy and can break the program, most of these functions will be stable next update.

- ## User-Friendly
  The project is still not user-friendly since the phone application is not out yet.
  Even the terminal controller is not well implemented.
