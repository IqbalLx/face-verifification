import cv2
from numpy import expand_dims, zeros
from scipy.spatial.distance import cosine

import tensorflow as tf
# enabling GPU - uncomment below to run on non-colab with GPU machine
physical_devices = tf.config.experimental.list_physical_devices("GPU")
tf.config.experimental.set_memory_growth(physical_devices[0], enable=True)

from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input


def extract_face(image):
    face_cascade = cv2.CascadeClassifier("src/CascadeFile/face-detect.xml")

    image = image.copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    face_image = zeros((224, 224, 3), dtype='float64')
    try:
        face_coords = face_cascade.detectMultiScale(gray, 1.3, 3)[0]

        x, y, w, h = face_coords
        face_image = image[y:y+h, x:x+w]

        face_image = cv2.resize(face_image, (224, 224), interpolation=cv2.INTER_LINEAR)
        face_image = face_image.astype('float64')
    except:
        pass
    
    return face_image


def get_embedding(model, face_image):
    face_image = preprocess_input(face_image, version=2)
    face_image = expand_dims(face_image, axis=0)
    embedding = model.predict(face_image)
    return embedding


def is_match(first_embedding, second_embedding, thresh=0.4):
    matchness = cosine(first_embedding, second_embedding)
    if matchness <= thresh:
        print("Match")
    else:
        print("Not Match")
    
    print(f"Matchness Cosine Score: {matchness}")

def main():
    model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')

    first_image = get_embedding(model, extract_face(cv2.imread("src/data/ronaldo.jpg")))
    
    cam = cv2.VideoCapture(0)

    while 1:
        _, frame = cam.read()
        frame = cv2.resize(frame, (640, 480))

        second_image = get_embedding(model, extract_face(frame))
        is_match(first_image, second_image)
        
        cv2.imshow("Preview", frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

    is_match(first_image, second_image)

if __name__ == "__main__":
    main()
