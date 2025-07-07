import bentoml
import shutil
from pathlib import Path  # Import Path
from create_pipeline import create_custom_pipeline
import spacy

def create_model():
    """Create BentoML model with custom spaCy pipeline"""
    
    # Create the pipeline
    nlp = create_custom_pipeline()
    
    # Save with BentoML
    with bentoml.models.create("custom_spacy_pipeline") as model_ctx:
        # Convert to Path object
        model_path = Path(model_ctx.path)
        
        # Now you can use the / operator
        nlp.to_disk(model_path / "spacy_pipeline")
        
        # Copy the components file directly
        shutil.copy("components.py", model_path / "components.py")
        
        # Copy any other files you need
        shutil.copy("create_pipeline.py", model_path / "create_pipeline.py")
        
        # Save metadata
        metadata = {
            "components": nlp.pipe_names,
            "custom_components": ["programming_language_detector", "tech_company_detector"],
            "spacy_version": spacy.__version__,
            "base_model": "en_core_web_sm"
        }
        
        import json
        with open(model_path / "metadata.json", "w") as f:
            json.dump(metadata, f, indent=2)
    
    print(f"Model created successfully!")
    return model_ctx

if __name__ == "__main__":
    create_model()