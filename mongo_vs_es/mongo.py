#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
https://github.com/mongodb/mongo/tree/master/src/mongo/db/fts 
# sc.find({ '$text': { '$search': 'browns', '$language': 'english' } })[0]
'''
import json
from mongo_vs_es.config import MONGO_CONF

from pymongo_ext import pymongo_ext as pmext 
import io
CL=pmext.MdbClient(**MONGO_CONF)
from __init__ import _PATH_TO_SAMPLES 

MC=CL.client.mongovses.sample

def db_reset():
    CL.client.drop_database('mongovses')
    CL.client.mongovses.sample.ensure_index( [('text', "text")], default_language='en', language_override="lang")
 
def write_sample(file_name='sample.json', count=None, w=0, j=False): 
    doc_cnt = 0 
    with io.open(_PATH_TO_SAMPLES + file_name, mode='rt', encoding='utf-8', newline= '\n') as file_in:
        doc = file_in.readline()
        while doc != u'' and (count is None or doc_cnt < count) : 
            doc_cnt += 1   
            MC.insert(json.loads(doc,"utf-8"),w=w,j=j) 
            doc = file_in.readline() 
    print "inserted: [%d] posts from file: [%s]"  % (doc_cnt, _PATH_TO_SAMPLES + file_name)