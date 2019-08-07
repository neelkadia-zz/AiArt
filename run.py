import sys
from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

response.download({"keywords":sys.argv[1],"limit":1})  #download images from Google
