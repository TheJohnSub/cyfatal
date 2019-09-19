import sys
sys.path.append('source_recognition')
from source_recognition import *
from django_models import *

def test_source_is_related_title():
	test_source = Incidents_SourceCandidate()
	test_source.article_title = 'Bicyclist killed on 101 Freeway in Studio City; lanes closed for investigation'
	test_source.article_text = 'Some text in the source'	
	assert source_is_related(test_source) == True

def test_source_is_related_text():
	test_source = Incidents_SourceCandidate()
	test_source.article_title = 'Some text in the title'
	test_source.article_text = 'A 64-year-old bicyclist was killed Tuesday afternoon in a collision with a car at a Lake Elsinore intersection. The crash happened just before 4 p.m. at Railroad Canyon Road and Carnation Way. A Honda Civic was being driven east on Railroad Canyon when it collided with the bicycle, which was northbound on Carnation, a Riverside County Sheriff\'s Department news release said. The driver was not injured. The bicyclist, who was a resident of Menifee, had not been publicly identified as of Wednesday afternoon. Anyone with information on the collision is asked to call Deputy Willow at 951-245-3300'
	assert source_is_related(test_source) == True

def test_source_is_unrelated_title():
	test_source = Incidents_SourceCandidate()
	test_source.article_title = 'Bicyclist who killed man arrested at Tampa airport, police said'
	test_source.article_text = 'Some text in the source'	
	assert source_is_related(test_source) == False

def test_source_is_unrelated_text():
	test_source = Incidents_SourceCandidate()
	test_source.article_title = 'Some text in the title'
	test_source.article_text = 'A 22-year-old woman was under the influence of a narcotic when she struck and injured a bicyclist Wednesday night, Houston police said. Jacqueline Cruz has been charged with of driving while intoxicated. The bicyclist, a 60-year-old man, is in critical condition at Ben Taub Hospital, Houston police said Thursday. TEENS DEAD: 14-year-old charged in racing crash that killed two Cruz was driving a beige Nissan Altima westbound in the 6300 block of Griggs about 9:35 p.m. Wednesday when she struck the man, who was headed south on Buford. The bicyclist failed to yield the right of way to the driver, police said. Cruz stayed at the scene. Testing determined she was under the influence of a narcotic, police said.'	
	assert source_is_related(test_source) == False