# Whatsapp-Bot
Simple Whatsapp bot that sends custom messages and attach multiple images and videos to a CSV contact list. User can specify the contacts that will receive the message and customize each message based on the contact's name. Uses selenium and chromedriver to navigate.

## Main features
* Customized messages
* Multiple attachments per contact
* CSV-based contact lookup
* Uses only reliable and well known libraries

## Prerequisites and installation
* Python
* Selenium
* Chromedriver
* Pandas

## Unfamiliar with Python or Selenium? See the complete steup step by step below
* Install Python from https://www.python.org/
  * When installing, check the box "Add Python to Environment Variables"
* On windows, open cmd.exe and type the following commands
  * "pip install selenium"
  * "pip install pandas"
* Install VS Code from https://code.visualstudio.com/
  * Or any other IDE that you prefer (PyCharm, Spyder etc.)
* Install Chrome's webdriver from http://chromedriver.chromium.org/downloads
  * chromedriver version must be the same as your Google Chrome version
  * To check your version:
  
  ![](Manual/mImages/00.png)
  
  ![](Manual/mImages/01.png)
  
  * Unzip chromedriver.exe to the same folder where your project is located (chromedriver v81 is attached here)
  * Open VS Code and click on customize -> Python
  
  ![](Manual/mImages/02.png)
  
  * Start -> Open Folder -> Navigate to your project's folder
  
  ![](Manual/mImages/03.png)
  
  ## WhatsappBot.py code - Step by step execution description
  * Import selenium, time, pandas and os
  
  ![](Manual/mImages/04.png)
  
  * Write custom message and leave a _NAME_ key to repalce with contact's names
  
  ![](Manual/mImages/05.png)
  
  * Import CSV file with names and phone numbers and convert the generated dataframe to string

  ![](Manual/mImages/25.PNG)
  
  ![](Manual/mImages/06.png)
  
  * Get names and paths of all images on _Images_ folder (where all attachments must be located)
  
  ![](Manual/mImages/07.png)
  
  * Create 2 custom functions: "clean" phone numbers and retrieve the contacts's first names
  
  ![](Manual/mImages/08.png)
  
  * Create a webdriver object and navigate to whatsapp web
  
  ![](Manual/mImages/09.png)
  
  * Wait 15 seconds for page to load and for user to scan QR code
  
  ![](Manual/mImages/10.png)
  
  * Loop all contacts from the CSV file
  
  ![](Manual/mImages/11.png)
  
  
