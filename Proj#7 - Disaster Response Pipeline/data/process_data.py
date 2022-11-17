import sys
import pandas as pd
import numpy as np
import sqlite3
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
    """Load & merge messages & categories datasets
    
    inputs:
    messages_filepath:Filepath for csv file containing messages dataset.
    categories_filepath: Filepath for csv file containing categories dataset.
       
    outputs:
    df: dataframe, containing merged content of messages & categories datasets.
    """
    #loading datasets
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    # merge datasets
    df = messages.merge(categories, on= 'id')
    # create a dataframe of the 36 individual category columns
    categories = df.categories.str.split(";", expand = True)

    # select the first row of the categories dataframe
    row = categories.iloc[[0]]
    # use this row to extract a list of new column names for categories.
    category_colnames = row.apply(lambda x: x.str[:-2]).values.tolist()
    #rename the columns
    categories.columns = category_colnames
    
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].apply(lambda x: x[-1:])
        
        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column])

    # drop the original categories column from `df`
    df.drop(columns='categories', inplace = True)
    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis = 1)
    
    return df


def clean_data(df):
    """Clean dataframe by removing duplicates & converting categories from strings 
    to binary values. Also, renames columns and replace wrong values.
    
    Args:
    df: dataframe, containing merged content of messages & categories datasets.
       
    Returns:
    df: dataframe, containing cleaned version of input dataframe.
    """
    # cleaning up the column names 
    for i in range(len(df.columns)):
        if i > 3:
            df.rename(columns = {df.columns[i] : df.columns[i][0]}, inplace = True)

    # drop duplicates
    df = df.drop_duplicates()

    # replace the 2s with 1s in 'related' column
    df['related'] = df['related'].replace(2, 1)

    return df


def save_data(df, database_filename):
    """Save into  SQLite database.
    
    inputs:
    df: dataframe, containing cleaned version of merged message and 
    categories data.
    database_filename: Filename for output database. String.
       
    outputs:
    None
    """
    engine = create_engine('sqlite:///'+database_filename)
    # name the database 'DisasterResponse'
    df.to_sql('DisasterResponse', engine,if_exists = 'replace', index=False)  


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()
