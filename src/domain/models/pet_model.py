from dataclasses import dataclass, field
from typing import List
from datetime import datetime

@dataclass
class MedicalHistory:
    date: datetime
    description: str
    veterinarian_id: int

@dataclass
class VaccineRecord:
    vaccine_name: str
    date_given: datetime
    next_due_date: datetime

@dataclass
class Pet:
    id: int
    name: str
    species: str
    breed: str
    age: int
    owner_id: int
    medical_histories: List[MedicalHistory] = field(default_factory=list)
    vaccines: List[VaccineRecord] = field(default_factory=list)

    def add_medical_history(self, history: MedicalHistory):
        self.medical_histories.append(history)

    def add_vaccine_record(self, vaccine: VaccineRecord):
        self.vaccines.append(vaccine)