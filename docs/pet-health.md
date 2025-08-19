# Architecture

```bash
    ├── migrations
    ├── scripts
    │   └── run_database.sh  #Khoi tao co so du lieu
    ├── src
    │   ├── api
    │   │   ├── controllers
    │   │   │   └── ...      #Xu li cac lich kham, xem ho so pet
    │   │   ├── schemas
    │   │   │   └── ...      #Xac nhan lich hen va phan hoi
    │   │   ├── middleware.py    #Kiem tra xac thuc, login
    │   │   ├── responses.py     #Phan hoi
    │   │   └── requests.py      #Xu li dau vao
    │   ├── infrastructure
    │   │   ├── services
    │   │   │   └── ...          #Thanh toan online
    │   │   ├── databases
    │   │   │   └── ...          #Ket noi co so du lieu
    │   │   ├── repositories
    │   │   │   └── ...          #CRUP(Create/Read/Update/Delete) pets, lich kham
    │   │   └── models
    │   │   │   └── ...          #User, Pets, Appointment(lich hen),….
    │   ├── domain
    │   │   ├── exceptions.py    #ERROR: Thieu lich su y te, lich hen trung,….
    │   │   ├── models
    │   │   │   └── ...          #Pet Health Records, Booking,…
    │   ├── services
    │   │    └── ...             #Tuong tac voi domain (logic kinh doanh)
    │   ├── app.py               #Khoi dong web
    │   ├── config.py            #Cau hinh chung
    │   ├── cors.py              #Cau hinh Cors
    │   ├── error_handler.py     #Xu li loi
    │   └── logging.py           #Cau hinh ghi log
```
## Domain Layer

## Service Layer

## Infrastructure Layer