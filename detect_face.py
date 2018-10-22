import cv2


has_cascade = 'opencv_files/haarcascade_frontalface_default.xml'

def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)


def detect_face(capture):
    ret, frame = capture.read()

    while ret:
        ret, frame = capture.read()

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(has_cascade)
        faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5)

        cont = 0
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(frame, str(cont), (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
            cont += 1

        cv2.imshow('video captured', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def main():
    capture = cv2.VideoCapture(0)
    detect_face(capture)


if __name__ == '__main__':
    main()
