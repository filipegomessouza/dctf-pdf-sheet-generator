from pdf_readers.pdf_reader import PdfReader
import fitz

class PyMuPdfReader(PdfReader):
    def get_text(self, path: str) -> str:
        pdf = fitz.open(path)
        text: str = ''

        for page in pdf:
            text += page.get_text() + '\n'

        return text
