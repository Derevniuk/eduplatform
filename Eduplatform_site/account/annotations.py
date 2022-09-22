from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class UserAnnotation:
    first_name: str
    last_name: str
    email: str
