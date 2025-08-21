# Pet Health Care

This project is designed following the principles of Clean Architecture, ensuring a clear separation of system layers for better scalability and maintainability. Below is an overview of the project's structure and its components.


## Actor
- Customer
- Staff
- Veterinarian
- Admin


## Main Features
1. Customer
- Quan li danh sach pets
- Xem va cap nhat thong tin pets
- Lich su y te
- Booking
- Payment
- Cancel booking:
    + Truoc 7 ngay: Hoan 100%
    + Tu 3-6 ngay: Hoan 75%
    + Duoi 3 ngay: Khong hoan tien
- Dua pets di kham (checkin)
- Thanh toan chi phi phat sinh
- Danh gia sau moi lan kham
- Theo doi qua trinh pet nhap vien (luu chuong)

2. Staff
- Quan li chuong trong he thong
- Quan li booking:
    + Xu li yeu cau Huy Booking
    + Hoan tien neu do he thong huy
- Quan li pets luu chuong
- Update trang thai pets nhap vien
- Xep lich bac si khach chua Book
- Xep lich bac si cham soc pet nhap vien

3. Veterinarian
- Kham cho pet va ghi nhan ho so dieu tri
- Theo doi va cham soc pet trong thoi gian nhap vien

4. Admin
- Quan li acc User (Cus,Staff, Vet)
- Quan li cau hinh he thong (chuong, lich lam viec, services,...)
- Thong ke doanh thu ngay, tuan, thang


## Directory Structure

- **migrations/**: File di chuyen co so du lieu (database migrations)
- **scripts/**: Script quan li he thong, vi du nhu `run_database.sh` de chay PostgreSQL.
- **api/**: Giao tiep API
  - **controllers/**: Xu li yeu cau tu User
  - **schemas/**: Kiem tra va tuan tu hoa du lieu (Marshmallow)
  - **middleware.py**: Middleware xu li requests va responses.
  - **responses.py**: Xu li tra ve API
  - **requests.py**: Chuan hoa du lieu gui den API

- **infrastructure/**: Cac thanh phan tuong tac voi he thong ben ngoai
  - **services/**: Dich vu ben thu ba nhu Thanh toan online,...
  - **databases/**: Ket noi va khoi tao du lieu
  - **repositories/**: Truy xuat du lieu
  - **models/**: Mo hinh du lieu

- **domain/**: Chua logic nghiep vu cot loi
  - **exceptions.py**: Ngoai le tuy chinh cho web
  - **models/**: Mo hinh nghiep vu (business models)

- **services/**: Tuong tac voi nghiep vu (domain) (business logic).
- **app.py**: Khoi chay
- **config.py**: Cau hinh web
- **cors.py**: Cau hinh Cross-Origin Resource Sharing (CORS)
- **error_handler.py**: Dinh nghia logic xu li loi
- **logging.py**: Cau hinh logging (ghi log)


## Getting Started
De khoi chay du an, ban can:
1. Cai dat thu vien can thiet (xem file requirements.txt neu co)
2. Thiet lap cau hinh he thong (config.py).
3. Khoi dong bang lenh: python .\src\app.py


## Contributing
Chung toi luon chao don nhung dong gop! Vui long tuan thu quy trinh dong gop trong tai lieu du an.