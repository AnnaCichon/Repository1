try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def czytanie_tekstu(plik):
    return pytesseract.image_to_string(Image.open(plik))