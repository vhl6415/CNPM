from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class BookingStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

@dataclass
class Booking:
    id: int
    pet_id: int
    customer_id: int
    veterinarian_id: int  # 0 or None if not assigned yet
    booking_datetime: datetime
    status: BookingStatus
    payment_amount: float
    payment_status: bool

    def cancel_booking(self, current_date: datetime) -> float:
        """
        Truoc 7 ngay: Hoan 100%
        Tu 3 den 6 ngay: hoan 75%
        Duoi 3 ngay: Khong hoan tien
        """
        delta = (self.booking_datetime.date() - current_date.date()).days
        if delta >= 7:
            refund = self.payment_amount
        elif 3 <= delta < 7:
            refund = self.payment_amount * 0.75
        else:
            refund = 0.0
        self.status = BookingStatus.CANCELLED
        return refund