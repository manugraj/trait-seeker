from pydantic import BaseModel


class Traits(BaseModel):
    extraversion: str
    neuroticism: str
    agreeableness: str
    conscientiousness: str
    openness: str


class TraitData(BaseModel):
    traits: Traits
    dominant: str


class TextMetadata(BaseModel):
    num_words: int
    common_words: dict


class TraitsResponse(BaseModel):
    trait_data: TraitData
    text_data: TextMetadata
