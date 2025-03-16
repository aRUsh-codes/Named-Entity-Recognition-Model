# Named-Entity-Recognition-Model
## Overview

This project implements a Named Entity Recognition (NER) model using SpaCy and the CoNLL-2003 dataset. The model is trained to identify entities such as persons, organizations, and locations. The workflow includes data preprocessing, feature engineering, model training, optimization, and deployment.

## Steps Taken
- Data Preprocessing & Feature Engineering
- Loaded the CoNLL-2003 dataset using the datasets library.
- Performed tokenization and entity extraction.
- Cleaned text data by removing special characters and ensuring proper alignment of tokens and labels.
- Converted the dataset into SpaCy's required training format.

## Model Selection & Optimization
- Used the en_core_web_sm SpaCy model as the base.
- Fine-tuned the NER pipeline by adding new entity labels and optimizing with minibatch training.
- Trained the model for 10 epochs while monitoring and minimizing loss.

## Deployment Strategy & API Usage Guide
- Saved the trained model using spacy.to_disk() for future use.
- Serialized the model into a pickle file (trained_ner_model.pkl) for easy deployment.
- The model can be loaded and used for entity recognition in new text data.

## How to run the project
### OPTION 1 (Running it locally)
Step 1 :- Install dependencies
```pip install -r requirements.txt```

Step 2 :- Load the trained model
```import spacy```
```nlp = spacy.load("trained_ner_model")```

Step 3 :- Use the model to predict named entities
```doc = nlp(text)```
```print([(ent.text, ent.label_) for ent in doc.ents])```

### OPTION 2 (Run using Postman)
Step 1 :- Download Postman Dekstop Agent

Step 2 :- Run the app.py using ```uvicorn app:app --reload```

Step 3 :- Go to Postman and Select Dekstop Agent (bottom right)

Step 4 :- Select 'POST' Method and in the body type the text in JSON format 

Step 5 :- Send.


## Working Video



https://github.com/user-attachments/assets/26e7bfaa-cf63-417f-8650-deb87664e3fc


