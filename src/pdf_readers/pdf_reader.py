from abc import ABC, abstractmethod

class PdfReader(ABC):
    @abstractmethod
    def get_text(self, path: str) -> str:
        pass
