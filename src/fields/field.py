from abc import ABC, abstractmethod
from typing import Optional
import pandas as pd

class Field(ABC):
    __instance: Optional['Field'] = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @abstractmethod
    def regex(self) -> Optional[str]:
        pass

    @abstractmethod
    def format_match(self, match: str) -> str:
        pass

    @abstractmethod
    def formatted_name(self) -> str:
        pass

    def sort_dataframe(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        return dataframe.copy()