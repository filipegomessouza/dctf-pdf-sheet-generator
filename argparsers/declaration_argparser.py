from argparsers.argparser import ArgParser
import argparse
from datetime import datetime, timedelta

class DeclarationArgParser(ArgParser):
    def __init__(self, input_folder: str, output_filename: str):
        self.input_folder = input_folder
        self.output_filename = output_filename

    @staticmethod
    def parse() -> 'DeclarationArgParser':
        parser = argparse.ArgumentParser(description = 'Generate sheet with declaration data')

        parser.add_argument('-f', '--folder', required = False, default = 'pdfs', help = 'Path to folder with all pdfs.')
        parser.add_argument('-o', '--output', required = False, default = 'declarations.xlsx', help = 'Path to output xlsx file.')

        parsed_args = parser.parse_args()

        return DeclarationArgParser(parsed_args.folder, parsed_args.output)