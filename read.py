import fitz  # PyMuPDF
import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

# Ruta del archivo PDF
pdf_path = 'documento.pdf'

# Abrir el archivo PDF
pdf_document = fitz.open(pdf_path)

# Inicializar el lector de easyocr
reader = easyocr.Reader(['en'], gpu=False)

# Procesar cada página del PDF
for page_num in range(len(pdf_document)):
    # Obtener la página
    page = pdf_document.load_page(page_num)
    
    # Renderizar la página a una imagen de píxeles
    pix = page.get_pixmap()
    
    # Convertir la imagen a un formato utilizable por OpenCV
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    
    # Si la imagen tiene 4 canales, convertirla a BGR
    if img.shape[2] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    
    # Realizar OCR en la imagen
    text_ = reader.readtext(img)

    # Dibujar cuadros alrededor del texto detectado y mostrar el texto
    for t in text_:
        bbox, text, score = t
        print(f"Página {page_num + 1} - Bbox: {bbox}, Texto: {text}, Puntaje: {score}")
        
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

# Cerrar el documento PDF
pdf_document.close()
