from fastapi import FastAPI, File, UploadFile
import pytesseract
import shutil

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # tesseract path
app = FastAPI()


@app.post('/ocr')
def ocr(image: UploadFile = File(...)):
    filepath = 'textfile'
    with open(filepath, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)

    return pytesseract.image_to_string(filepath, lang='eng')
