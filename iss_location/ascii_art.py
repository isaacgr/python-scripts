#Project taken from 
#https://www.hackerearth.com/practice/notes/beautiful-python-a-simple-ascii-art-generator-from-images/
#Just copying to learn


from PIL import Image

ASCII_CHARS = ['#', '?', '%', '.', 'S', '+', '.', '*', ':', ',', '@']

def scale_image(image, new_width = 200):
	#Resizes the image preserving the aspect ratio

	(original_width, original_height) = image.size
	aspect_ratio = original_width/float(original_height)
	new_height = int(new_width/aspect_ratio)

	new_image = image.resize((new_width, new_height))
	return new_image, new_width, new_height
	
def convert_to_grey_scale(image):
	return image.convert('L')

def map_to_ascii(image, range_width=25):
	#Maps each pixel to an ascii char based on the range in which it lies
	#0-255 divided into 11 ranges of 25 pixels each

	pixels_in_image = list(image.getdata())
	pixels_to_chars = [ASCII_CHARS[pixel_value/range_width] for pixel_value in pixels_in_image]

	return "".join(pixels_to_chars)

def convert_image_to_ascii(image, new_width=200):
	image = scale_image(image)[0]
	image = convert_to_grey_scale(image)

	pixels_to_chars = map_to_ascii(image)
	len_pixels_to_chars = len(pixels_to_chars)

	image_ascii = [pixels_to_chars[index: index + new_width] for index in xrange(0, len_pixels_to_chars, new_width)]
	return "\n".join(image_ascii), image_ascii

def handle_image_conversion(image_path):
	image = None
	try:
		image = Image.open(image_path)
	except Exception, e:
		print('Error')
		return
	image_ascii = convert_image_to_ascii(image)[0]
	print image_ascii

if __name__=='__main__':
	import sys

	image_path = sys.argv[1]
	handle_image_conversion(image_path)
