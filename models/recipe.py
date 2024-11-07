from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass(frozen=True)
class Recipe:
    name: str
    ingredients: List[Tuple[str, int]]
    prep_time: int  # minutes
    difficulty: str
