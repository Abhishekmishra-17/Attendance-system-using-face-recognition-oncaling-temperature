def camer():
    import cv2
    from urllib.request import urlopen
    import numpy as np
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # To capture video from webcam.
    #cap = cv2.VideoCapture(0)
    url="http://192.168.43.1:8080/shot.jpg"
    while True:
        # Read the frame
        #_, img = cap.read()
        imgResp=urlopen(url)
        imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        img=cv2.imdecode(imgNp,-1)
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(30, 30),flags = cv2.CASCADE_SCALE_IMAGE)

        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255,255,0), 2)


        # Display
        cv2.imshow('Webcam Check', img)

        # Stop if escape key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object
    cv2.destroyAllWindows()
