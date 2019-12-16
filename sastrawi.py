# import Sastrawi package
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import pandas
# sentence = pandas.read_csv('#212spiritmuslim.csv')
sentence = pandas.read_csv('#212spiritmuslim.csv', 
            index_col='IdUser', 
            parse_dates=['twett'],
            header=0, 
            names=['IdUser', 'twett'])
sentence.to_csv('#212spiritmuslim_modified.csv')
# print(df)
# create stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# stem
# sentence = 'Perekonomian Indonesia sedang dalam pertumbuhan yang membanggakan'
# print   = stemmer.stem(sentence)


sentence = sentence[~sentence.applymap(lambda x: str.startswith(str(x), '--')).any(1)]
print(sentence)
# ekonomi indonesia sedang dalam tumbuh yang bangga

# print(stemmer.stem('Mereka meniru-nirukannya'))
# mereka tiru
