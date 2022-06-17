import pandas as pd

df = pd.read_excel('input/Content Automation (1).xlsx', header=1)
df.dropna(inplace=True)

df['Words count'] = [len(x.split()) for x in df['TEXT'].tolist()]
df['Percentage of required length'] = round(df['Words count'] / df['Length\n (Words)'], 2)
keywords_raw = [x.lower().split('-') for x in df['Keywords'].str.replace('-', '', 1).replace('\n', '', regex=True)]
keywords = [[st.strip() for st in keyword] for keyword in keywords_raw]
df['Keywords raw'] = keywords
df['Total Keywords'] = [len(x) for x in df['Keywords raw']]

counter_list = []
for index, row in df.iterrows():
    count = 0
    for keyword in row['Keywords raw']:
        if keyword in row['TEXT'].lower():
            count += 1
    counter_list.append(count)
df['Total keywords used in text'] = counter_list
df['Percentage of keywords used'] = round(df['Total keywords used in text'] / df['Total Keywords'], 2)
exclude_columns = ['Words count',
                   'Keywords raw',
                   'Total keywords used in text',
                   'Total Keywords',
                   'Total keywords used in text'
                   ]

df.to_excel('output.xlsx', columns=[column for column in df.columns if column not in exclude_columns])
