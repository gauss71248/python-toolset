import csv
import os
import pandas as pd


def ingest_file(filename: str):
    with open(filename) as file:
        reader = csv.reader(file, delimiter=',')
        data = list(reader)
        columns = data[0]
        data = data[1:]
        df = pd.DataFrame(data, columns=columns)
        return df


def filenames_in_dir(dir: str):
    return [file for file in os.walk(dir)][0][2]


def dir_to_df(dir: str):
    filenames = filenames_in_dir(dir)
    file_dfs = [ingest_file(dir + "/" + x) for x in filenames]
    df = pd.concat(file_dfs, ignore_index=True)
    return df


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = dir_to_df("./input")
    df.to_csv("bigbangvoucher.csv")
