import requests
import ascii_art
from clint.textui import colored
from PIL import Image

r = requests.get("http://api.open-notify.org/iss-now.json")

response = r.json()

latitude = response["iss_position"]["latitude"]
longitude = response["iss_position"]["longitude"]

#def find_iss(image,latitude,longitude):
	

def get_dimensions(image):
	width, height = ascii_art.scale_image(image)[1:3]
	map_center = [int(width/2), int(height/2)]

if __name__=='__main__':
	import sys

	image_path = sys.argv[1]
	get_dimensions(Image.open(image_path))




 

