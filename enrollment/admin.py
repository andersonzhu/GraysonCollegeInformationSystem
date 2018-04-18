from django.contrib import admin
from .models import EnrollmentItemByYear

# Register your models here.
@admin.register(EnrollmentItemByYear)
class EnrollmentAdmin(admin.ModelAdmin):
  list_display=['semester', 'enrollment', 'attemptedCredits', 'contactHours']


# admin.site.register(EnrollmentItemByYear)