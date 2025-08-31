from abc import ABC, abstractmethod
from typing import List
from datetime import datetime
import argparse

class ArgParser(ABC):
    @staticmethod
    @abstractmethod
    def parse() -> 'ArgParser':
        pass

    @staticmethod
    def _valid_true_strings() -> List[str]:
        return ['y', 'yes', '1', 'true', 't']

    @staticmethod
    def _valid_false_strings() -> List[str]:
        return ['n', 'no', '0', 'false', 'f']

    @staticmethod
    def _validate_date(date: str) -> str:
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return date

        except ValueError:
            raise argparse.ArgumentTypeError('Date must be in format YYYY-MM-DD.')

    @staticmethod
    def _validate_bool(value: str) -> bool:
        value = value.lower()

        true_strings = ArgParser._valid_true_strings()
        if value in true_strings:
            return True

        false_strings = ArgParser._valid_false_strings()
        if value in false_strings:
            return False

        raise argparse.ArgumentTypeError(f'Invalid bool. Valid values are {true_strings + false_strings}.')
