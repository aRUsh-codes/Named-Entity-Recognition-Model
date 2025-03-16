from fastapi import FastAPI
from pydantic import BaseModel
import spacy

# Load the trained NER model
nlp = spacy.load("trained_ner_model")

# Initialize FastAPI app
app = FastAPI()

# Define request model
class TextInput(BaseModel):
    text: str

# Define /predict endpoint
@app.post("/predict")
def predict_entities(input_data: TextInput):
    doc = nlp(input_data.text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return {"entities": entities}

