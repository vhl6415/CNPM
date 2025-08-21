from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

@dataclass
class Admission:
    id: int
    pet_id: int
    room_id: int
    admitted_at: datetime
    discharged_at: Optional[datetime] = None
    attending_veterinarian_id: int = 0
    treatment_notes: List[str] = field(default_factory=list)

    def add_treatment_note(self, note: str):
        self.treatment_notes.append(note)

    def discharge(self, discharge_time: datetime):
        self.discharged_at = discharge_time