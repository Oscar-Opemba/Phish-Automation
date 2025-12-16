from dataclasses import dataclass
from typing import List


@dataclass
class Role:
name: str
risk_profile: str # e.g. low, medium, high


@dataclass
class Campaign:
name: str
roles: List[Role]
duration_days: int
