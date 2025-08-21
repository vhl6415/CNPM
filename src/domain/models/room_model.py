from dataclasses import dataclass

@dataclass
class Room:
    id: int
    room_number: str
    room_type: str  # vd: "standard", "icu", "isolation"
    capacity: int
    is_available: bool = True

    def occupy(self):
        self.is_available = False

    def release(self):
        self.is_available = True