import spacy
from spacy.tokens import Span
from spacy.util import filter_spans

@spacy.Language.component("programming_language_detector")
def detect_programming_languages(doc):
    """Find mentions of programming languages and mark them as entities"""
    programming_languages = {
        "python", "javascript", "java", "c++", "rust", 
        "go", "ruby", "php", "swift", "kotlin"
    }
    
    matches = []
    for token in doc:
        if token.text.lower() in programming_languages:
            span = Span(doc, token.i, token.i + 1, label="PROG_LANG")
            matches.append(span)
    
    # Use filter_spans to handle overlaps
    all_ents = list(doc.ents) + matches
    doc.ents = filter_spans(all_ents)
    return doc

@spacy.Language.component("tech_company_detector") 
def detect_tech_companies(doc):
    """Find tech company mentions"""
    tech_companies = {"apple", "google", "microsoft", "amazon", "meta", "openai"}
    
    matches = []
    for token in doc:
        if token.text.lower() in tech_companies:
            span = Span(doc, token.i, token.i + 1, label="TECH_COMPANY")
            matches.append(span)
    
    # Use filter_spans to handle overlaps
    all_ents = list(doc.ents) + matches
    doc.ents = filter_spans(all_ents)
    return doc