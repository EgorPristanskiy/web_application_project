import cv2
from threading import Lock


class ImageProcessing(object):
    def __init__(self, image_path=None):
        self.__original_image = None
        if image_path:
            self.__original_image = cv2.imread(image_path)
        self.__mutex = Lock()

    @staticmethod
    def encode_img(img):
        return cv2.imencode('jpg', img).tobytes()

    def image_stream_thread(self):
        while True:
            with self.__mutex:
                yield self.encode_img(self.__original_image.copy())

    def update_image(self, path_to_image):
        with self.__mutex:
            self.__original_image = cv2.imread(path_to_image)