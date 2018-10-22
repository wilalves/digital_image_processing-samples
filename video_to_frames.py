import cv2


def video_to_frames(video_filename):
    """Extract frames from video"""

    directory_name = "frames/"
    cap = cv2.VideoCapture(video_filename)
    success, image = cap.read()
    count = 0
    while success:
        cv2.imwrite(directory_name + str(count) + '.jpg', image)
        success, image = cap.read()
        count += 1

    return "OK!"


if __name__ == '__main__':
    file_video = './videos/dzb.mp4'
    video_to_frames(file_video)
