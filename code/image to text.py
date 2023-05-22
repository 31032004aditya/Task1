import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

def load_image(file_path):
    image = cv2.imread(file_path)
    return image

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply additional preprocessing steps if needed, such as thresholding or denoising
    return gray

def extract_text(image):
    # Convert the image to PIL format
    pil_image = Image.fromarray(image)

    # Perform OCR using PyTesseract
    # print(pytesseract.image_to_string(pil_image))
    text = pytesseract.image_to_string(pil_image)

    return text


file_path = 'C:/Users/adity/Downloads/Data/Data/Task1/2.jpg'
image = load_image(file_path)
processed_image = preprocess_image(image)
text = extract_text(image)

print(text)