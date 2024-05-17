import cv2
import easyocr
import matplotlib.pyplot as plt

image_path = 'image.jpg'

img=cv2.imread(image_path)

reader= easyocr.Reader(['en'])

text_=reader.readtext(img)

for t  in text_:
    print (t)

bbox, text , score= t

cv2.rectangle(img, bbox[0], bbox[2], (0,0,255), 2)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()