from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from fastapi import Request
import time
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"{request.method} {request.url} - {duration:.2f}s")
    return response

fake_db = [
    {"id": 0, "name": "apple", "price": 20},
    {"id": 1, "name": "orange", "price": 15},
    {"id": 2, "name": "banana", "price": 36.7}
]
class Products(BaseModel):
    name: str
    price: float

@app.get("/products")
def show_products():
    return fake_db

@app.get("/products/{id}")
def product_id(id : int):
    if id < len(fake_db):
        return fake_db[id]
    raise HTTPException(status_code=404, detail="not found")

@app.post("/products",status_code=201)
def products_info(info : Products):
    fake_db.append({"id": len(fake_db), "name": info.name, "price": info.price})
    return {"message": "created"}

@app.delete("/products/{id}")
def product_id(id : int):
    if id < len(fake_db):
        del fake_db[id]
        return {"message": "deleted"}
    raise HTTPException(status_code=404 , detail="product not found!")




