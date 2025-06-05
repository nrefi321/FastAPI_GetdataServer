# 🚀 FastAPI Getdata Server

A lightweight and efficient FastAPI-based backend for receiving and processing uploaded data and files. This project is designed for flexibility, and it runs on both **Jetson Nano** and **Windows** systems.

---

## 📌 Features

- Receive uploaded files via REST API
- Header/token validation
- SQLAlchemy ORM for database interaction
- CORS middleware included
- Background task support

---

## ⚙️ Requirements

- Python >= 3.6
- pip

---

## 🔧 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/nrefi321/FastAPI_GetdataServer.git
   cd FastAPI_GetdataServer
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, create one with the following:

   ```txt
   fastapi>=0.75.0
   uvicorn[standard]>=0.17.0
   sqlalchemy>=1.4.0
   starlette>=0.17.0
   ```

---

## 🛠️ Usage

Run the FastAPI server:

```bash
uvicorn main:app --reload
```

- Open in browser: [http://localhost:8000](http://localhost:8000)
- API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📂 Project Structure

```
FastAPI_GetdataServer/
├── main.py
├── checklist/         
│   └── checklist.py
│   └── checklistdb.py
│   └── checklistmodel.py
├── requirements.txt
└── README.md
```

---

## 📬 Contact

For access to hidden/private repositories or collaboration inquiries, contact me via email:

📧 **pontip_solo@hotmail.com**

---
