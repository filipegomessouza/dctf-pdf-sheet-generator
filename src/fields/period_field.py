from src.fields.field import Field
from typing import Optional
import pandas as pd
from typing import Dict

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

    def sort_dataframe(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        formatted_name = self.formatted_name()

        if formatted_name not in dataframe.columns:
            return dataframe

        month_by_period: Dict[str, int] = {
            'Janeiro': 1,
            'Fevereiro': 2,
            'Março': 3,
            'Abril': 4,
            'Maio': 5,
            'Junho': 6,
            'Julho': 7,
            'Agosto': 8,
            'Setembro': 9,
            'Outubro': 10,
            'Novembro': 11,
            'Dezembro': 12,
            '1º Trimestre': 1,
            '1° Trimestre': 1,
            '2º Trimestre': 4,
            '2° Trimestre': 4,
            '3º Trimestre': 7,
            '3° Trimestre': 7,
            '4º Trimestre': 10,
            '4° Trimestre': 10,
        }

        return dataframe.sort_values(
            formatted_name,
            key = lambda col: pd.to_datetime(
                col.apply(lambda period: f"1/{month_by_period[period.split('/')[0]]}/{period.split('/')[1]}")
            ),
        )
