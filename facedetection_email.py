#from harr cascade we can use diffrent types face detection algorithms that are already pre made in
#github page open cv

#scale factor This means that this size of face is detected in the image if present.
# However, by rescaling the input image, you can resize a larger face to a smaller one,
# making it detectable by the algorithm.

#minneighbours This parameter will affect the quality of the detected faces. Higher value results in less
# detections but with higher quality. 3~6 is a good value for it.
import cv2 as cv
import smtplib
from tkinter import *
from tkinter import messagebox

def sendemails():
    try:
        global  user_username,user_password
        server= smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(user_username,user_password)
        server.sendmail(user_username,user_username,"you have a intruder in your room")
        print("email sent")
        server.quit()
    except:


        messagebox.showwarning("Warning", "invalid username and password")



video = cv.VideoCapture(0)
harr_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = video.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    faces = harr_cascade.detectMultiScale(gray, 1.3, 5)

    if len(faces) >= 1:
        sendemails()
        break

    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=5)

    cv.imshow("ola", frame)

    if cv.waitKey(1) & 0xff == ord("q"):
        break
video.release()
cv.destroyAllWindows()









