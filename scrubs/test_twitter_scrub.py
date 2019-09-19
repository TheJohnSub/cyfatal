from django_models import *
from twitter_scrub import *
import pytest

def test_contains_nonTwitter_domain_true():
	test_url = 'https://www.nydailynews.com/new-york/nyc-crime/ny-metro-bicyclist-killed-hit-run-20181214-story.html'
	test_dict = {'expanded_url': 'test_url', 'other_junk': 'www.twitter.com'}
	test_dict_2 = {'expanded_url': 'www.facebook.com', 'other_junk': 'www.twitter.com'}
	test_list = [test_dict, test_dict_2]
	assert contains_nonTwitter_domain(test_list) == True

def test_contains_nonTwitter_domain_false():
	test_dict = {'expanded_url': 'www.twitter.com/TheJohnSub', 'other_junk': 'www.twitter.com'}
	test_dict_2 = {'expanded_url': 'www.facebook.com', 'other_junk': 'www.twitter.com'}
	test_list = [test_dict, test_dict_2]
	assert contains_nonTwitter_domain(test_list) == False

def test_get_expanded_url():
	test_url = 'https://www.nydailynews.com/new-york/nyc-crime/ny-metro-bicyclist-killed-hit-run-20181214-story.html'
	test_dict = {'expanded_url': test_url, 'other_junk': 'www.twitter.com'}
	test_dict_2 = {'expanded_url': 'www.facebook.com', 'other_junk': 'www.twitter.com'}
	test_list = [test_dict, test_dict_2]
	assert get_expanded_url(test_list) == test_url

def test_load_config_file():
	config_parse = load_config_file('test_config.ini')
	assert config_parse.get('test', 'test_value') == 'this_is_a_successful_test'

def test_get_twitter_api_creds_success():
	config_parse = load_config_file('config.ini')	
	ts = get_twitter_api_creds(config_parse)

def test_get_twitter_api_creds_exception():
	config_parse = load_config_file('test_config.ini')
	with pytest.raises(Exception):
		ts = get_twitter_api_creds(config_parse)

def test_is_url_in_dataset_false():
	assert is_url_in_dataset('www.asdfsdafsdfgt43322.com') == False

def test_is_url_in_dataset_true():
	url = 'https://www.abc15.com/news/region-southeast-valley/tempe/bicyclist-struck-killed-near-52nd-street_broadway-road-in-tempe'
	assert is_url_in_dataset(url) == True

def test_filter_twitter_search_resp():
	assert len(filter_twitter_search_resp(test_resp)) == 2


test_resp = {
'content': {
	'search_metadata': {
		'completed_in': 0.106,
		'count': 100,
		'max_id': 1079141008175259650,
		'max_id_str': '1079141008175259650',
		'next_results': '?max_id=1076072637397377023&q=bicyclist%20killed&lang=en&count=100&include_entities=1',
		'query': 'bicyclist+killed',
		'refresh_url': '?since_id=1079141008175259650&q=bicyclist%20killed&lang=en&include_entities=1',
		'since_id': 0,
		'since_id_str': '0'},
	'statuses': [
		{
			"created_at": "Mon May 06 20:01:29 +0000 2019",
			"id": 1125490788736032770,
			"id_str": "1125490788736032770",
			"text": "Today's new update means that you can finally add Pizza Cat to your Retweet with comments! Learn more about this ne… https://t.co/Rbc9TF2s5X",
			"entities": {
				"hashtags": [],
				"symbols": [],
				"user_mentions": [],
				"urls": [
					{
						"url": "https://t.co/Rbc9TF2s5X",
						"expanded_url": "https://google.com/i/web/status/1125490788736032770",
						"display_url": "google.com/i/web/status/1…"
					},
				]
			},
		},
		{
			"created_at": "Mon May 06 20:01:29 +0000 2019",
			"id": 1125490788736032770,
			"id_str": "1125490788736032770",
			"text": "Today's new update means that you can finally add Pizza Cat to your Retweet with comments! Learn more about this ne… https://t.co/Rbc9TF2s5X",
			"entities": {
				"hashtags": [],
				"symbols": [],
				"user_mentions": [],
				"urls": [
					{
						"url": "https://t.co/Rbc9TF2s5X",
						"expanded_url": "https://nbc.com/i/web/status/1125490788736032770",
						"display_url": "nbc.com/i/web/status/1…"
					},
				]
			},
		},
		{
			"created_at": "Sat May 04 15:00:33 +0000 2019",
			"id": 1124690280777699328,
			"id_str": "1124690280777699328",
			"text": "If you're at #Pycon2019 and you use Twitter data or the Twitter API with your code, we are running an Open Space in… https://t.co/mVLIzEr9Gx",
			"entities": {
				"symbols": [],
				"user_mentions": [],
				"urls": [
					{
						"url": "https://t.co/mVLIzEr9Gx",
						"expanded_url": "https://twitter.com/i/web/status/1124690280777699328",
						"display_url": "twitter.com/i/web/status/1…"
					}
				]
  			},
			"in_reply_to_status_id": None,
			"in_reply_to_status_id_str": None,
			"in_reply_to_user_id": None,
			"in_reply_to_user_id_str": None,
			"in_reply_to_screen_name": None
		}
	]
}
}