import cv2
import pytesseract
import imutils


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

image = cv2.imread('TesteOCRDecimal/teste.png',0)
cv2.imshow('original',image)
image = imutils.resize(image, width=300)
thresh = cv2.threshold(image, 150, 255, cv2.THRESH_BINARY_INV)[1]

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

result = 255 - close 
result = cv2.GaussianBlur(result, (5,5), 0)

data = pytesseract.image_to_string(result, lang='eng',config='--psm 10 ')
processed_data = ''.join(char for char in data if char.isnumeric() or char == '.')
print(data)
print(processed_data)

#cv2.imshow('thresh', thresh)
#cv2.imshow('close', close)
#cv2.imshow('result', result)
cv2.waitKey()