import cv2


def detect_face(capture):
    ret, frame = capture.read()

    while ret:
        ret, frame = capture.read()
        cv2.imshow('video captured', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


def main():
    capture = cv2.VideoCapture(0)
    detect_face(capture)


if __name__ == '__main__':
    main()
