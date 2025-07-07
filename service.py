from __future__ import annotations

import bentoml
import spacy
from pathlib import Path
import sys
import importlib.util

EXAMPLE_INPUT = "Apple is hiring Python developers. Google prefers Go programming."

@bentoml.service(
  traffic={'timeout': 30},
  resources={'cpu': 1, 'memory': '4Gi'},
  image=bentoml.images.Image(python_version='3.11').requirements_file('requirements.txt').uv_lock(),
)
class Service:
  hf = bentoml.models.HuggingFaceModel('spacy/en_core_web_sm')
  pipeline_ref = bentoml.models.get("custom_spacy_pipeline:latest") # This is the custom pipeline we created

  def __init__(self):
    # Base pipeline example
    self.model = spacy.load(self.hf)
    
    # Custom pipeline example
    self.pipeline = self._load_pipeline()

  def _load_pipeline(self):
    # Convert to Path object
    model_path = Path(self.pipeline_ref.path)
    
    # Add to Python path
    if str(model_path) not in sys.path:
        sys.path.insert(0, str(model_path))
    
    # Import components
    components_path = model_path / "components.py"
    spec = importlib.util.spec_from_file_location("components", components_path)
    components_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(components_module)
    
    # Load pipeline
    return spacy.load(model_path / "spacy_pipeline")

  @bentoml.api
  def analyze(self, text: str = EXAMPLE_INPUT) -> list[tuple[str, str]]:
    doc = self.model(text)
    return [(w.text, w.pos_) for w in doc]
  
  @bentoml.api
  def analyze_lang(self, text: str = EXAMPLE_INPUT) -> list[tuple[str, str]]:
    doc = self.pipeline(text)
    return [(w.text, w.label_) for w in doc.ents]
