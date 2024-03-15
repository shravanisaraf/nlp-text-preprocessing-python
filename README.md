# Text Preprocessing with NLTK and SpaCy

Welcome to the Text Preprocessing repository! This project demonstrates the preprocessing of text using NLTK and SpaCy libraries in Python. The code provided here performs various text preprocessing tasks such as sentence segmentation, tokenization, lemmatization, and part-of-speech tagging.

## Features

- Sentence segmentation using SpaCy
- Tokenization and lemmatization with NLTK
- Part-of-speech tagging using SpaCy
- User-friendly command-line interface for text input

## Installation

To run the code locally, you'll need Python 3 and the following libraries:

```bash
pip install nltk spacy
python -m spacy download en_core_web_sm
python -m nltk.downloader punkt stopwords wordnet
```

## Usage

1. Download the .py file 

2. Run the script and follow the prompts:

 ## Example

Here's a sample output after preprocessing the input text:

```
Enter the text you want to preprocess: This is a sample sentence. It demonstrates the text preprocessing pipeline.
```

Output:
```
Sentence: This is a sample sentence.
Tokens: ['This', 'sample', 'sentence', '.']
Lemmatized Words: ['This', 'sample', 'sentence', '.']
Part of Speech Tags: [('This', 'DET'), ('is', 'AUX'), ('a', 'DET'), ('sample', 'NOUN'), ('sentence', 'NOUN'), ('.', 'PUNCT')]

Sentence: It demonstrates the text preprocessing pipeline.
Tokens: ['It', 'demonstrates', 'text', 'preprocessing', 'pipeline', '.']
Lemmatized Words: ['-PRON-', 'demonstrate', 'text', 'preprocessing', 'pipeline', '.']
Part of Speech Tags: [('It', 'PRON'), ('demonstrates', 'VERB'), ('the', 'DET'), ('text', 'NOUN'), ('preprocessing', 'NOUN'), ('pipeline', 'NOUN'), ('.', 'PUNCT')]
```

3. Enter the text you want to preprocess when prompted.


## Contributing

Contributions are welcome! If you have any ideas for improvement or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
