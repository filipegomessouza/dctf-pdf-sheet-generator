from fields.field import Field
from typing import Optional

class CodeField(Field):
    def regex(self) -> Optional[str]:
        return r'CÓDIGORECEITA:\d+-\d+'

    def format_match(self, match: str) -> str:
        return match.split(':')[-1].strip()

    def formatted_name(self) -> str:
        return 'CÓDIGO RECEITA'
