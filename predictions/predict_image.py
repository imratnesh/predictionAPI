from PIL import Image
import pytesseract
def parse(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return {'file':filename, 'result':text}