import cv2
import face_recognition
import csv
import os
import datetime
import time

# Initialize Haar Cascade for face detection
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

video_capture = cv2.VideoCapture(0)
path = "K:\\Face Recognition\\By Face_Rec\\Photos"

# Load and encode faces from the folder
encodings = []
names = []

#Taking ALl The Name And Number Of Photos For Encoding
for file_name in os.listdir(path):
    if file_name.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(path, file_name)
        name = os.path.splitext(file_name)[0]

        # Load the image and encode the face
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        if face_locations:  # Ensure a face is detected
            encoding = face_recognition.face_encodings(image, face_locations)[0]
            encodings.append(encoding)
            names.append(name)


#In Order To Check If The Student Has Been Marked Then It Will Remove
students = names.copy()
s = True

print("Press 'q' to quit.")

now = datetime.datetime.now()
current_date = now.strftime("%Y-%m-%d")

#Creating A CSV File With Current Date For Storing Attendance
f = open(current_date+".csv","w+",newline = '')
writerf = csv.writer(f)

while True:
    ret,frame = video_capture.read()
    if not ret:
        print("Failed to capture frame. Exiting...")
        break

    # Convert frame to grayscale for Haar Cascade
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces using Haar Cascade And Decrease The Size Of The Image To Load Faster
    haar_faces = haar_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x1, y1, x2, y2) in haar_faces:
        # Extract face region from the original frame
        face = frame[y1:y1+y2, x1:x1+x2]

        # Convert face region to RGB for face_recognition
        rgb_face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)

        #Detect Faces And Other Objects

        face_locations = face_recognition.face_locations(rgb_face)
        face_encodings = face_recognition.face_encodings(rgb_face,face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compare against known encodings
                    matches = face_recognition.compare_faces(encodings, face_encoding)
                    face_distances = face_recognition.face_distance(encodings, face_encoding)

        #Finding Perfect Matches
        time.sleep(5)
        if any(matches):
            idx = face_distances.argmin()
            name = names[idx]
            if name in names:
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    writerf.writerow([name, current_time, 'present'])
        else:
            name = "Unknown"#To Find If Someone Is Not From The Class

        if name!="Unknown":
            #Draw A Rectangle To Check If The Faces Are Being Detected
            cv2.rectangle(frame,(x1,y1),(x1+x2,y1+y2),(0,255,0),2)
        else:
            cv2.rectangle(frame,(x1,y1),(x1+x2,y1+y2),(0,0,255),2)
            current_time = now.strftime("%H-%M-%S")
            writerf.writerow([name, current_time, 'present'])


    #Show The Frame
    cv2.imshow("Attendance System",frame)

    #Press q To Exit
    if cv2.waitKey(10) & 0xFF ==ord('q'):
        break

# Marking Absentees
for i in students:
    writerf.writerow([i, " ", 'Absent'])
#Release Resources
video_capture.release()
cv2.destroyAllWindows()
f.close()

