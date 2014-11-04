'''
Created on May 8, 2014

@author: nickmilon
'''
import json  
import io
from pymongo_ext import pymongo_ext as pmext 
from mongo_vs_es.config import MONGO_SAMPLE_CONF, MONGO_TS_SUPPORTED_LANGUAGES 
from __init__ import _PATH_TO_SAMPLES 
PATH_TO_SAMPLE = _PATH_TO_SAMPLES 
CL=pmext.MdbClient(**MONGO_SAMPLE_CONF) 
CL.db.Tstatuses.ensure_index('lang') 

def sample_tweets(file_name='sample.json', lang_list=['en','es','ru'],count=None,mode='w'): 
    #@note we could use mongoexport instead
    if lang_list == 'all':
        lang_list = MONGO_TS_SUPPORTED_LANGUAGES 
    for l in lang_list:
        if not  l in MONGO_TS_SUPPORTED_LANGUAGES:
            print 'language %s not supported Aborting' %l 
            return False
    doc_cnt = 0 
    fl=io.open(_PATH_TO_SAMPLES + file_name, mode='w', encoding='utf-8', newline='\n')
    sq = CL.db.Tstatuses.find({"lang":{"$in":lang_list}},fields=['lang','text', 'usn'])
    if count:
        sq.limit(count)
    for doc in sq: 
        doc['orgId']=doc['_id']
        del doc['_id']   
        fl.write(json.dumps(doc, ensure_ascii=False,encoding='utf-8')+'\n')
        if doc_cnt % 10000 == 0:
            print doc_cnt 
    fl.close()   
    print "Exported: [%d] docs to file: [%s]"  % (doc_cnt, _PATH_TO_SAMPLES + file_name)  
    return True
