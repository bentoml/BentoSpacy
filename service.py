
import bentoml
import spacy

@bentoml.service(traffic={"timeout": 30},
    resources={
        "cpu": 1,
        "memory": "4Gi",
    },
)
class SpaceService:
    def __init__(self) -> None:
        self.model = spacy.load("en_core_web_sm")

    @bentoml.api
    def predict(self, text: str) -> list[list[str, str]]:
        doc = self.model(text)
        return [[w.text, w.pos_] for w in doc]
    
