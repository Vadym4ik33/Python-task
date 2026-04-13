import cv2

# Загружаем "мозг" и картинку
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
img = cv2.imread('people.jpg') # Убедись, что фотка на месте!
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Ищем лица
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# --- ДАЛЬШЕ БУДЕТ МАГИЯ ---
for (x, y, w, h) in faces:
    
    face_img = img[y:y+h, x:x+w]
    
    blurred_face = cv2.GaussianBlur(face_img, (51,51), 30)
    
    img[y:y+h, x:x+w] = blurred_face

cv2.imshow('Censored', img)
cv2.waitKey(0)
