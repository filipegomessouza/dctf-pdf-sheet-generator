from fields.field import Field
from typing import Optional

class PeriodField(Field):
    def regex(self) -> Optional[str]:
        return r'PERÍODODEAPURAÇÃO:(?:Janeiro|Fevereiro|Março|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro)/\d{4}DÉBITO'

    def format_match(self, match: str) -> str:
        return match.split(':')[-1].replace('DÉBITO', '').strip()

    def formatted_name(self) -> str:
        return 'PERÍODO DE APURAÇÃO'
