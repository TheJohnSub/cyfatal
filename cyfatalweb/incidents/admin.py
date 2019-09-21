from django.contrib import admin
from .models import Incident, IncidentSource, Scrub, Error
from django.urls import reverse
from django.utils.safestring import mark_safe


class IncidentSourceInline(admin.StackedInline):
	model = IncidentSource
	extra = 1

class IncidentAdmin(admin.ModelAdmin):
	list_display = ('victim_name_col', 'city', 'state', 'incident_date_time', 'related_sources_count')

	def victim_name_col(self,obj):
		return obj.get_name()
	victim_name_col.short_description = 'Victim Name'

	def related_sources_count(self, obj):
		count = IncidentSource.objects.filter(Incident=obj).count()
		return str(count)
	related_sources_count.short_description = 'Count'

	def related_sources(self, obj):
		if obj is None or obj.id is None:
			return "No related sources."
		list_str = ''
		for source in IncidentSource.objects.filter(Incident=obj):
			url = '/admin/incidents/incidentsource/' + str(source.id) + '/change/'
			link = '<a href="%s">%s | %s</a>' % (url, source.article_title, source.domain)
			list_str += link + '<br/>'
		return mark_safe(list_str)
	related_sources.short_description = 'Related Sources'

	fieldsets = [
		(None, {'fields': ['incident_date_time', ('city', 'state', 'zip_code', 'coordinates'), ('hit_and_run', 'impaired_driving'), ('notes')]}),
		('Victim Information', {'fields': [('victim_name', 'victim_gender', 'victim_age')]}),
		('Motorist Information', {'fields': [('motorist_name', 'motorist_gender', 'motorist_age')]}),
		('Vehicle Information', {'fields': [('vehicle_type', 'vehicle_make', 'vehicle_model')]}),
		('Sources', {'fields': [('related_sources')]})
    ]
	readonly_fields = ['related_sources_count', 'related_sources', 'id']

def mark_not_in_usa(modeladmin, request, queryset):
    queryset.update(is_not_USA=True)
mark_not_in_usa.short_description = "Mark as not in USA"

def mark_reviewed(modeladmin, request, queryset):
    queryset.update(is_reviewed=True)
mark_reviewed.short_description = "Mark as reviewed"


class IncidentSourceAdmin(admin.ModelAdmin):
	list_display = ('article_title', 'is_reviewed_col', 'domain', 'is_related_col', 'is_not_usa_col')
	list_filter = ("is_reviewed", "is_not_USA", "is_related")

	def is_reviewed_col(self, obj):
		return obj.is_reviewed
	is_reviewed_col.boolean = True
	is_reviewed_col.short_description = 'Reviewed'

	def is_related_col(self, obj):
		return obj.is_related
	is_related_col.boolean = True
	is_related_col.short_description = 'Related'

	def is_not_usa_col(self, obj):
		return obj.is_not_USA
	is_not_usa_col.boolean = True
	is_not_usa_col.short_description = 'Not USA'

	def url_go_button(self, obj):
		if obj is None or obj.url is None:
			return ''
		return mark_safe('<a href="%s" target="_blank">%s</a>' % (obj.url, obj.url))
	url_go_button.short_description = 'Link to Article'

	fieldsets = [
		('Website', {'fields': [('url', 'site_name', 'domain'), ('url_go_button')]}),
		('Article', {'fields': ['article_title', 'article_text']}),
		('Review', {'fields': [('is_related', 'is_not_USA', 'is_reviewed', 'Incident'), ('notes')]})
	]
	actions = [mark_not_in_usa, mark_reviewed]
	readonly_fields = ['url_go_button']


class ScrubAdmin(admin.ModelAdmin):
	list_display = ['scrub_type', 'search_keywords', 'run_date_time', 'related_candidates']
	def has_add_permission(self, request, obj=None):
		return False
	def has_delete_permission(self, request, obj=None):
		return False

	list_fields = Scrub._meta.get_fields()
	list_fields_str = []
	for field in list_fields:
		list_fields_str.append(field.name)

	readonly_fields = list_fields_str

class ErrorAdmin(admin.ModelAdmin):
	list_display = ['error_date_time', 'file_name', 'error_code', 'error_text', 'associated_url', 'associated_source_candidate_id', 'scrub_link', 'call_stack']
	

	def scrub_link(self, error):
		if error.associated_scrub_id is None:
			return "None"
		url = '/admin/incidents/scrub/' + str(error.associated_scrub_id) + '/change/'
		link = '<a href="%s">%s</a>' % (url, error.associated_scrub_id)
		return mark_safe(link)
	scrub_link.short_description = 'Associated Scrub ID'


	def has_add_permission(self, request, obj=None):
		return False
	def has_delete_permission(self, request, obj=None):
		return False

	fields = list_display

	readonly_fields = fields



admin.site.register(Incident, IncidentAdmin)
admin.site.register(IncidentSource, IncidentSourceAdmin)
admin.site.register(Scrub, ScrubAdmin)
admin.site.register(Error, ErrorAdmin)

