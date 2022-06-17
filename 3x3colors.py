# Importing necessary libraries
import cv2
from instabot import Bot
import numpy as np
import random
from datetime import datetime

'''createPicture() : Creates a pic with given dimension with random
colors and saves it in pictures folder and returns path.'''
def createPicture(length,width,x_square_count,y_square_count):
	picture = np.zeros(shape=(width,length,3),dtype=np.uint8)
	x_offset = width//x_square_count
	y_offset = length//y_square_count
	for k in range(0,picture.shape[2]):
		for i in range(0,picture.shape[0],x_offset):
			for j in range(0,picture.shape[1],y_offset):
				pixel = random.randint(0,255)
				picture[i:i+x_offset,j:j+y_offset,k] = np.full((x_offset,y_offset), pixel)
	
	name = str(datetime.now()).replace(':','-').replace('.','-')
	cv2.imwrite(f"Pictures/picture-{name}.jpeg",picture)
	return f"Pictures/picture-{name}.jpeg"

if __name__ == "__main__":
	path = createPicture(900,900,3,3)
	with open("password.txt",'r') as f:
		password = f.read().strip()
		f.close()
	bot = Bot()
	bot.login(username = "colors3x3",password = password)
	bot.upload_photo(path,caption =" ")