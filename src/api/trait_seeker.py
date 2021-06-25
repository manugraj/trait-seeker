from fastapi import APIRouter

from src.core.trait_seeker import complete, seek, text_metadata
from src.model import TraitsResponse, TraitData, TextMetadata

router = APIRouter(prefix="/api/v1/text")


@router.post(path="/analyse", tags=["Text Analysis"], response_model=TraitsResponse, summary="Analyse Trait & metadata")
def complete_data(text_data: str):
    return complete(text_data)


@router.post(path="/traits", tags=["Text Analysis"], response_model=TraitData, summary="Analyse traits")
def text(text_data: str):
    return seek(text_data)


@router.post(path="/metadata", tags=["Text Analysis"], response_model=TextMetadata, summary="Analyse metadata")
def text(text_data: str):
    return text_metadata(text_data)
