import pandas as pd
import pprint


drake = pd.read_csv('drake/drake_data.csv')

for album in drake['album']:
    pprint.pprint(album)

#pprint.pprint(drake['lyrics'][0])

