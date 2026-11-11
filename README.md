# api-agrotech

A FastAPI study project for building a small agricultural credit API.

## Endpoints

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/api/agroscr` | Create an AgroSCR record |
| `GET` | `/api/agroscr` | List all records |
| `GET` | `/api/agroscr/{id}` | Find a record by ID |
| `PUT` | `/api/agroscr/{id}` | Update a record by ID |
| `DELETE` | `/api/agroscr/{id}` | Delete a record by ID |

## Run locally

```sh
pip install fastapi uvicorn sqlalchemy
uvicorn main:app --reload
```

The API uses SQLAlchemy with a local SQLite database (`db.sqlite3`).
