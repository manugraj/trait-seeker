from src.core.model import PretrainedModel
from src.core.predict import *
from loguru import logger

from src.model import TextMetadata, TraitData, Traits, TraitsResponse


def seek(text_data):
    try:
        traits = ['Extraversion', 'Neuroticism', 'Agreeableness', 'Conscientiousness', 'Openness']
        prediction = Predict().run(text_data, model_name=PretrainedModel.Personality_traits_NN.value)
        highest_probability = prediction[0].tolist()
        return TraitData(traits=Traits(extraversion=highest_probability[0],
                                       neuroticism=highest_probability[1],
                                       agreeableness=highest_probability[2],
                                       conscientiousness=highest_probability[3],
                                       openness=highest_probability[4]),
                         dominant=traits[highest_probability.index(max(highest_probability))].lower())
    except Exception as exc:
        raise exc
        logger.error("Exception while processing, {}", exc)
        return None


def text_metadata(text_data):
    words = tokenize.word_tokenize(text_data)
    common_words = FreqDist(words).most_common(100)
    num_words = len(text_data.split())
    return TextMetadata(common_words=common_words, num_words=num_words)


def complete(text_data: str) -> TraitsResponse:
    return TraitsResponse(trait_data=seek(text_data), text_data=text_metadata(text_data))

