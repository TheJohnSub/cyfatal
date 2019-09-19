import peewee 
import configparser
from peewee import *
#from Incidents import *
import datetime

config_parse = configparser.ConfigParser()
config_parse.read('config.ini')

database = MySQLDatabase(config_parse.get('keys', 'database_name'), user=config_parse.get('keys', 'database_user'), passwd=config_parse.get('keys', 'database_passwd'))
database.connect()

class BaseModel(Model):
		class Meta:
			database = database

class BaseSource(BaseModel):
    url = CharField(null = True)
    site_name = CharField(null = True)
    domain = CharField(null = True)
    article_title = TextField(null = True)
    article_text = TextField(null = True)
    is_related = BooleanField(null = True, default = False)

# class Incidents_Incident(BaseModel):
# 	IncidentDateTime = 	DateTimeField(null = True)
# 	City = CharField(null = True)
# 	State = CharField(null = True)
# 	Zip = CharField(null = True)
# 	Coordinates = CharField(null = True)
# 	VictimName = CharField(null = True)
# 	VictimGender = CharField(null = True)
# 	VictimAge = IntegerField(null = True)
# 	MotoristName = CharField(null = True)
# 	MotoristGender = CharField(null = True)
# 	MotoristAge = IntegerField(null = True)	
# 	HitAndRun = BooleanField(null = True)
# 	ImpairedDriving = BooleanField(null = True)
# 	IncidentType = CharField(null = True)
# 	VehicleType = CharField(null = True)
# 	VehicleMake = CharField(null = True)
# 	VehicleModel = CharField(null = True)

class Incidents_IncidentSource(BaseSource):
    is_not_usa = BooleanField(null = True, default = False)
    is_reviewed = BooleanField(null = True, default = False)
    source_candidate_id = IntegerField(null = True)

class Incidents_Scrub(BaseModel):
	run_date_time = DateTimeField(null = True)
	candidates = IntegerField(null = True)
	related_candidates = IntegerField(null = True)
	scrub_type = CharField(null = True)
	scrub_type_id = IntegerField(null = True)
	search_keywords = CharField(null = True)

class Incidents_SourceCandidate(BaseSource):
	scrub = ForeignKeyField(Incidents_Scrub, related_name='Candidates')
	search_feed_id = CharField(null = True)
	search_feed_url = TextField(null = True)
	search_feed_text = TextField(null = True)
	search_feed_json = TextField(null = True)

class Incidents_Error(BaseModel):
	error_date_time = DateTimeField(null = True)
	error_code = IntegerField(null = True)
	file_name = CharField(null = True)
	error_text = TextField(null = True)
	call_stack = TextField(null = True)
	associated_url = CharField(null = True)
	associated_source_candidate_id = IntegerField(null=True)
	associated_scrub_id = IntegerField(null=True)

if not (Incidents_SourceCandidate.table_exists()):
	with database:
		Incidents_SourceCandidate.create_table()

#transfer_to_django()

#def transfer_to_django():
#	isc_query = IncidentSourceCandidate.select().where(IncidentSourceCandidate.IsRelated == True)
#	for isc in isc_query:
#		dj_is = Incidents_IncidentSource.create(url=isc.URL, site_name=isc.Name, domain=isc.Domain, article_title=isc.ArticleTitle, article_text=isc.ArticleText, is_related=isc.IsRelated)
#		dj_is.save()

#if not (Incidents_Incident.table_exists() and Incidents_IncidentSource.table_exists()):
#	database.create_tables([Incident, IncidentSource])