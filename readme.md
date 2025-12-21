expense-system/
│
├── app/
│   ├── main.py
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │   └── dependencies.py
│   │
│   ├── auth/
│   │   ├── router.py
│   │   ├── service.py
│   │   └── schemas.py
│   │
│   ├── users/
│   ├── expenses/
│   ├── policies/
│   ├── approvals/
│   ├── analytics/
│   │
│   ├── models/
│   │   └── base.py
│   │
│   └── db/
│       ├── session.py
│       └── init_db.py
│
├── alembic/
├── requirements.txt
└── README.md

fastapi
uvicorn
sqlalchemy
pymysql
python-jose
passlib[bcrypt]
pydantic

