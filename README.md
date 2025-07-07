# BentoSpacy
Serving a Bento with a Spacy model.
This bento also showcases to serve a custom generated pipelines

## Run locally
Generate the custom pipeline and package it with `bentoml.models`.
```
python create_model.py
```

Serve locally
```
bentoml serve
```

## Deploy to BentoCloud
```
bentoml deploy .
```
Spacy Model can be downloaded as a python package, so we include the wheel file as part of the `requirements.txt`.

