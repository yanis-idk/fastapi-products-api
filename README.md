# FastAPI Products API

A simple REST API built with FastAPI to manage products.

## Features
- Full CRUD (GET, POST, DELETE)
- Pydantic validation
- Error handling (404)
- Request logging middleware
- CORS enabled

## Install
pip install fastapi uvicorn pydantic

## Run
uvicorn main:app --reload

## Endpoints
- GET /products → list all products
- GET /products/{id} → get one product
- POST /products → create a product
- DELETE /products/{id} → delete a product

## Testing
Go to http://127.0.0.1:8000/docs