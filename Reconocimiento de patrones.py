#importacion de modulos
import cv2
import numpy as np
#Orlando Murcia Perdomo 20162151798
#Carga la imagen
imagen1 = cv2.imread("original.jpg",0)
imagen11 = cv2.imread("original.jpg",1)
#Se crea un ciclo for para que la comparativa se haga de forma automatica con las 4 imagenes presentadas
for imagen in range(1,5,1):
    IMAGEN=str(imagen)
    template_color = cv2.imread(IMAGEN + '.jpg', 1)
   #Mostramos las caracteristicas de las dos imagenes
    print("La forma de la imagen original es: ", imagen1.shape)
    print("La forma de la imagen plantilla es: ", template_color.shape)
    cv2.imshow(IMAGEN+'numero', template_color)

    template = cv2.cvtColor(template_color, cv2.COLOR_BGR2GRAY)
    template_layers = template_color.copy()
    # A cada capa le asigno blanco y negro
    template_layers[:, :, 0] = template  # Capa B
    template_layers[:, :, 1] = template  # Capa G
    template_layers[:, :, 2] = template  # Capa R
    #Definimos el umbral de suma
    umbral = 99999
    #Se procede a crear el ciclo for para la comparativa y diferencia de las imagenes
    for x in range(0, 6):
        for y in range(0, 4):
            ROI = imagen1[y*100:100*(y+1),x*100:100*(x+1)]
            diferencia = cv2.absdiff(template, ROI)
            Sum = np.sum(diferencia)
            print(Sum)
            if Sum < umbral:
                umbral = Sum
                print(Sum)
            if Sum <= umbral:
                #Se muestra el resultado correcto una imagen totalmente negra
                cv2.imshow('Resta', diferencia)
                #Se Crea un "parche sobre la imagen original al igual que un cuadro donde se encuentra el ROI
                imagen11[y*100:100*(y+1),x*100:100*(x+1)] = template_layers
                cv2.rectangle(imagen11, (x*100, y*100), ((x+1)*100,(y+1)*100), (0, 0, 255), 3)
                cv2.imshow('resultado', ROI)
                cv2.imshow(IMAGEN+' Resultados', imagen11)
cv2.waitKey(0)
