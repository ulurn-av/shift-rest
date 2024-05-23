from fastapi import FastAPI
from src.auth.router import router as router_auth
from src.salary.router import router as router_salary

app = FastAPI()

app.include_router(router_auth)
app.include_router(router_salary)