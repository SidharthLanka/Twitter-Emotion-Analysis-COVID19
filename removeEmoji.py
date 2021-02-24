import re
import csv
import sys
import pandas as pd 
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

df = pd.read_csv("tweetsCopy.csv", encoding = "latin1") 
def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)

if __name__ == '__main__':
    with open('tweetsCopy.csv', encoding = "latin1") as csvfile:
        reader = csv.DictReader(csvfile)
        i=0
        for row in reader:
            text = row['Text']
            result = re.sub(r"RT", "", text)
            result = re.sub(r"@[a-zA-Z0-9]+", "", result)
            final_text = remove_emoji(result)
            df.loc[i, 'Text'] = final_text
            df.to_csv("tweetsCopy.csv", index=False) 
            i = i+1