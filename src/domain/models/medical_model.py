from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class MedicalRecord:
    id: int
    pet_id: int
    veterinarian_id: int
    visit_date: datetime
    symptoms: str
    diagnosis: str
    treatment: str
    notes: Optional[str] = None

    def update_treatment(self, new_treatment: str):
        self.treatment = new_treatment

    def add_notes(self, additional_notes: str):
        if self.notes:
            self.notes += "\n" + additional_notes
        else:
            self.notes = additional_notes