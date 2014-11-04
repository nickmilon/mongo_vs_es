'''
 http://localhost:9200/_cluster/nodes?settings=true&pretty=true
 res = elas.ES.search(index="mongovses", body={"query": {"match_all": {}}})
 print("num of docs=[%d] :" % res['hits']['total'])
 
 esq={"term" : { "text": "brown" }}
 res = elas.ES.search(index="mongovses", body={"query": esq})
 for i in  res['hits']['hits']: print  i['_source']['text']
 
 cProfile.run("for i in range(0,1000):res = elas.ES.search(index='mongovses', body={'query': esq})")
'''
#from gevent import monkey 
#monkey.patch_all()
 
from elasticsearch import Elasticsearch  
import codecs
from __init__ import _PATH_TO_SAMPLES

PATH_TO_SAMPLE = _PATH_TO_SAMPLES + "sample.txt"
ES = Elasticsearch()
 

def db_reset():
    ES.indices.delete(index='mongovses',ignore=404)
    ES.indices.create(index='mongovses')

def write_sample1():
    with codecs.open(PATH_TO_SAMPLE, encoding='utf-8') as file_in:
        record = file_in.read().split('||')
        doc = {'lang': record[0],'text':record[1]}
        ES.index(index="mongovses", doc_type='tweet', body=doc)


def write_sample(file_name='sample.json', count=None): 
    doc_cnt = 0
    err_cnt = 0 
    with codecs.open(_PATH_TO_SAMPLES + file_name, mode='r', encoding='utf-8') as file_in:
        doc = file_in.readline()
        while doc != u'' and (count is None or doc_cnt < count) :
            try: 
                #print "doc=[%s]" % (doc) 
                ES.index(index="mongovses", doc_type='tweet', body=doc)
                doc_cnt += 1  
            except:
                err_cnt += 1
                pass
            doc = file_in.readline()
    ES.indices.refresh(index="mongovses")        
    print "inserted: [%d] posts errors[%d] from file: [%s]"  % (doc_cnt, err_cnt, _PATH_TO_SAMPLES + file_name)