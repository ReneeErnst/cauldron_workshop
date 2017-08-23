import cauldron as cd
import pandas as pd
import requests
import io
import string

url_prefix = 'https://s3-us-west-2.amazonaws.com/cauldron-workshop/data'

def pull_data(file_name: str) -> pd.DataFrame:
    """
    Downloads data from aws
    :param file_name:
    :return: Dataframe with downloaded data
    """
    response = requests.get('{}/{}.csv'.format(url_prefix, file_name))
    buffer = io.StringIO(response.text)
    return pd.read_csv(buffer)

data_frames = [
    pull_data(character)
    for character in string.ascii_lowercase
]

df: pd.DataFrame = pd.concat(data_frames)
cd.display.table(df.head(20))

cd.shared.df = df
