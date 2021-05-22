import cv2

def isVideo(pathFile:str, posX:int=0, posY:int=0):
    nameWindow = "video"
    cv2.namedWindow(nameWindow)
    cv2.moveWindow(nameWindow, posX, posY)

    width = 960
    height = 640
    
    cap = cv2.VideoCapture(pathFile)
    while True:
        retVal, frame = cap.read()
        if cv2.waitKey(1) == 27 or (not retVal):
            break
        
        resize = cv2.resize(frame, (width, height))
        cv2.imshow(nameWindow, resize)

        
    cap.release()
    cv2.destroyAllWindows()
    return 0

