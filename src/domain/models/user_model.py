from dataclasses import dataclass
from enum import Enum

class UserRole(Enum):
    CUSTOMER = "customer"
    STAFF = "staff"
    VETERINARIAN = "veterinarian"
    ADMIN = "admin"

@dataclass
class User:
    id: int
    username: str
    email: str
    hashed_password: str
    role: UserRole

    def check_password(self, password: str) -> bool:
        # Gia lap su dung bcrypt / hashlib
        return password == self.hashed_password