#Obtenga las coordenadas X y Y de los contornos de dos logos de automóviles (Chevrolet, Hyundai, Mazda, etc.), a través de Python.
import cv2

img=cv2.imread('logo1.jpg')
img2=cv2.imread('logo2.jpg')
imgbinary = cv2.Canny(img,20,60)
imgbinary2 = cv2.Canny(img2,20,60)
contornos, jerarquia =cv2.findContours(imgbinary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contornos2, jerarquia2 =cv2.findContours(imgbinary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(contornos)
print(contornos2)

cv2.drawContours(img,contornos,-1,(0,255,0),3)
cv2.drawContours(img2,contornos2,-1,(0,255,0),3)


cv2.imshow("imagen1",img)
cv2.imshow("escala gris",imgbinary)
cv2.imshow("imagen2",img2)
cv2.imshow("escala gris2",imgbinary2)

cv2.waitKey(0)
cv2.destroyAllWindows()
