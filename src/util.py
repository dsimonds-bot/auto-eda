# Package Import
import pandas as pd
import numpy as np
import os
import shutil

# Globals
branding_dict = {
    'gold' : '#946B2D',
    'dark-blue' : '#0E1A40',
    'grey' : '#5D5D5D',
    'light-blue' : '#222F5B'
}

# Function definitions
def dataframe_attributes(dataframe: pd.DataFrame) -> dict:
    
    """
    This function takes a user inputted dataframe, and creates an easily accessible dictionary
    of dataframe attributes. 
    
    Parameters:
    ----------
    dataframe : pd.DataFrame
        The dataframe to gather attributes for
        
    Returns:
    -------
    attribute_dict : dict
        A dictionary containing a mapping of dataframe attributes
    """
    
    # Create the dictionary
    attribute_dict = {
        '_m' : dataframe.shape[0],
        '_n' : dataframe.shape[1],
        '_columns' : list(dataframe.columns),
        '_categorical' : dataframe.select_dtypes(include = object),
        '_numeric' : dataframe.select_dtypes(include = np.number)
    }
    
    return attribute_dict

def dataframe_overview_writeup(report_name:str, attribute_dict: dict) -> str:
    
    """
    This function takes a user inputted attribute dictionary, and creates a brief text summary
    of the dataframe attributes.
    
    Parameters:
    ----------
    report_name : str
        The name of the report called in the write up
        
    attribute_dict : dict
        A dictionary produced by dataframe_attributes(dataframe: pd.DataFrame)
        
    Returns:
    -------
    dataframe_overview_string : str
        A string containing a brief write up of the core dataframe attributes
    """
    
    # Gathering the variables for write up
    nobs = attribute_dict['_m']
    ndim = attribute_dict['_n']
    cat = attribute_dict['_categorical']
    num = attribute_dict['_numeric']
    
    # Writing string
    overview_writeup = f'Report name: {report_name}' \
        f' Your dataframe has {nobs} nobs and {ndim} ndim.' \
        f' There are {len(cat)} categorical features, and {len(num)} numeric features.'
    
    return overview_writeup

def dataframe_info_table(dataframe: pd.DataFrame) -> pd.DataFrame:
    
    """
    This function creates a dataframe info table, essentially the same as pd.Dataframe().info()
    However, the difference is the NaN values are converted to a %
    
    Parameters:
    ----------
    dataframe : pd.DataFrame
        The dataframe to produce info for
        
    Returns:
    -------
    dataframe_info : pd.DataFrame
        The summary dataframe containing:
            - Columns
            - dtype
            - nunique() values
            - NaN % of feature
    """
    
    # Creating the info dataframe
    dataframe_info = pd.DataFrame(
        data = {
            'dtypes' : dataframe.dtypes,
            'nunique' : dataframe.nunique(),
            'NaN' : round(100*(dataframe.isna().sum()/len(dataframe)),3)
        }
    ).sort_values(
        by = 'NaN',
        ascending = False
    )
    
    return dataframe_info

def mk_assets_dir():

    """
    This function makes a dir called assets in the cwd
    """
    if os.path.exists('assets') and os.path.isdir('assets'):
        shutil.rmtree(os.path.join(os.getcwd(), 'assets'))

    os.mkdir(os.path.join(os.getcwd(), 'assets'))

def rm_dir(dirname: str):
    
    """
    This function takes a dir name in the current working directory and deletes it.
    It will also take care of all of the files saved within that directory.
    
    Parameters:
    ----------
    dirname : str
        The name of the directory we are removing
    """
    
    shutil.rmtree(os.path.join(os.getcwd(), dirname))

def easter_egg():
    class Dave:
        is_goobie = True

    if Dave.is_goobie:
        print("mehoy minoy")

def column_describe_storage(dataframe: pd.DataFrame) -> dict:

    """
    This function takes a pandas dataframe, and loops through each column.
    Within each loop, this function then stores the column name along with a simple
    pd.DataFrame.describe() method dataframe within the dictionary. 

    Parameters:
    ----------
    dataframe : pd.DataFrame
        A pandas dataframe to loop through and store results for

    Returns:
    -------
    column_describe_dict : dict
        A dictionary with each key : value pair corresponding to the 
        column name and .describe() method on that column    
    """

    # Create the storage dictionary
    column_describe_dict = {}

    # Start the loop
    for numeric_column_names in list(dataframe.columns):

        # Create the key value pair
        column_describe_dict[numeric_column_names] = pd.DataFrame(
            data = {
                numeric_column_names : dataframe[numeric_column_names].describe()
            })

    return column_describe_dict