from abc import ABC, abstractmethod
from typing import List

class PdfReader(ABC):
    @abstractmethod
    def get_text(self, path: str) -> str:
        pass
