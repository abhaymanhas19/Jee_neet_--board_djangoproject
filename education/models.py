from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class PageModel(models.Model):
    page_id = models.CharField(max_length=20)
    position = models.IntegerField(_("Position"),null=True,blank=True)

    class Meta:
        abstract = True


class Section(PageModel):
    number = models.IntegerField(_("Section Number"))
    image = models.ImageField(
        _("Image"), null=True, upload_to="media", blank=True, help_text="Add a section image if required"
    )
    title = models.CharField(_("Section Title"), max_length=200, null=True, blank=True)
    description = models.TextField(_("Description"), null=True, blank=True)
    short_description = models.TextField(_("Short Description"), null=True, blank=True)

    class Meta:
        unique_together = (
            "page_id",
            "number",
        )

    def __str__(self) -> str:
        return f"{self.number}-{self.title}"


class CourseCategory(PageModel):
    name = models.CharField(_("Name"), max_length=100)

    class Meta:
        ordering = ("position",)
        unique_together = (
            "page_id",
            "position",
        )

    def __str__(self) -> str:
        return self.name


class Course(PageModel):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        CourseCategory, on_delete=models.SET_NULL, null=True, blank=False
    )
    description = RichTextField()
    
    class Meta:
        ordering = ("position",)
        unique_together = (
            "page_id",
            "position",
        )

    def __str__(self):
        return self.name


class HistoricalData(PageModel):
    title = models.CharField(_("Title"), max_length=50)
    value = models.IntegerField(_("Value"), default=0)

    class Meta:
        ordering = ("position",)
        unique_together = (
            "page_id",
            "position",
        )

    def __str__(self) -> str:
        return f"{self.position}-{self.title}"


class StaffDetail(PageModel):
    image = models.ImageField(_("Expert Image"),upload_to="media", null=True, blank=True)
    name = models.CharField(_("Name"), max_length=100)
    subject = models.CharField(_("Subject"), max_length=100)
    education = models.CharField(_("Education"), max_length=100)
    experience = models.CharField(_("Experience"), max_length=100)
    class Meta:
        ordering = ("position",)
        unique_together = (
            "page_id",
            "position",
        )

    def __str__(self) -> str:
        return self.name


class Testimonial(PageModel):
    image = models.ImageField(_("Student Image"),upload_to="media",  null=True, blank=True)
    name = models.CharField(_("Student Name"), max_length=20)
    testimonial = models.TextField(_("Student Testinonial"))
    additional_detail = models.TextField(
        _("Additional Detail"),
        null=True,
        blank=True,
        help_text=_("Exams appreared, rank scored etc"),
    )

    class Meta:
        ordering = ("position",)
        unique_together = (
            "page_id",
            "position",
        )

    def __str__(self) -> str:
        return self.name


class SampleVideo(PageModel):
    link = models.URLField(_("Video urls"))
    class Meta:
        ordering = ("position",)
        unique_together = (
            "page_id",
            "position",
        )

    def __str__(self) -> str:
        return self.link


class ContactUs(PageModel):
    name = models.CharField(_("Name"), max_length=20)
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Phone Number"), max_length=12)
    type = models.CharField(_("Type"), max_length=20)
    message = models.TextField(_("Message"))
    
    class Meta:
        ordering = ("position",)
        unique_together = (
            "page_id",
            "position",
        )

    def __str__(self) -> str:
        return self.email


class Lead(PageModel):
    name = models.CharField(_("Full Name"), max_length=20)
    email = models.EmailField(_("Email"))
    phone = models.CharField(_("Phone Number"), max_length=12)
    class Meta:
        ordering = ("position",)
        unique_together = (
            "page_id",
            "position",
        )

    def __str__(self) -> str:
        return self.email


class FAQ(PageModel):
    question = models.TextField(_("Question"))
    reply = models.TextField(_("Reply"))


    class Meta:
        ordering = ("position",)
        unique_together = (
            "page_id",
            "position",
        )

    def __str__(self):
        return self.question




class SiteLogo(PageModel):
    header_logo = models.ImageField(
        _("Header Logo"),upload_to="media" ,null=True, blank=True, help_text="Add header logo"
    )
    footer_logo = models.ImageField(
        _("Footer Logo logo"), upload_to="media", null=True, blank=True, help_text="Add footer logo"
    )