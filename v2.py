
import cv2
import glob
import os

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
# face_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
# face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
img_files = list(glob.glob(os.path.join("shots",'*.*')))
count = 0
for img_file in img_files:
    
    img = cv2.imread(img_file)
    blur_rate = cv2.Laplacian(img, cv2.CV_64F).var()
    if blur_rate > 145 and blur_rate < 155:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        height, width = img.shape[:2]
        # min size of face w.r.t. image (using max was intentional)
        # min_size = int(max(0.4*width, 0.3*height))
        faces = face_cascade.detectMultiScale(gray,
                                            scaleFactor=1.0485258,
                                            minNeighbors=3,
                                            minSize=(60, 60))
       
        print(img_file)
        print(len(faces))
        print(blur_rate)
        if len(faces) == 1:# want only one face
            cv2.putText(img, "{}: {:.2f}".format("blur rate",blur_rate), (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
            cv2.imwrite(f"./faces/face{count}.jpg", img)
        count += 1

    