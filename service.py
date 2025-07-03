from __future__ import annotations

import bentoml
import spacy


@bentoml.service(
  traffic={'timeout': 30},
  resources={'cpu': 1, 'memory': '4Gi'},
  image=bentoml.images.Image(python_version='3.11').requirements_file('requirements.txt').uv_lock(),
)
class Service:
  hf = bentoml.models.HuggingFaceModel('spacy/en_core_web_sm')

  def __init__(self):
    self.model = spacy.load(self.hf)

  @bentoml.api
  def analyze(self, text: str) -> list[tuple[str, str]]:
    doc = self.model(text)
    return [(w.text, w.pos_) for w in doc]
