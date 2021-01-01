import cv2

def extract_face(image):
    face_cascade = cv2.CascadeClassifier("src/CascadeFile/face-detect.xml")

    image = image.copy()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    face_coords = face_cascade.detectMultiScale(gray, 1.3, 3)
    
    return face_coords

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)

    while 1:
        _, frame = cam.read()
        frame = cv2.resize(frame, (640, 480))

        for x, y, w, h in extract_face(frame):
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        cv2.imshow("Preview", frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
