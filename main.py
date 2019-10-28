from PIL import Image
import pytesseract
import argparse
import cv2
import os
import re
import GetOldTweets3 as got

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="image")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="args")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
image2 = cv2.addWeighted(image, 0.25, image, 0, 100)
#Change above line to decrease contract - cv2.addWeighted( img, contrast, img, 0, brightness) https://stackoverflow.com/questions/39308030/how-do-i-increase-the-contrast-of-an-image-in-python-opencv
gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# check to see if we should apply thresholding to prepWcess the
# image
if args["preprocess"] == "thresh":
	gray = cv2.threshold(gray, 0, 255,
		cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
# make a check to see if median blurring should be done to remove
# noise
elif args["preprocess"] == "blur":
	gray = cv2.medianBlur(gray, 3)
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "testtweets/{}.png".format(os.getpid())
cv2.imwrite(filename, gray)
#DECREASE CONTRAST SO DATE/TIME/NAME CAN BE SEEN BETTER

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

handle_check = re.search('(@[^ ]+) .*', text)
if handle_check:
	text = text.replace('\n', ' ').replace('\r', '')
	handle = re.findall('(@[^ ]+) .*', text)[0] #Make list of handles, check each handle, return one with highest similarity score
	print("Found a handle!")
	print(handle)
	print("Text:", text)
	tweet = re.findall('@[^ ]+ (.*)[0-9]{1,2}:[0-9]{1,2}', text)[0] #Assuming timestamp is recognized properly, reads up to timestamp. Add check for time
	print("Tweet:", tweet)
	tweetCriteria = got.manager.TweetCriteria().setQuerySearch(tweet).setMaxTweets(1).setUsername(handle[1:])
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0] #Iterate through tweets, similarity score.
	print(tweet.text)
else: 
	print("No handle")

# show the output images
cv2.imshow("Image", image2)
cv2.imshow("Output", gray)
cv2.waitKey(0)

#Add code to remove temp image