import os
import face_recognition
import cv2

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def face_detector(path):
    images = os.listdir(path)
    for image in images:
        image_path = path + image
        face_image = face_recognition.load_image_file(image_path)
        imagen_location = face_recognition.face_locations(face_image)
        if imagen_location != []:
            image = cv2.imread(image_path)
            for x, y, w, z in imagen_location:
                cv2.rectangle(image, (z, x), (y, w), (0, 0, 255), 1)
            viewImage(image, 'image')
        else:
            print(f'No faces found in file: {image}')




path ='path'
face_detector(path)
