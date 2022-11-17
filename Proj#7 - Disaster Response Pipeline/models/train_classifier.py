import sys
# download necessary NLTK data
import nltk
nltk.download(['punkt', 'wordnet'])
nltk.download('stopwords')
# import statements
import re
import numpy as np
import pandas as pd
import warnings
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sqlalchemy import create_engine
import pickle

from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from nltk.corpus import stopwords
from sklearn.metrics import classification_report
from sklearn.ensemble import AdaBoostClassifier

warnings.simplefilter('ignore')

def load_data(database_filepath):
    engine = create_engine('sqlite:///'+database_filepath)
    df= pd.read_sql_table('DisasterResponse', engine)
    X = df.message
    Y = df[df.columns[4:]]
    #category_names = Y.columns
    return X, Y


def tokenize(text):
    # Converting everything to lower case
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    
    # Tokenize words
    tokens = word_tokenize(text)
    
    # normalization word tokens and remove stop words
    stop_words = stopwords.words("english")
    lemmatizer = WordNetLemmatizer()
    
    normalized = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    return normalized


def build_model():
    pipeline = Pipeline([
        ('vect', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('clf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    # Setting up parameters
    parameters = {
    # deleted some parameters because the file was too big for Github
    # plk file was 900 MB; plese see my ML pipeline notebook for the original codes
    #'vect__ngram_range': ((1, 1),(1,2)), 
    'clf__estimator__n_estimators': [5],
    'clf__estimator__min_samples_split': [2],
    }

    model = GridSearchCV(pipeline, param_grid=parameters, verbose=10)
    #model = model.best_estimator_
    
    return model


def evaluate_model(model, X_test, Y_test):
    Y_pred=model.predict(X_test)

    for i in range(36):
        print(Y_test.columns[i], ':')
        print(classification_report(Y_test.iloc[:,i], Y_pred[:,i]))


def save_model(model, model_filepath):
    pickle.dump(model.best_estimator_, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        #X, Y, category_names = load_data(database_filepath)
        X, Y = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
