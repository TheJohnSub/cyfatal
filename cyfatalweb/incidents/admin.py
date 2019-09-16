from django.contrib import admin
from .models import Incident, IncidentSource, Scrub

class IncidentSourceInline(admin.StackedInline):
	model = IncidentSource
	extra = 1

class IncidentAdmin(admin.ModelAdmin):
	#inlines = [IncidentSourceInline]
	list_display = ('victim_name_col', 'city', 'state', 'incident_date_time')

	def victim_name_col(self,obj):
		return obj.get_name()
	victim_name_col.short_description = 'Victim Name'

	fieldsets = [
		(None, {'fields': ['incident_date_time', ('city', 'state', 'zip_code', 'coordinates'), ('hit_and_run', 'impaired_driving'), ('notes')]}),
		('Victim Information', {'fields': [('victim_name', 'victim_gender', 'victim_age')]}),
		('Motorist Information', {'fields': [('motorist_name', 'motorist_gender', 'motorist_age')]}),
		('Vehicle Information', {'fields': [('vehicle_type', 'vehicle_make', 'vehicle_model')]})
    ]
	readonly_fields = ['id']

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
	
	fieldsets = [
		('Website', {'fields': [('url', 'site_name', 'domain')]}),
		('Article', {'fields': ['article_title', 'article_text']}),
		('Review', {'fields': [('is_related', 'is_not_USA', 'is_reviewed', 'Incident'), ('notes')]})
	]
	actions = [mark_not_in_usa, mark_reviewed]

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



admin.site.register(Incident, IncidentAdmin)
admin.site.register(IncidentSource, IncidentSourceAdmin)
admin.site.register(Scrub, ScrubAdmin)

