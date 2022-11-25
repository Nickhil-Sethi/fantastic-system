# pip install -U spacy
# python -m spacy download en_core_web_sm
import spacy
import sys

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")


def entity_resolve(text: str):
    doc = nlp(text)
    for entity in doc.ents:
        print(entity.text, entity.label_)
    return


if __name__ == "__main__":
    body = sys.stdin.read()
    entity_resolve(body)
