import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

argument_parser= ArgumentParser()
argument_parser.add_argument("-i", "--image", required=True, help="Ruta a la imagen a procesar")
arguments = vars(argument_parser.parse_args())

image= cv2.imread(arguments["image"])
cv2.inshow("image", image)
cv2.waitKey(0)

image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text= pytesseract.image_to_string(image)
print('texto escaneado: \n')
print(text)

cv2.destroyAllWindows()