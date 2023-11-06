#照片去背
from rembg import remove
from PIL import Image
import cv2
from google.colab.patches import cv2_imshow

input_path='IMG_5805.JPG'
output_path='output.png'
imput = Image.open(input_path)
output = remove(imput)
output.save(output_path)

img=cv2.imread('output.png')
cv2_imshow(img)
