import nltk
import spacy

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

nlp = spacy.load('en_core_web_sm')

def preprocess_text(text):

    doc = nlp(text)
    processed_data = []
    
    for sentence in doc.sents:
        tokens = [token.text for token in sentence if not token.is_stop]
        
        
        lemmatized_words = [token.lemma_ for token in sentence if not token.is_stop]
        
    
        pos_tags = [(token.text, token.pos_) for token in sentence]
        
        processed_data.append({
            'sentence': sentence.text,
            'tokens': tokens,
            'lemmatized_words': lemmatized_words,
            'pos_tags': pos_tags
        })
    
    return processed_data

text = input("Enter the text you want to preprocess: ")

processed_data = preprocess_text(text)
for data in processed_data:
    print("Sentence:", data['sentence'])
    print("Tokens:", data['tokens'])
    print("Lemmatized Words:", data['lemmatized_words'])
    print("Part of Speech Tags:", data['pos_tags'])
    print()
