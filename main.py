from src.builders.declaration_builder import DeclarationBuilder
from src.pdf_readers.pdf_reader import PdfReader
from src.pdf_readers.py_mu_pdf_reader import PyMuPdfReader
import os
from typing import List
from src.argparsers.declaration_argparser import DeclarationArgParser

declaration_arg_parser: DeclarationArgParser = DeclarationArgParser.parse()
pdf_reader: PdfReader = PyMuPdfReader()
declaration_manager = DeclarationBuilder(pdf_reader)

filenames: List[str] = [filename for filename in os.listdir(declaration_arg_parser.input_folder) if filename.endswith('.pdf')]

for filename in filenames:
    path: str = os.path.join(declaration_arg_parser.input_folder, filename)
    declaration_manager.append_declarations_from_pdf(path)

declaration_manager\
    .sort_by_period()\
    .save_excel(declaration_arg_parser.output_filename)

