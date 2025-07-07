import spacy
from components import *  # Import your components

def create_custom_pipeline():
    """Create a custom spaCy pipeline with our components"""
    # Load base model
    nlp = spacy.load("en_core_web_sm")
    
    # Add custom components
    nlp.add_pipe("programming_language_detector", after="ner")
    nlp.add_pipe("tech_company_detector", after="programming_language_detector")
    
    return nlp

if __name__ == "__main__":
    # Test the pipeline
    nlp = create_custom_pipeline()
    
    text = "Apple is hiring Python developers. Google prefers Go programming."
    doc = nlp(text)
    
    print("Test results:")
    for ent in doc.ents:
        print(f"  {ent.text}: {ent.label_}")