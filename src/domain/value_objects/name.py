from dataclasses import dataclass

@dataclass(frozen=True)
class Name:
    value: str

    def __post_init__(self):
        if not self.value or not self.value.strip():
            raise ValueError("Name cannot be empty")
