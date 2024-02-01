
import face_recognition
import cv2
import numpy as np
from datetime import datetime

# Load images and names of students
# Replace the paths and names with your dataset
known_face_encodings = []
known_face_names = []

# Example:
# known_face_encodings.append(face_recognition.face_encodings(face_recognition.load_image_file("student1.jpg"))[0])
# known_face_names.append("Student 1")

# Initialize variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# Initialize attendance log
attendance_log = {}

# Open webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture each frame from the webcam
    ret, frame = video_capture.read()

    # Resize the frame to speed up face recognition
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (OpenCV) to RGB color (face_recognition)
    rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # Process every other frame to speed up face recognition
    if process_this_frame:
        # Find all face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Check if the face matches any known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If a match is found, use the name of the known face
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

            # Mark attendance
            if name != "Unknown":
                if name not in attendance_log:
                    attendance_log[name] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a rectangle around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw the name below the face
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
video_capture.release()
cv2.destroyAllWindows()

# Print the attendance log
print("\nAttendance Log:")
for student, timestamp in attendance_log.items():
    print(f"{student}: {timestamp}")
