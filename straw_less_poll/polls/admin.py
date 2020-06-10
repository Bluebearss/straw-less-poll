from django.contrib import admin
from .models import Question, Choice

# Changing the Admin Page titles
admin.site.site_header = "Straw_less Poll Admin"
admin.site.site_title = "Straw_less Poll Admin Area"
admin.site.index_title = "Welcome to the Straw_less Poll Admin Area"


# Choice Class that shows choices within the Question Model in an inline fashion.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# Question Admin Class that modifies the current Question Model to show the Choices under the Question and the Date info
# as a collapsible tab.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['publish_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


# Now allow admin to register a Question with this new modified Question model.
admin.site.register(Question, QuestionAdmin)
