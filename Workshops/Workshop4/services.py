from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select
from sqlalchemy.orm import sessionmaker

"""
Deleting one "app = FastAPI()"
"""
app = FastAPI()

"""
Implementation of origins and middleware
"""
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""
Creation of the class
"""
class Product(BaseModel):
    id: int
    name: str
    description: str

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/public"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("description", String),
)

@app.get("/hello_ud")
def hello_ud():
    return "Welcome to UD!"

@app.get("/get_products")
def get_products():
 query = products.select()
 result = session.execute(query)
 products = result.fetchall()
 return products
    
"""
change in endpoint name, and addition of exceptions
"""
@app.post("/create_products")
def create_product(product: Product):
    try:
        query = products.insert().values(
            id=product.id, name=product.name, description=product.description
        )
        session.execute(query)
        session.commit()
        return {"message": "Product created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

"""
port change
"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
