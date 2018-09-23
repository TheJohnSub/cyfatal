import datetime
from django.db import models
from django.utils import timezone

class Incident(models.Model):
    incident_date_time = models.DateTimeField(null = True, blank = True)
    city = models.CharField(null = True, max_length = 200, blank = True)
    state = models.CharField(null = True, max_length = 10, blank = True)
    zip_code = models.CharField(null = True, max_length = 10, blank = True)
    coordinates = models.CharField(null = True, max_length = 100, blank = True)
    victim_name = models.CharField(null = True, max_length = 200, blank = True)
    victim_gender = models.CharField(null = True, max_length = 10, blank = True)
    victim_age = models.IntegerField(null = True, blank = True)
    motorist_name = models.CharField(null = True, max_length = 200, blank = True)
    motorist_gender = models.CharField(null = True, max_length = 10, blank = True)
    motorist_age = models.IntegerField(null = True, blank = True)
    hit_and_run = models.NullBooleanField(null = True)
    impaired_driving = models.NullBooleanField(null = True)
    incident_type = models.CharField(null = True, max_length = 100, blank = True)
    vehicle_type = models.CharField(null = True, max_length = 100, blank = True)
    vehicle_make = models.CharField(null = True, max_length = 100, blank = True)
    vehicle_model = models.CharField(null = True, max_length = 100, blank = True)
    
    def get_name(self):
        if self.victim_name is not None and self.victim_name != '':
            return self.victim_name
        elif self.victim_age is not None and self.victim_age != '':
            return 'Unknown (Age: ' + str(self.victim_age) + ')'
        elif self.city is not None and self.state is not None and self.city != '' and self.state != '':
            return 'Unknown (' + self.city + ', ' + self.state + ')'
        else:
            return 'Unknown (ID: ' + str(self.id) + ')'

    def __str__(self):
        return self.get_name()




class IncidentSource(models.Model):
    url = models.CharField(null = True, max_length = 300)
    site_name = models.CharField(null = True, max_length = 200, blank = True)
    domain = models.CharField(null = True, max_length = 300, blank = True)
    article_title = models.TextField(null = True, blank = True)
    article_text = models.TextField(null = True, blank = True)
    is_related = models.NullBooleanField(null = True)
    is_not_USA = models.NullBooleanField(null = True)
    is_reviewed = models.NullBooleanField(null = False)
    source_candidate_id = models.IntegerField(null = True)
    Incident = models.ForeignKey(Incident, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.article_title

class Scrub(models.Model):
    run_date_time = models.DateTimeField(null = True)
    candidates = models.IntegerField(null = True)
    related_candidates = models.IntegerField(null = True)
    scrub_type = models.CharField(null = True, max_length = 100)
    scrub_type_id = models.IntegerField(null = True)
    search_keywords = models.CharField(null = True, max_length = 150)
    def __str__(self):
        return self.scrub_type + ' (' + self.run_date_time.strftime("%Y-%m-%d %H:%M:%S") + ')'