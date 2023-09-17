from django.contrib import admin

# Register your models here.
from .models import (
    Section,
    Course,
    HistoricalData,
    StaffDetail,
    Testimonial,
    ContactUs,
    Lead,
    FAQ,
    CourseCategory,
    SampleVideo,
    SiteLogo
)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display=('number', 'title', 'page_id')


@admin.register(SampleVideo)
class SampleVideoAdmin(admin.ModelAdmin):
    pass


@admin.register(HistoricalData)
class HistoricalDataAdmin(admin.ModelAdmin):
    list_display=('position','title', 'value')


@admin.register(StaffDetail)
class StaffDetailAdmin(admin.ModelAdmin):
    list_display=('position', 'name', 'subject')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    pass


@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone", "type", "message"]


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("page_id",)


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone"]


@admin.register(Course)
class CoursemodelAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "category"]




@admin.register(SiteLogo)
class SiteLogoAdmin(admin.ModelAdmin):
    list_display = ["id","page_id", "header_logo","footer_logo"]

  