
import cv2
import glob
import os

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eyes_cascade = cv2.CascadeClassifier('haarcascade_mcs_eyepair_small.xml')
img_files = list(glob.glob(os.path.join("shots",'*.*')))
count = 0
for img_file in img_files:
    
    img = cv2.imread(img_file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = img.shape[:2]
    # min size of face w.r.t. image (using max was intentional)
    # min_size = int(max(0.4*width, 0.3*height))
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.0485258,
                                          minNeighbors=4)
                                          
    eyes = eyes_cascade.detectMultiScale(gray,
                                          scaleFactor=1.0485258,
                                          minNeighbors=2)
    blur_rate = cv2.Laplacian(gray, cv2.CV_64F).var()
   
    if len(faces) == 1 and len(eyes) == 1 : # want only one face
        for (x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (127,0,255), 2)

        for (x,y,w,h) in eyes:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)
        cv2.putText(img, "{}: {:.2f}".format("blur rate",blur_rate), (10, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
        cv2.imwrite(f"./faces/face{count}.jpg", img)
        print(img_file)
        print(faces)
        print(eyes)
        print(eyes[0][0], eyes [0][1])
        print(blur_rate)
        print(f"this is the file ---> face{count}.jpg \n")

        count += 1

    