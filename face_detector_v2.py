import os
import face_recognition
import cv2
import requests
import bs4

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
            imag = cv2.imread(image_path)
            for x, y, w, z in imagen_location:
                cv2.rectangle(imag, (z, x), (y, w), (0, 0, 255), 2)
            viewImage(imag, 'image')
        else:
            imag = cv2.imread(image_path)
            viewImage(imag, 'image')
            print(f'No faces found in file: {image}')

def parcer(link):
    html = requests.get(link).text
    soup = bs4.BeautifulSoup(html, 'html5lib')
    all_image = soup.find_all('img')
    downloaded_files = set()
    for tag in all_image:
        url = tag.get('data-cover', tag.get('src'))
        if url:
            filename = url.split('/')[-1]
            filename = f'photos/{filename}'
            downloaded_files.add(filename)
            with open(filename, 'wb') as f:
                f.write(requests.get(url).content)


path ='C://PycharmProjects/venv/photos/'
link = 'https://woman.rambler.ru/stars/44138341-komu-holostyak-pomog-vygodno-vyyti-zamuzh/'
parcer(link)
face_detector(path)
