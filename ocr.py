import pytesseract
from PIL import Image

def extract_text(image_path):
    # Load the image
    img = Image.open(image_path)
    # Use pytesseract to perform OCR
    extracted_text = pytesseract.image_to_string(img, lang='eng+hin')
    return extracted_text
