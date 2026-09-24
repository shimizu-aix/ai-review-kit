from abc import ABC, abstractmethod
from enum import StrEnum

from pydantic import BaseModel


class Severity(StrEnum):
    ERROR = "error"
    WARNING = "warning"


class Finding(BaseModel):
    rule_id: str
    severity: Severity
    file: str
    line: int
    message: str


class Rule(ABC):
    rule_id: str
    severity: Severity

    @abstractmethod
    def check(self, source: str, filename: str) -> list[Finding]:
        """ソースコードを解析し、検出結果を返す。"""