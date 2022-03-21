## Labelencoder for categorical attribute
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

def labelencoder_conversion(df, column_in, column_out):
    '''
    Summary:
    read in a categorical column and convert it to a new labelencoded column
    
    Parameters: 
        df - a dataframe holding the categorical column
        column_in - string the name of input column
        column_out - string the name of output column
        
    Returns:
        encode_df - a dataframe with the converted categorical labels
        
    '''
    encode_column = df[column_in]
    encode_df = pd.DataFrame(encode_column, columns=[column_in])
    # creating instance of labelencoder
    labelencoder = LabelEncoder()
    # Assigning numberical values and storing in another column
    encode_df[column_out] = labelencoder.fit_transform(encode_df[column_in])
    
    return encode_df



def onehotencoder_conversion(df, encode_in):
    '''
    Summary:
    read in a categorical column and transform to one-hot enocdered columns, then join with original input column
    
    Parameters: 
        df - a dataframe holding the categorical column
        encode_in - string the name of input column
        
    Returns:
        encode_df_join - a dataframe with the converted onehotencoder labels and original column
        
    '''


    encode_types = df[encode_in]
    encode_df = pd.DataFrame(encode_types, columns=[encode_in])
    # converting type of columns to 'category'
    encode_df[encode_in] = encode_df[encode_in].astype('category')
    encode_df[encode_in] = encode_df[encode_in].cat.codes
    #print (encode_df['building_class_Cat'])
    # creating instance of one-hot-encoder
    enc = OneHotEncoder(handle_unknown='ignore')
    # passing bridge-types-cat column (label encoded values of bridge_types)
    enc_df = pd.DataFrame(enc.fit_transform(df[[encode_in]]).toarray())
    #print (enc_df)
    enc_df.columns = enc.get_feature_names_out()
    
    # merge with main df bridge_df on key values
    encode_df_join = encode_df.join(enc_df)
    #print (encode_df_join)
    return encode_df_join

def ordinalencoder_conversion(df_input, col_name, map_list_test):
    '''
    Summary:
    read in a categorical column and convert it to a new labelencoded column based on the provided map_list
    
    Parameters: 
        df_input - a dataframe holding the categorical column
        col_name - string the name of input column
        map_list_test - dictionary map each category to assigned label
        
    Returns:
        df_ordinal - a dataframe with the converted categorical labels
        
    '''
    from category_encoders import OrdinalEncoder 

    maplist = [{'col': col_name, 
                'mapping': map_list_test}]


    oe = OrdinalEncoder(mapping=maplist)
    df_ordinal = oe.fit_transform(df_input)
    return df_ordinal
