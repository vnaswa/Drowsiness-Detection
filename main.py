import cv2
import dlib
import pyttsx3
from scipy.spatial import distance

# INITIALIZING THE pyttsx3 SO THAT ALERT AUDIO MESSAGE CAN BE DELIVERED
engine = pyttsx3.init()

# TRYING CAMERA INDEX 0 OR 1; IF CAMERAS ARE NOT WORKING, TRY VIDEO FILE INSTEAD
camera_index = 0  # Try 0 or 1
cap = cv2.VideoCapture(camera_index)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream. Trying with a sample video file...")
    # Test with a sample video file (provide correct path)
    cap = cv2.VideoCapture('path_to_a_video_file.mp4')
    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

# FACE DETECTION OR MAPPING THE FACE TO GET THE EYE AND EYES DETECTED
face_detector = dlib.get_frontal_face_detector()

# PUT THE CORRECT LOCATION OF .DAT FILE (FILE FOR PREDICTING THE LANDMARKS ON FACE)
dlib_facelandmark = dlib.shape_predictor(r"C:\Users\vaibh\shape_predictor_68_face_landmarks.dat")

# FUNCTION CALCULATING THE ASPECT RATIO FOR THE EYE BY USING EUCLIDEAN DISTANCE FUNCTION
def Detect_Eye(eye):
    poi_A = distance.euclidean(eye[1], eye[5])
    poi_B = distance.euclidean(eye[2], eye[4])
    poi_C = distance.euclidean(eye[0], eye[3])
    aspect_ratio_Eye = (poi_A + poi_B) / (2 * poi_C)
    return aspect_ratio_Eye

# MAIN LOOP IT WILL RUN UNLESS AND UNTIL THE PROGRAM IS TERMINATED BY THE USER
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector(gray_scale)

    for face in faces:
        face_landmarks = dlib_facelandmark(gray_scale, face)
        leftEye = []
        rightEye = []

        # LEFT EYE POINTS (42 to 47)
        for n in range(42, 48):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            rightEye.append((x, y))
            next_point = n + 1
            if n == 47:
                next_point = 42
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (0, 255, 0), 1)

        # RIGHT EYE POINTS (36 to 41)
        for n in range(36, 42):
            x = face_landmarks.part(n).x
            y = face_landmarks.part(n).y
            leftEye.append((x, y))
            next_point = n + 1
            if n == 41:
                next_point = 36
            x2 = face_landmarks.part(next_point).x
            y2 = face_landmarks.part(next_point).y
            cv2.line(frame, (x, y), (x2, y2), (255, 255, 0), 1)

        # CALCULATING THE ASPECT RATIO FOR LEFT AND RIGHT EYE
        right_Eye = Detect_Eye(rightEye)
        left_Eye = Detect_Eye(leftEye)
        Eye_Rat = (left_Eye + right_Eye) / 2

        # ROUND OF THE VALUE OF AVERAGE MEAN OF RIGHT AND LEFT EYES
        Eye_Rat = round(Eye_Rat, 2)

        # VALUE OF 0.25 (CAN BE CHANGED) WILL DECIDE IF THE EYES ARE CLOSE
        if Eye_Rat < 0.25:
            cv2.putText(frame, "DROWSINESS DETECTED", (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 210), 3)
            cv2.putText(frame, "Alert!!!! WAKE UP DUDE", (50, 450), cv2.FONT_HERSHEY_PLAIN, 2, (21, 56, 212), 3)

            # CALLING THE AUDIO FUNCTION FOR ALERTING THE PERSON
            engine.say("Alert!!!! WAKE UP DUDE")
            engine.runAndWait()

    cv2.imshow("Drowsiness DETECTOR IN OPENCV2", frame)
    key = cv2.waitKey(9)
    if key == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
