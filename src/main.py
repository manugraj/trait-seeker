from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from loguru import logger

from src.api.trait_seeker import router as main_router
from src.config import SystemConfig

logger.add("./logs/trait-seeker.log", rotation="5 MB")
logger.info("Initializing application : trait-seeker")

app = FastAPI(
    title="Trait-Seeker",
    description="Find personality traits from text",
    version="0.1.0"
)

app.include_router(main_router)


@app.on_event("startup")
def startup():
    logger.info("Loading configuration from env")
    SystemConfig.load()


@app.on_event("shutdown")
def startup():
    logger.info("System shutdown initiated")


@app.get("/", include_in_schema=False)
async def redirect():
    return RedirectResponse("/docs")

