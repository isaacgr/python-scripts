import requests
import ascii_art
from clint.textui import colored
from PIL import Image
import math

r = requests.get("http://api.open-notify.org/iss-now.json")

response = r.json()

latitude = response["iss_position"]["latitude"]
longitude = response["iss_position"]["longitude"]

#def find_iss(image,latitude,longitude):
	

def get_dimensions(image):
	width, height = ascii_art.scale_image(image)[1:3]
	map_center = {
					'width': int(width/2), 
					'height': int(height/2),

				 }
	latitude_steps = math.ceil(180/map_center['width'])
	longitude_steps = math.ceil(90/map_center['height'])
	
#	find_iss(image, latitude, longitude)

	image_list = ascii_art.convert_image_to_ascii(image)[1]
	location_char = image_list[map_center['height']][map_center['width']]
		
	print ascii_art.convert_image_to_ascii(image)[0]

if __name__=='__main__':
	import sys

	image_path = sys.argv[1]
	get_dimensions(Image.open(image_path))




 

