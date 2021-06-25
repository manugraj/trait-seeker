# Trait-seeker

A straight-forward tool to identify Big5 personality traits from models. Models can be trained externally and made available in platform or use the platform capabilities to build model.


## Stack
- Poetry
- Tensorflow
- Scipy
- Scikit-learn
- Keras
- Numpy
- Nltk
- Gensim

## Other data
- 300-dimension Word2Vec


## API

- /api/v1/text/traits

```
{
  "traits": {
    "extraversion": "0.21699446439743042",
    "neuroticism": "0.0937899574637413",
    "agreeableness": "0.24144093692302704",
    "conscientiousness": "0.19555066525936127",
    "openness": "0.252223938703537"
  },
  "dominant": "openness"
}
```

## References
- Building on the work by `https://github.com/maelfabien/Multimodal-Emotion-Recognition`