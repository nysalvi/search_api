import urllib.request as libreq
from tqdm import tqdm
import feedparser
import argparse
import time
import sys
import re
import os

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", type=int, default=0)
parser.add_argument("-nlp", "--nlp_args", nargs="*")
parser.add_argument("-geo", "--geo_args", nargs="*")
parser.add_argument("-d", "--delay", type=int, default=4)
parser.add_argument("-it_size", "--iteration_size", type=int, default=50)
parser.add_argument("-f", "--file_name")
args = parser.parse_args()

API_URL = 'http://export.arxiv.org/api/query?'

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

def format_query(all_nlp, all_geo):
    search = "all:%28"    
    for i in all_nlp:
        search = search + f"%22{i}%22+OR+"
    search = search[:-4] + "%29+AND+all:%28"    
    for i in all_geo:
        search = search + f"%22{i}%22+OR+"
    search = search[:-4] + "%29"
    return search

def GET_request_is_valid(result):
    parsed = feedparser.parse(result)
    start_index = parsed['feed']['opensearch_startindex']
    end_index = parsed['feed']['opensearch_itemsperpage']
    size = end_index - start_index
    return True if len(result['entries']) != size else False
        

get_query = lambda query: libreq.urlopen(API_URL + query).read().decode('utf-8')        
start = args.start
iter_size = args.iter_size
delay = args.delay

searches = [format_query(ALL_NLP, ALL_GEO)]
for search in searches:
    with open(f"teste.txt", "a+", encoding="utf-8") as file:
        query = 'search_query=%s&start=%i&max_results=%i' % (search, start, iter_size)                   
        result = get_query(query)
        file.write(result); file.flush()
        with tqdm(initial=iter_size, total=TOTAL) as pbar:
            TOTAL = int(feedparser.parse(result).feed['opensearch_totalresults'])        
            i = iter_size
            while i < TOTAL:            
                time.sleep(delay)
                query = 'search_query=%s&start=%i&max_results=%i' % (search, i, i+iter_size)                   
                while not GET_request_is_valid(result):
                    result = get_query(query)
                file.write(result); file.flush()
                i+= iter_size
                pbar.update(iter_size)
        


