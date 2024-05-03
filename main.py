import urllib.request as libreq

from enum import IntEnum
import pandas as pd
import argparse
import pickle
import time
import sys
import os


searches = [""]

#for i in searches:
with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1') as url:        
    data = url.read()
    print(data.decode('utf-8'))



