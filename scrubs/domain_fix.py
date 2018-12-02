import sys
import configparser
from TwitterSearch import *
from peewee import *
from goose3 import Goose
from datetime import datetime
from urllib.parse import urlparse
from django_models import *
sys.path.insert(0, 'source_recognition') 
from source_recognition import *

def fix_domain(source_record):
	g = Goose()
	article = None
	try:
		article = g.extract(url=source_record.url)
		if (article.canonical_link is not None) and (article.canonical_link is not None):
			source_record.url = article.canonical_link
			source_record.domain = urlparse(source_record.url).netloc
			source_record.save()
			print(article.canonical_link)
		else:
			print("No canonical_link for " + article.title)
	except Exception as e:
		print(e)

list_of_domains = ['dlvr.it']
query = Incidents_IncidentSource.select().where(Incidents_IncidentSource.domain << list_of_domains)
print(query.count())
print()
for row in query:
	print(row.id)
	fix_domain(row)
