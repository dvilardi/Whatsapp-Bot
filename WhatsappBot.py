# --------------------------------------------------------------------------------------------------------------------------------------------------
# Import libraries
# --------------------------------------------------------------------------------------------------------------------------------------------------

print("--------------------------------------------------------------------------------------------------------------------------")
print("Whatsapp Bot V1.0")
print("--------------------------------------------------------------------------------------------------------------------------")
print("Importing libraries")

from selenium import webdriver                  # import the navigator
from selenium.webdriver.common.keys import Keys # Keys library (to use SHIFT+ENTER)
import time                                     # time library to add delays between commands
import pandas as pd                             # pandas library to read CSV files (with whatsapp contacts)
import os                                       # file and directory management
import sys                                      # Will be used to flush the debug window


# --------------------------------------------------------------------------------------------------------------------------------------------------
# Main message (customizable)
# --------------------------------------------------------------------------------------------------------------------------------------------------

print("Storing main message")

mainMsg = ["Custom message test.", "Name: _NAME_"]
#mainMsg = "" #uncomment this if you don't want messages, just attachments

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Import contacts csv as dataframe and convert to string
# --------------------------------------------------------------------------------------------------------------------------------------------------

print("Importing CSV")

csvFileName = "Contacts.csv"
contactsDF = pd.read_csv(csvFileName, error_bad_lines = False, sep=';')
contactsDF = contactsDF.applymap(str)
nContacts = len(contactsDF.index)

# --------------------------------------------------------------------------------------------------------------------------------------------------
# List all images to attach (if there are no images on the images folder, the code will not attach anything)
# --------------------------------------------------------------------------------------------------------------------------------------------------

print("Listing attachments")

nImages = 0                                                # control variable to get total number of attachments
mainPath = os.path.dirname(os.path.abspath(__file__))      # path of current file
imgPath = mainPath + "\\Images"                            # path of images folder within current folder
imgFiles = []                                              # initialize empty list of images 

for r,d,f in os.walk(imgPath):
    for file in f:
        imgFiles.append(imgPath + "\\" + file)
        nImages = nImages + 1


# --------------------------------------------------------------------------------------------------------------------------------------------------
# Function to leave only numbers of string and also remove leading zeroes
# --------------------------------------------------------------------------------------------------------------------------------------------------

print("Declaring user defined functions")

def onlyNumbers(fullString):
    a = ""
    
    for i in range(len(fullString)):
        for k in range(10):
            if fullString[i] == k or fullString[i] == str(k):
                a = a + fullString[i]
    
    finalStr = a.lstrip('0') 
    return finalStr

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Function to extract first name
# --------------------------------------------------------------------------------------------------------------------------------------------------

def firstName(fullName):
    return fullName.split()[0]

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Webdriver object
# --------------------------------------------------------------------------------------------------------------------------------------------------

print("Opening chrome")

driver = webdriver.Chrome(executable_path = r'./chromedriver.exe')

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Navigate to whatsapp web 
# --------------------------------------------------------------------------------------------------------------------------------------------------

print("Accessing whatsapp web")

driver.get('https://web.whatsapp.com')

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Wait 15 seconds for user to log in using QR code
# --------------------------------------------------------------------------------------------------------------------------------------------------

print("Waiting for QR code log-in")

for i in range(20,0,-1):
    sys.stdout.write(str(i)+' ')
    sys.stdout.flush()
    time.sleep(1)

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Loop all contacts in the CSV file
# --------------------------------------------------------------------------------------------------------------------------------------------------

print("Looping contacts")

st = 3      # sleep time in seconds

# Begin loop
for i in range(nContacts):
    
    # Get name, first name and phone number
    cName = contactsDF.at[i,'Name']
    cFirstName = firstName(cName)
    cNumber = onlyNumbers(contactsDF.at[i,'Phone'])

    print("\n--------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Contact " + str(i+1) + " of " + str(nContacts) + ": " + cName + " (" + cNumber + ")")
    print("--------------------------------------------------------------------------------------------------------------------------")
    
    # Get search box
    # <div class="_2S1VP copyable-text selectable-text" contenteditable="true" data-tab="3" dir="ltr"></div>
    print("Finding searchbox and writing contact's number")
        
    searchBox = driver.find_element_by_class_name('_2S1VP')
    searchBox.click()
    time.sleep(st)
    for i in range(0,30):
        searchBox.send_keys(Keys.BACKSPACE)
        searchBox.send_keys(Keys.DELETE)
    time.sleep(st)
    
    searchBox.send_keys(cNumber)
    time.sleep(st)
    
    try: 
        # Click on the result (will use complete full name from contact list)
        print("Clicking on the contact")
        
        contactBtn = driver.find_element_by_xpath(f"//span[@title='{cName}']")
        contactBtn.click()
        time.sleep(st)

    except:
        print("Couldn't find contact's Whatsapp number")
        continue #Jump to next iteration

    # Create custom message and send the message
    if len(mainMsg) > 0:
        # Get msgBox reference
        print("Finding the message box and typing the custom message")
        msgBox = driver.find_element_by_class_name('_1Plpp')
        msgBox.click()
        time.sleep(st)
        
        # Write message line by line
        for msg in mainMsg:
            msgBox.send_keys(msg.replace("_NAME_",cFirstName))
            msgBox.send_keys(Keys.SHIFT + Keys.ENTER)
        time.sleep(st)

        # Press enter (easier than looking for the "send button")
        #time.sleep(st)
        #msgBox.send_keys(Keys.ENTER)
        #time.sleep(st)
        
        # Find the send button and click it (the right way)
        sendBtn = driver.find_element_by_xpath("//span[@data-icon='send']")
        sendBtn.click()
        time.sleep(st)

    # Send attachments
    print("Sending attachments")
    if nImages > 0:

        # Get first attachment button (clip shaped) to click and open attachment options
        clipBtn = driver.find_element_by_xpath("//div[@title='Attach']")
        clipBtn.click()
        time.sleep(st)

        # Get input element
        imageBox = driver.find_element_by_xpath("//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
            
        # Attach images (loop)
        imgStr = ""
        ic = 0
        for imgFile in imgFiles: # create an imgStr string with all image file paths separated by a new line (\n)
            ic = ic + 1
            if ic == 1:
                imgStr = imgFile
            else:
                imgStr = imgStr + "\n" + imgFile
        
        imageBox.send_keys(imgStr)
        time.sleep(st)
        
        # Send attachments
        sendAttachments = driver.find_element_by_xpath("//span[@data-icon='send']") # changed "send-light" to "send"
        sendAttachments.click()

    time.sleep(st)
