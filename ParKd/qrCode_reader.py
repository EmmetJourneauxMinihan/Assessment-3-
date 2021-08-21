import cv2
import msvcrt as m

camera = cv2.VideoCapture(0)

print("Press enter to scan qr code")
m.getch()
return_value, image = camera.read()

cv2.imwrite('image.png', image)

img = cv2.imread('image.png')

detector = cv2.QRCodeDetector()
data, bbox, straight_qrcode = detector.detectAndDecode(img)
print(data)

cv2.imshow("QR_code", img)

#waits for user to press any key 
#(this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0) 

#closing all open windows 
cv2.destroyAllWindows() 



del(camera)
