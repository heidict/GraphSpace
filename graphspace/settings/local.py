from graphspace.settings.base import *
from confluent_kafka import Consumer, Producer

# variables for setting up account through which GraphSpace emails
EMAIL_HOST = 'NONE'
EMAIL_HOST_USER = 'NONE'
EMAIL_HOST_PASSWORD = 'NONE'

# If error is thrown, display the error in the browser (ONLY FOR LOCAL
# MACHINES)
DEBUG = True
TEMPLATE_DEBUG = True

# URL through which to access graphspace
URL_PATH = "http://localhost:8000/"

# If tracking is enabled for GraphSpace in Google Analytics
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-00000000-0'

# Keys given by creating a requestor account on Amazon Mechanical Turk
# (https://www.mturk.com/mturk/welcome)
AWSACCESSKEYID = 'None'
SECRETKEY = 'None'

# Path to GraphSPace
PATH = "/Path_to_GraphSpace"

# SHOULD NEVER CHANGE THIS VALUE
SECRET_KEY = 'this-is-a-secret-key-for-local-settings-only'

# If needing to test on production mturk account (real money)
# AWS_URL = 'https://mechanicalturk.amazonaws.com'

# Sandbox (development) MTURK (fake money used)
AWS_URL = 'https://mechanicalturk.sandbox.amazonaws.com'

# To configure the application to use the Console Backend for sending e-mail. It writes e-mails to standard out instead of sending them.
# http://stackoverflow.com/questions/4642011/test-sending-email-without-email-server
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_database',
        'USER': 'adb',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

# Kafka Configuration
KAFKA_URL = 'localhost:9092'

KAFKA_CONSUMER_OWNER = {
    'bootstrap.servers': KAFKA_URL,
    'group.id': 'graphspace_owner',
    'default.topic.config': {
        'auto.offset.reset': 'smallest'
    }
}

KAFKA_CONSUMER_GROUP = {
    'bootstrap.servers': KAFKA_URL,
    'group.id': 'graphspace_group',
    'default.topic.config': {
        'auto.offset.reset': 'smallest'
    }
}

# Consumer for owner notification
KAFKA_CONSUMER = {
    "owner": Consumer(KAFKA_CONSUMER_OWNER),
    "group": Consumer(KAFKA_CONSUMER_GROUP)
}

KAFKA_CONSUMER["owner"].subscribe(['owner'])
KAFKA_CONSUMER["group"].subscribe(['group'])

KAFKA_CONSUMER_POLL_TIMEOUT = 2

KAFKA_PRODUCER = Producer({
    'bootstrap.servers': KAFKA_URL
})
