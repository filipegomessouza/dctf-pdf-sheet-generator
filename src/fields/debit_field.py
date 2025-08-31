from src.fields.field import Field
from typing import Optional

class DebitField(Field):
    def regex(self) -> Optional[str]:
        return r'DÉBITOAPURADO(?:[0-9]|\.)+,\d{2}'

    def format_match(self, match: str) -> str:
        return match.split('DÉBITOAPURADO')[-1].strip()

    def formatted_name(self) -> str:
        return 'DÉBITO APURADO'
