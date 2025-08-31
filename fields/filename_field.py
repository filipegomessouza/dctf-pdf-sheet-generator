from fields.field import Field
from typing import Optional

class FilenameField(Field):
    def regex(self) -> Optional[str]:
        return None

    def format_match(self, match: str) -> str:
        return match

    def formatted_name(self) -> str:
        return 'ARQUIVO DE ORIGEM'
