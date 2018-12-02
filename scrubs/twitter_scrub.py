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

def contains_nonTwitter_domain(urls):
    success = False
    url = get_expanded_url(urls)
    if (url.find('twitter.com') == -1):
        success = True
        return success

def get_expanded_url(urls):
    for url in urls:
        expanded_url = url['expanded_url']
        return expanded_url

def get_tweet_url(json_node):
    tweet_id = json_node['id_str']
    user_handle = json_node['user']['id_str']
    return 'https://www.twitter.com/' + user_handle + '/status/' + tweet_id

def run_tweet_scrub(keywords):
    print('Running scrub for keywords: ' + str(keywords))
    try:
        tso = TwitterSearchOrder() 
        tso.set_keywords(keywords) 
        tso.set_language('en') 
        tso.set_include_entities(True) 

        config_parse = configparser.ConfigParser()
        config_parse.read('config.ini')

        ts = TwitterSearch(
            consumer_key = config_parse.get('keys', 'consumer_key'),
            consumer_secret = config_parse.get('keys', 'consumer_secret'),
            access_token = config_parse.get('keys', 'access_token'),
            access_token_secret = config_parse.get('keys', 'access_token_secret'),
         )

        scrub = Incidents_Scrub(run_date_time=datetime.datetime.now(), scrub_type='Twitter', scrub_type_id=1, search_keywords=', '.join(keywords))
        scrub.save()

        mysearchResp = ts.search_tweets(tso)
        contentOnly = mysearchResp['content']['statuses']
        filter_resp = [x for x in contentOnly if len(x['entities']['urls']) > 0 and contains_nonTwitter_domain(x['entities']['urls'])]
        num_related = 0
        scrub.candidates = len(filter_resp)

        for candidate in filter_resp:
            twit_url = get_expanded_url(candidate['entities']['urls'])
            if Incidents_SourceCandidate.select().where(Incidents_SourceCandidate.url == twit_url).count() > 0:
                print('Continued on URL: ' + twit_url)
                continue

            g = Goose()
            article = None
            try:
                article = g.extract(url=twit_url)
                if (article.canonical_link is not None) and (article.canonical_link is not None):
                    twit_url = article.canonical_link
                    if Incidents_SourceCandidate.select().where(Incidents_SourceCandidate.url == twit_url).count() > 0:
                        print('Continued on URL: ' + twit_url)
                        continue
                twit_id = candidate['id']
                source_candidate = Incidents_SourceCandidate(url=twit_url, domain=urlparse(twit_url).netloc, article_text=article.cleaned_text, article_title=article.title, scrub=scrub, search_feed_id=twit_id, search_feed_url=get_tweet_url(candidate), search_feed_text=candidate['text'].encode('utf8'))
                source_candidate.article_title.replace("'","'")
                source_candidate.article_text.replace("'","'")
                source_candidate.search_feed_json = candidate
                if (article.opengraph is not None) and ('site_name' in article.opengraph):
                    source_candidate.site_name = article.opengraph['site_name']
                if source_is_related(source_candidate):
                    source_record = Incidents_IncidentSource(url=source_candidate.url, site_name=source_candidate.site_name, domain=source_candidate.domain, article_text=source_candidate.article_text, article_title=source_candidate.article_title, is_related=True)
                    source_record.is_reviewed = False
                    source_record.save()
                    source_candidate.is_related = True
                    num_related += 1
                source_candidate.article_title.encode('ascii', 'ignore')
                source_candidate.article_text.encode('ascii', 'ignore')
                source_candidate.save()
                print(source_candidate.search_feed_text.decode('UTF-8'))
            except Exception as e:
                print(twit_url)
                if article:
                    print(type(article.cleaned_text))
                print(e)

        scrub.related_candidates = num_related
        scrub.save()

    except TwitterSearchException as e:
        print(e)

    print()
    print('--------------------------------------')

file_name = sys.argv[1]
text_file = open(file_name, "r")
text_list = text_file.readlines()
for line in text_list:
    keywords = line.split()
    run_tweet_scrub(keywords)