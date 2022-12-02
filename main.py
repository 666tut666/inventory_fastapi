from fastapi import FastAPI
from db.database import engine
from db.models import Base
from config.db_config import setting
from routers import admin
from routers import staff
from routers import items
from webapps.routers import items as web_items, users as web_users, auth as web_auth
from fastapi.staticfiles import StaticFiles


Base.metadata.create_all(bind=engine)
app = FastAPI(
    title=setting.TITLE,
    description=setting.DESCRIPTION,
    version=setting.VERSION,
    contact={
        "name": setting.NAME,
        "email": setting.EMAIL
    }
)

app.mount("/static", StaticFiles(directory="static"), name="static")
    #mount the path for img


app.include_router(admin.router)
app.include_router(staff.router)
app.include_router(items.router)
app.include_router(web_items.router)
app.include_router(web_users.router)
app.include_router(web_auth.router)


