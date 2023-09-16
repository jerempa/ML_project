import pandas as pd


def main():
    df = load_data()

    #select_columns_and_rows(df)


def load_data():
    df = pd.read_csv("players_and_transf.csv")

    df = subset_df(df)
    
    return df

def subset_df(df):

    season_list = ["2010/2011", "2011/2012", "2012/2013", "2013/2014", "2014/2015", "2015/2016", "2016/2017", "2017/2018", "2018/2019", "2019/2020"]

    df = df[df["position"] == "FW"]

    df = df[df["season"].isin(season_list)] #select certain position and certain seasons


    df = df[["age", "apps", "mins", "goals", "assists", "motm", "rating", "league", "traded"]]

    #print(df.shape) # Only select forwards and columns that are either a target or a feature
    print(df.isnull().values.any()) #NaN values are not present on the df after subsetting

    #print(df.isnull().sum().sum()) #There are 0 null values

    #print(df.columns.values)

    #for column in df.columns.values:
        #print(df[column].isnull().sum(), column)
    return df

def select_columns_and_rows(df):
    #print(df["season"])
    #new_df = df.loc["2010/2011":"2019/2020"]
    #print(new_df)
    #new_df = df.loc[["age",]]
    #print(df.head())

    return df


main()