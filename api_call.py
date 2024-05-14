import urllib.request as libreq
import feedparser
import time
from tqdm import tqdm
import sys
import os


NER = "Named+Entity+Recognition"
NLP = "%22Natural+Language+Processing%22"
LLM = "%22Large+Language+Models%22"
BOW = "%22Bag+of+Words%22"
WORD = "word+embedding"

DOM = "%22Digital+Outcrop+Models%22"
REM = "Remote+Sensing"
CAR = "Carbonate+Rocks"
RES = "Reservoir+Analogue"
SOUR = "Source+Rocks"

all_nlp = [NLP, "NLP", "BERT", "Transformers", "GLOVE", 
       "WORD2VEC", BOW, "LSTM", "RNN", "llama", "n-gram",
        WORD, "clip", NER, LLM
]

all_geo = ["geoscience", DOM, "geophysics", "Petrophysics", REM, CAR, RES, SOUR]

def get_query(nlp, geo):
    search = "all:%28"    
    for i in nlp:
        search = search + f"{i}+OR+"
    search = search[:-4] + "%29+AND+all:%28"    
    for i in geo:
        search = search + f"{i}+OR+"
    search = search[:-4] + "%29"
    return search

base_url = 'http://export.arxiv.org/api/query?'
start = 10000
iter_size = 50
delay = 5
TOTAL = 55818

searches = [get_query(all_nlp, all_geo)]
for search in searches:
    SIZE_WAS_UPDATED = False
    max = TOTAL
    i = 0
    with open(f"Arxiv Search_part2.txt", "a+", encoding="utf-8") as file, tqdm(initial=start, total=TOTAL) as pbar:
        while i < max:            
            query = 'search_query=%s&start=%i&max_results=%i' % (search, i, i+iter_size)
            print(base_url + query)            
            result = libreq.urlopen(base_url + query).read().decode('utf-8')
            if not SIZE_WAS_UPDATED:
                query_size = int(feedparser.parse(result).feed['opensearch_totalresults'])
                #print(query_size)                
                max = query_size# if query_size < TOTAL else TOTAL
                pbar.total = query_size
                pbar.refresh()
                SIZE_WAS_UPDATED = True
            file.write(result)
            file.flush()
            i+= iter_size
            time.sleep(delay)
            pbar.update(50)
    


