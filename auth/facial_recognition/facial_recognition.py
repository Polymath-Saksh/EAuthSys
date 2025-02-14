import cv2
import dlib
import numpy as np

class FacialRecognition:
    def __init__(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        self.recognizer = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")
        self.known_faces = []

    def capture_face(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.detector(gray)

            for face in faces:
                landmarks = self.predictor(gray, face)
                face_descriptor = self.recognizer.compute_face_descriptor(frame, landmarks)
                self.known_faces.append(np.array(face_descriptor))

            cv2.imshow("Capture Face", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def verify_face(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.detector(gray)

            for face in faces:
                landmarks = self.predictor(gray, face)
                face_descriptor = self.recognizer.compute_face_descriptor(frame, landmarks)
                face_descriptor = np.array(face_descriptor)

                for known_face in self.known_faces:
                    distance = np.linalg.norm(known_face - face_descriptor)
                    if distance < 0.6:
                        print("Face Verified")
                        return True

            cv2.imshow("Verify Face", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        return False
