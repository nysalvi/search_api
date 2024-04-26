from collections.abc import Container
from argparse import ArgumentParser
import urllib.request as libreq
from enum import IntEnum
import pandas as pd
import argparse
import pickle
import time
import sys
import os

class ApiRequestRate():
    class CallRate(IntEnum):    
        ieee = 4,
        arxiv = 4    
    def __call__(self, x): 
        return self.CallRate[x].value
    
class ApiTimeOut():    
    class TimeOut(IntEnum):
        ieee = 0,
        arxiv = 1000
    def __call__(self, x):
        return self.TimeOut[x].value
    


    
def create_parser():
    def config_or_args(parser):
        if hasattr(parser, '--config') and any(hasattr())
    parser = argparse.ArgumentParser()    
    parser.add_argument("--config")
    parser.add_argument("--api_rate", choices=["ieee", 'arxiv', 't&f', 'elsevier'])    
    parser.add_argument("--time_out", choices=["ieee", 'arxiv', 't&f', 'elsevier'])    
    return parser

def parse_args(parser: ArgumentParser):    
    args = parser.parse_args()        
    
    if args[0] == '--config' and any(x.startswith('-') for x in args[::-1]):
        Exception("Must set args OR config")

    args.api_rate = ApiRequestRate()(args.api_rate)
    args.time_out = ApiTimeOut()(args.time_out)


    return args
    
parser = create_parser()
for x in vars(parser.parse_args()):
    print(x)
#args = parse_args(parser)
print(sys.argv)
#for i in range():
#with libreq.urlopen('http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=1') as url:
#   #r = url.read()
#print(r)


