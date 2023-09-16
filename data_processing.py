import pandas as pd


def main():
    df = load_data()

    return df


def load_data():
    df = pd.read_csv("players_and_transf.csv")

    #print(df.shape)

    df = subset_df(df)
    
    return df

def subset_df(df):

    season_list = ["2010/2011", "2011/2012", "2012/2013", "2013/2014", "2014/2015", "2015/2016", "2016/2017", "2017/2018", "2018/2019", "2019/2020"]

    df = df[df["position"] == "FW"]

    df = df[df["season"].isin(season_list)] #select certain position and certain seasons


    df = df[["name", "age", "apps", "mins", "goals", "assists", "motm", "rating", "traded"]]

    #print(df.isnull().values.any(), df.isnull().sum().sum()) #No Nan values after subsettting

    #print(df.head())
    #print(df.shape)
    #print(df.nunique())
    #for column in df.columns.values:
        #print(df[column].isnull().sum(), column)
    return df



main()