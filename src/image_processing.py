import cv2
import imutils
from threading import Lock


class ImageProcessing(object):
    def __init__(self, image_path=None):
        print("image_path")
        self.__original_image = None
        if image_path:
            self.__original_image = cv2.imread(image_path)
        self.__mutex = Lock()
        self.__rotate_angle = 0

    def encode_img(self, img):
        show_img = img.copy().astype('int')
        encode_return_code, image_buffer = cv2.imencode('.jpg', show_img)
        image_bytes = image_buffer.tobytes()
        return (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + image_bytes + b'\r\n\r\n')

    def image_stream_thread(self):
        while True:
            with self.__mutex:
                yield self.encode_img(self.__original_image.copy())

    def update_image(self, path_to_image):
        with self.__mutex:
            self.__original_image = cv2.imread(path_to_image)

    def set_rotate_angle(self, colors_value):
        with self.__mutex:
            self.__rotate_angle = colors_value.copy()
