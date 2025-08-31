from fields.field import Field
from typing import Optional

class PeriodField(Field):
    def regex(self) -> Optional[str]:
        return r'PERÍODODEAPURAÇÃO:[^/]+/\d{4}DÉBITO'

    def format_match(self, match: str) -> str:
        formatted_match: str = match.split(':')[-1].replace('DÉBITO', '').strip()

        if 'Trimestre' in formatted_match:
            quarter_number, year = formatted_match.split('Trimestre/')

            return f'{quarter_number} Trimestre/{year}'

        return formatted_match

    def formatted_name(self) -> str:
        return 'PERÍODO DE APURAÇÃO'
