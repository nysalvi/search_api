import urllib.request as libreq
from tqdm import tqdm
import feedparser
import argparse
import time
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", type=int, default=0)
parser.add_argument("-nlp", "--nlp_args", nargs="*")
parser.add_argument("-geo", "--geo_args", nargs="*")
parser.add_argument("-d", "--delay", type=int, default=4)
parser.add_argument("-it_size", "--iteration_size", type=int, default=50)
parser.add_argument("-f", "--file_name")
args = parser.parse_args()

NLP = "Natural+Language+Processing"
NER = "Named+Entity+Recognition"
LLM = "Large+Language+Model"
BOW = "Bag+of+Words"
WORD = "word+embedding"

if not args.nlp_args == None: 
    ALL_NLP = args.nlp_args 
else:
    ALL_NLP = [
        NLP, "NLP", "BERT", "Transformer", "GPT", "GLOVE", "WORD2VEC",
        BOW, "LSTM", "RNN", "llama", "n-gram", WORD, "clip", NER, LLM
    ] 

DOM = "Digital+Outcrop+Model"
REM = "Remote+Sensing"
CHEM = "Geochemistry"
CAR = "Carbonate+Rocks"
RES = "Reservoir+Analogue"
SOUR = "Source+Rocks"

if not args.geo_args == None:
    ALL_GEO = args.geo_args 
else: 
    ALL_GEO = [
        "geosciences", DOM, "Geophysics", "Petrophysics",  
        "Geochemistry", REM, CAR, RES, SOUR
    ]

def get_query(all_nlp, all_geo):
    search = "all:%28"    
    for i in all_nlp:
        search = search + f"%22{i}%22+OR+"
    search = search[:-4] + "%29+AND+all:%28"    
    for i in all_geo:
        search = search + f"%22{i}%22+OR+"
    search = search[:-4] + "%29"
    return search

API_URL = 'http://export.arxiv.org/api/query?'
start = args.start
iter_size = args.iter_size
delay = args.delay

#test_url = "http://export.arxiv.org/api/query?search_query=all:%28%22Natural+Language+Processing%22+OR+%22NLP%22+OR+%22BERT%22+OR+%22Transformer%22+OR+%22GLOVE%22+OR+%22GPT%22+OR+%22WORD2VEC%22+OR+%22Bag+of+Words%22+OR+%22LSTM%22+OR+%22RNN%22+OR+%22llama%22+OR+%22n-gram%22+OR+%22word+embedding%22+OR+%22clip%22+OR+%22Named+Entity+Recognition%22+OR+%22Large+Language+Model%22%29+AND+all:%28%22geoscience%22+OR+%22Digital+Outcrop+Models%22+OR+%22geophysics%22+OR+%Geochemistry%22+OR+%22Remote+Sensing%22+OR+%22Carbonate+Rocks%22+OR+%22Reservoir+Analogue%22+OR+%22Source+Rocks%22%29"
searches = [get_query(ALL_NLP, ALL_GEO)]
for search in searches:
    with open(f"teste.txt", "a+", encoding="utf-8") as file:
        query = 'search_query=%s&start=%i&max_results=%i' % (search, start, iter_size)                   
        result = libreq.urlopen(API_URL + query).read().decode('utf-8')        
        file.write(result)
        file.flush()
        with tqdm(initial=iter_size, total=TOTAL) as pbar:
            TOTAL = int(feedparser.parse(result).feed['opensearch_totalresults'])        
            i = iter_size
            while i < TOTAL:            
                time.sleep(delay)
                query = 'search_query=%s&start=%i&max_results=%i' % (search, i, i+iter_size)                   
                result = libreq.urlopen(API_URL + query).read().decode('utf-8')

                file.write(result)
                file.flush()
                i+= iter_size
                pbar.update(iter_size)
        


