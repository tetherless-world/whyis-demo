# -*- config:utf-8 -*-

import os
import logging
from datetime import timedelta

project_name = "whyis-demo"
import importer

import autonomic
import agents.nlp as nlp
import agents.hermit as hermit
import rdflib
from datetime import datetime

# Set to be custom for your project
LOD_PREFIX = 'http://purl.org/twc/demo/mcbk'
#os.getenv('lod_prefix') if os.getenv('lod_prefix') else 'http://hbgd.tw.rpi.edu'

skos = rdflib.Namespace("http://www.w3.org/2004/02/skos/core#")

from whyis_demo.agent import *

# base config class; extend it to your needs.
Config = dict(
    # use DEBUG mode?
    DEBUG = False,

    site_name = "MCBK Demo",

    site_header_image = 'static/images/random_network.png',

    site_description = '',
    
    DEFAULT_ANONYMOUS_READ = True,
    
    root_path = '/apps/whyis',

    # use TESTING mode?
    TESTING = False,

    # use server x-sendfile?
    USE_X_SENDFILE = False,

    WTF_CSRF_ENABLED = True,
    SECRET_KEY = "LJ9ccziRGL2GIKYy7xStZhywz22Mx4mq",

    nanopub_archive = {
        'depot.storage_path' : "/data/nanopublications",
    },

    file_archive = {
        'depot.storage_path' : '/data/files',
        'cache_max_age' : 3600*24*7,
    },
    vocab_file = "/apps/whyis-demo/vocab.ttl",
    WHYIS_TEMPLATE_DIR = [
        "/apps/whyis-demo/templates",
    ],
    WHYIS_CDN_DIR = "/apps/mcbk_demo/static",

    # LOGGING
    LOGGER_NAME = "%s_log" % project_name,
    LOG_FILENAME = "/var/log/%s/output-%s.log" % (project_name,str(datetime.now()).replace(' ','_')),
    LOG_LEVEL = logging.INFO,
    LOG_FORMAT = "%(asctime)s %(levelname)s\t: %(message)s", # used by logging.Formatter

    PERMANENT_SESSION_LIFETIME = timedelta(days=7),

    # EMAIL CONFIGURATION
    ## MAIL_SERVER = "",
    ## MAIL_PORT = 587,
    ## MAIL_USE_TLS = True,
    ## MAIL_USE_SSL = False,
    ## MAIL_DEBUG = False,
    ## MAIL_USERNAME = '',
    ## MAIL_PASSWORD = '',
    ## DEFAULT_MAIL_SENDER = "Jim McCusker <mccusj2@rpi.edu>",

    # see example/ for reference
    # ex: BLUEPRINTS = ['blog']  # where app is a Blueprint instance
    # ex: BLUEPRINTS = [('blog', {'url_prefix': '/myblog'})]  # where app is a Blueprint instance
    BLUEPRINTS = [],

    lod_prefix = LOD_PREFIX,
    SECURITY_EMAIL_SENDER = "Jim McCusker <mccusj2@rpi.edu>",
    SECURITY_FLASH_MESSAGES = True,
    SECURITY_CONFIRMABLE = False,
    SECURITY_CHANGEABLE = True,
    SECURITY_TRACKABLE = True,
    SECURITY_RECOVERABLE = True,
    SECURITY_REGISTERABLE = True,
    SECURITY_PASSWORD_HASH = 'sha512_crypt',
    SECURITY_PASSWORD_SALT = '9HoKGpbbKD4fP5rieQj3m8/2KtUfedEH',
    SECURITY_SEND_REGISTER_EMAIL = False,
    SECURITY_POST_LOGIN_VIEW = "/",
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False,
    SECURITY_DEFAULT_REMEMBER_ME = True,
    ADMIN_EMAIL_RECIPIENTS = [],
    db_defaultGraph = LOD_PREFIX + '/',

    java_classpath = "/apps/mcbk_demo/jars",

    admin_queryEndpoint = 'http://localhost:8080/blazegraph/namespace/admin/sparql',
    admin_updateEndpoint = 'http://localhost:8080/blazegraph/namespace/admin/sparql',
    
    knowledge_queryEndpoint = 'http://localhost:8080/blazegraph/namespace/knowledge/sparql',
    knowledge_updateEndpoint = 'http://localhost:8080/blazegraph/namespace/knowledge/sparql',

    LOGIN_USER_TEMPLATE = "auth/login.html",
    CELERY_BROKER_URL = 'redis://localhost:6379/0',
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0',
    default_language = 'en',
    namespaces = [
        importer.LinkedData(
            prefix = LOD_PREFIX+'/doi/',
            url = 'http://dx.doi.org/%s',
            headers={'Accept':'text/turtle'},
            format='turtle',
            postprocess_update= '''insert {
                graph ?g {
                    ?pub a <http://purl.org/ontology/bibo/AcademicArticle>.
                }
            } where {
                graph ?g {
                    ?pub <http://purl.org/ontology/bibo/doi> ?doi.
                }
            }
            '''
        ),
#        importer.LinkedData(
#            prefix = LOD_PREFIX+'/schema/',
#            url = 'http://schema.org/%s',
#            headers={'Accept':'text/turtle'},
#            format='turtle',
#            postprocess_update= '''insert {
#                graph ?g {
#                    ?class a <http://www.w3.org/2002/07/owl#Class>.
#                }
#            } where {
#                graph ?g {
#                    ?class a <http://www.w3.org/2000/01/rdf-schema#Class>.
#                }
#            }
#            '''
#        ),
        importer.LinkedData(
            prefix = LOD_PREFIX+'/dbpedia/',
            url = 'http://dbpedia.org/resource/%s',
            headers={'Accept':'text/turtle'},
            format='turtle',
            postprocess_update= '''insert {
                graph ?g {
                    ?article <http://purl.org/dc/terms/abstract> ?abstract.
                }
            } where {
                graph ?g {
                    ?article <http://dbpedia.org/ontology/abstract> ?abstract.
                }
            }
            '''
        ),
        importer.FileImporter(
            prefix = LOD_PREFIX+'/arrayexpress/xml/v3/',
            url = 'https://www.ebi.ac.uk/arrayexpress/xml/v3/%s',
            import_once=True
        )
    ],
    inferencers = {
        "SETLr": autonomic.SETLr(),
        "SETLMaker": autonomic.SETLr(),
#        "Consistency Check" : hermit.ConsistencyCheck()
#        "HTML2Text" : nlp.HTML2Text(),
#        "EntityExtractor" : nlp.EntityExtractor(),
#        "EntityResolver" : nlp.EntityResolver(),
#        "TF-IDF Calculator" : nlp.TFIDFCalculator(),
#        "SKOS Crawler" : autonomic.Crawler(predicates=[skos.broader, skos.narrower, skos.related])
    },
    inference_tasks = [
#        dict ( name="SKOS Crawler",
#               service=autonomic.Crawler(predicates=[skos.broader, skos.narrower, skos.related]),
#               schedule=dict(hour="1")
#              )
    ],

    base_rate_probability = 0.5
)


# config class for development environment
Dev = dict(Config)
Dev.update(dict(
    DEBUG = True,  # we want debug level output
    MAIL_DEBUG = True,
    EXPLAIN_TEMPLATE_LOADING = True,
    DEBUG_TB_INTERCEPT_REDIRECTS = False
))

# config class used during tests
Test = dict(Config)
Test.update(dict(
    TESTING = True,
    WTF_CSRF_ENABLED = False
))
