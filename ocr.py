import cv2
import easyocr
import matplotlib.pyplot as plt

# Ruta de la imagen escaneada
image_path = 'Texto.png'

# Leer la imagen
img = cv2.imread(image_path)

# Inicializar el lector de easyocr
reader = easyocr.Reader(['en'], gpu=False)

# Realizar OCR en la imagen
text_ = reader.readtext(img)

# Dibujar cuadros alrededor del texto detectado y mostrar el texto
for t in text_:
    bbox, text, score = t
    print(f"Bbox: {bbox}, Texto: {text}, Puntaje: {score}")
    
    # Asegurarse de que bbox tiene el formato correcto
    if len(bbox) == 4:
        # bbox es una lista de cuatro puntos [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        top_left = tuple(bbox[0])
        bottom_right = tuple(bbox[2])
        cv2.rectangle(img, top_left, bottom_right, (0, 0, 255), 2)

# Mostrar la imagen con los cuadros de texto
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')  # Ocultar ejes
plt.show()
