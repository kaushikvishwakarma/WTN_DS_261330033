# Introduction to NLP - Interview Questions

1. **How Text Preprocessing is performed?**
   *Answer*: Text preprocessing typically involves a pipeline of operations:
   - Converting text to lowercase
   - Removing punctuation, special characters, and numbers
   - Tokenization (splitting text into individual words or tokens)
   - Removing stop words (common words like "and", "the", "is")
   - Applying Stemming or Lemmatization to reduce words to their base forms.

2. **Difference between Structured and Unstructured Dataset**
   *Answer*: 
   - **Structured Data** is highly organized and formatted in a predefined model, typically residing in relational databases (e.g., SQL tables with rows and columns).
   - **Unstructured Data** lacks a predefined data model or organization, making it harder to process and analyze using traditional tools (e.g., text documents, emails, images, audio, video).

3. **What is POS Tagging?**
   *Answer*: Part-of-Speech (POS) tagging is the process of marking up a word in a text as corresponding to a particular part of speech (e.g., noun, verb, adjective, adverb), based on both its definition and its context within the sentence.

4. **What is Name Entity Recognition?**
   *Answer*: Named Entity Recognition (NER) is an NLP technique that identifies and classifies key information (entities) in unstructured text into predefined categories such as person names, organizations, locations, medical codes, monetary values, etc.

5. **What is Stemming and Lemmatization?**
   *Answer*: Both are text normalization techniques used to reduce words to their root forms.
   - **Stemming** chops off the suffixes of words using heuristic rules.
   - **Lemmatization** uses vocabulary and morphological analysis of words to return the base, dictionary form of a word, known as the lemma.

6. **Difference between Stemming and Lemmatization.**
   *Answer*: 
   - **Accuracy**: Stemming often results in non-real words (e.g., "caring" becomes "car") because it brutally removes endings. Lemmatization considers the context and converts the word to a meaningful base form (e.g., "caring" becomes "care").
   - **Speed**: Stemming is faster and computationally cheaper, while Lemmatization is slower but more accurate.
