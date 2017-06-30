# Just a silly program to track the location of the iss on an ascii map
# ASCII converter credited in code, just tweaked a bit and used it as a module here


import requests
import ascii_art
from clint.textui import colored
from PIL import Image
import math


def find_iss(width, height):
	r = requests.get("http://api.open-notify.org/iss-now.json")
	response = r.json()
	latitude = response["iss_position"]["latitude"]
	longitude = response["iss_position"]["longitude"]

	# normalize everything to make it easier
	adj_lat = float(latitude) + 90
	adj_long = float(longitude) + 180
	
	# co-ordinates on the scaled map
	map_lat = int(math.floor(adj_lat*.138))
	map_long = int(math.floor(adj_long*.277))

	return map_lat, map_long


def draw_map(image, latitude , longitude):
	# get the list of characters that will make up the map
	image_list = ascii_art.convert_image_to_ascii(image)[1]
	
	#this is the character that will be converted
	location_char = image_list[latitude][longitude]
	iss_char = str(colored.red('X'))
	new_image_list = list(image_list[latitude])

	#replace the character and insert it back into the list
	new_image_list[longitude] = iss_char
	new_image_list = "".join(new_image_list)
	image_list[latitude] = new_image_list

	return "\n".join(image_list)

def get_dimensions(image):
	#get the ascii map dimensions
	width, height = ascii_art.scale_image(image)[1:3]
	map_center = {
					'width': int(width/2), 
					'height': int(height/2),

				 }
	
	#find and replace the character, then print the new image
	y, x = find_iss(map_center['width'], map_center['height'])
	ascii_iss_location = draw_map(image, y,x)
	print ascii_iss_location


if __name__=='__main__':
	import sys

	image_path = sys.argv[1]
	get_dimensions(Image.open(image_path))

