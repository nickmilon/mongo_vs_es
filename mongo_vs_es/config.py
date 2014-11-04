#MONGO_CONF={'hosts_or_uri': 'nm-21', 'replicaSet': 'rstwtgr'} 
"""
    MongoDB TS Language support 
    http://docs.mongodb.org/manual/reference/text-search-languages/#text-search-languages
    en or english
    fi or finnish
    fr or french
    de or german
    hu or hungarian
    it or italian
    no or norwegian
    pt or portuguese
    ro or romanian
    ru or russian
    es or spanish
    sv or swedish
    tr or turkish]
"""

MONGO_CONF ={}  #for local Host 
MONGO_SAMPLE_CONF= {'dbName':'tst_sample1'} 
MONGO_TS_SUPPORTED_LANGUAGES =('nl', 'en', 'fi', 'fr', 'de', 'hu',
                               'it', 'no', 'pt', 'ro', 'ru', 'es', 'sv', 'tr')
 
