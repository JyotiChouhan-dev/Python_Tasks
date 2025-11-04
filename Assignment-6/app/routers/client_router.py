import csv
import io
import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from fastapi.responses import StreamingResponse
from app.core.config import db
from app.schemas.client_schema import ClientCreate

router = APIRouter(prefix="/clients", tags=["Clients"])


# Upload CSV and save data to DB
@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are allowed")

    content = await file.read()
    decoded = content.decode("utf-8")
    reader = csv.DictReader(io.StringIO(decoded))

    clients = []
    for row in reader:
        if not row.get("name") or not row.get("email"):
            continue  # skip invalid rows

        clients.append(
            {
                "name": row["name"],
                "email": row["email"],
                "about": row.get("about", ""),
            }
        )

    # Insert into database
    for client in clients:
        await db.client.create(data=client)

    return {"message": f"{len(clients)} records added successfully"}


# Manually add a client via JSON
@router.post("/add")
async def add_client(client: ClientCreate):
    new_client = await db.client.create(data=client.dict())
    return new_client


# Export clients as CSV or XLSX
@router.get("/export")
async def export_clients(
    file_type: str = Query("csv", enum=["csv", "xlsx"]),
    limit: int = Query(None, description="Limit number of rows to export"),
):
    clients = await db.client.find_many(take=limit)

    if not clients:
        raise HTTPException(status_code=404, detail="No clients found")

    df = pd.DataFrame(clients)

    if file_type == "csv":
        stream = io.StringIO()
        df.to_csv(stream, index=False)
        response = StreamingResponse(
            iter([stream.getvalue()]),
            media_type="text/csv",
            headers={"Content-Disposition": "attachment; filename=clients.csv"},
        )
    else:
        stream = io.BytesIO()
        with pd.ExcelWriter(stream, engine="xlsxwriter") as writer:
            df.to_excel(writer, index=False)
        stream.seek(0)
        response = StreamingResponse(
            stream,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": "attachment; filename=clients.xlsx"},
        )

    return response
