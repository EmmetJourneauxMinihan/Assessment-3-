import cv2
import msvcrt as m

def qrcode_reader():
    camera = cv2.VideoCapture(0)
    
    print("Press enter to scan qr code")
    m.getch()
    return_value, image = camera.read()
    
    cv2.imwrite('temp.png', image)
    
    img = cv2.imread('temp.png')
    
    detector = cv2.QRCodeDetector()
    data, bbox, straight_qrcode = detector.detectAndDecode(img)
    print("\n\nThe qr code resolved to:\t",data)
    
    cv2.imshow("QR_code", img)
    
    cv2.waitKey(0) 
    
    cv2.destroyAllWindows() 
    del(camera)
    

qrcode_reader()
