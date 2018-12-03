import sys
import pandas as pd
import sqlite3
import os

conn = sqlite3.connect('harassment-labels.db')
c = conn.cursor()

def load_into_db(table, tweetID, text, label):
    try:
        data = (tweetID, text, label, 0, -1)
        c.execute("INSERT INTO " + table + "(id, tweet, label, isVerified, answer) VALUES (?, ?, ?, ?, ?)", data)
    except:
        print(table, tweetID, text, label)

def main():
    data_dir = sys.argv[1]
    for f in os.listdir(data_dir):
        fname = os.path.join(data_dir, f)
        sample_df = pd.read_csv(fname)
        for idx, row in sample_df.iterrows():
            load_into_db("kumarde", row['tweetID'], row['text'], f.split('.')[0])
            load_into_db("zzma", row['tweetID'], row['text'], f.split('.')[0])
        conn.commit()

if __name__ == "__main__":
    main()
