import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
#Funcion para seleccionar un archivo de imagen
def seleccionar_imagen():
    Tk().withdraw() #Ocultar la ventan principal de Tkinter
    ruta_archivo = askopenfilename(filetypes=[("Imagenes", "*.jpg;*.png")])
    return ruta_archivo
#Seleccionar la imagen
ruta_imagen = seleccionar_imagen()
if not ruta_imagen:
    print("No se selecciono ninguna imagen.")
    exit()
#Cargar la imagen en escala de grises
i_gris = cv2.imread(ruta_imagen, cv2.IMREAD_GRAYSCALE)

#Expansion de contraste que no altera el histograma
i_expansion = i_gris.copy()

#Ecualizacion de histograma
i_ecualizada = cv2.equializeHist(i_gris)

#Calcular histogramas(rango 256 para todos)
hist_original = cv2.calcHist([i_gris],[0],None,[256],[0,256],[0,256])
hist_expansion = cv2.calcHist([i_expansion],[0], None, [256],[0,256])
hist_ecualizada = cv2.calcHist([i_ecualizada],[0],None, [256],[0,256])

#Configuracion del grafico
plt.figure(figsize=(18,12))

#Imagen e Histograma para la imagen original
plt.subplot(3,2,1)
plt.imshow(i_gris,cmap='gray')
plt.title('imagen original', fontsize=12)
plt.xlabel('Nivel de intensidad')
plt.ylabel('Frecuencia')

#Imagen e Histograma para la imagen expandida(igual que el original)
plt.subplot(3,2,3)
plt.imshow(i_expansion, cmap='gray')
plt.title('Imagen expansion', fontsize=12)
plt.axis('off')

plt.subplot(3,2,4)
plt.plot(hist_expansion, color='blue')
plt.title('Histograma - Expansion', fontsize=12)
plt.xlabel('Nivel de intensidad')
plt.ylabel('frecuencia')

#Imagen e histograma para la imagen ecualizada
plt.subplot(3,2,5)
plt.imshow(i_expansion, cmap='gray')
plt.title('Imagen ecualizada', fontsize=12)
plt.axis('off')

plt.subplot(3,2,6)
plt.imshow(hist_ecualizada, color='gray')
plt.title('histograma- ecualizada', fontsize=12)
plt.xlabel('nivel de intensidad')
plt.ylabel('frecuencia')

#Ajustar la presentacion de los graficos para mayor espacio
plt.show()