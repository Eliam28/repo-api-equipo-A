from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ODOO_URL: str
    ODOO_DB: str
    ODOO_USER: str
    ODOO_PASSWORD: str
    PRESTASHOP_URL: str
    API_KEY: str


    class Config:
        env_file = ".env"

settings = Settings()