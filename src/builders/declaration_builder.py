from src.pdf_readers.pdf_reader import PdfReader
from src.fields.field import Field
from src.fields.code_field import CodeField
from src.fields.debit_field import DebitField
from src.fields.period_field import PeriodField
from src.fields.filename_field import FilenameField
from typing import List, Dict
import re
import pandas as pd
import os
import json

class DeclarationBuilder():
    def __init__(self, pdf_reader: PdfReader):
        self.pdf_reader: PdfReader = pdf_reader
        self.dataframe: pd.DataFrame = self.__empty_dataframe()

    def __fields(self) -> List[Field]:
        return [
            CodeField(),
            PeriodField(),
            DebitField(),
        ]

    def __empty_dataframe(self) -> pd.DataFrame:
        columns: List[str] = [field.formatted_name() for field in self.__fields() + [FilenameField()]]

        return pd.DataFrame(columns = columns)

    def append_declarations_from_pdf(self, path: str) -> 'DeclarationBuilder':
        text = self.pdf_reader.get_text(path)
        declaration: Dict[str, List[str]] = {}
        declarations_size: int = 0

        for field in self.__fields():
            formatted_name = field.formatted_name()

            declaration[formatted_name] = [field.format_match(match) for match in re.findall(field.regex(), text)]
            declarations_size = len(declaration[formatted_name])

        declaration[FilenameField().formatted_name()] = declarations_size * [os.path.basename(path)]

        try:
            self.dataframe = pd.concat([self.dataframe, pd.DataFrame(declaration)], ignore_index = True)
        except Exception as exception:
            self.__print_out_of_standard_message(path, declaration)
        finally:
            return self

    def __print_out_of_standard_message(self, path: str, declaration: Dict[str, List[str]]):
        print(f'Ocorreu um erro ao ler o arquivo {path}.')
        print(f'Os dados identificados foram os seguintes:')
        print(json.dumps(declaration, indent = 2, ensure_ascii = False))

    def sort_by_period(self) -> 'DeclarationBuilder':
        self.dataframe = PeriodField().sort_dataframe(self.dataframe)

        return self

    def save_excel(self, path: str) -> 'DeclarationBuilder':
        self.dataframe.to_excel(path, index = False)

        return self
