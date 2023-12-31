# Generated by Django 4.2.3 on 2023-07-17 07:16

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_id", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=20, verbose_name="Name")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("phone", models.CharField(max_length=12, verbose_name="Phone Number")),
                ("type", models.CharField(max_length=20, verbose_name="Type")),
                ("message", models.TextField(verbose_name="Message")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CourseCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_id", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="FAQ",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_id", models.CharField(max_length=20)),
                ("question", models.TextField(verbose_name="Question")),
                ("reply", models.TextField(verbose_name="Reply")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Lead",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_id", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=20, verbose_name="Full Name")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("phone", models.CharField(max_length=12, verbose_name="Phone Number")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SampleVideo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_id", models.CharField(max_length=20)),
                ("link", models.URLField(verbose_name="Video urls")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SiteLogo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_id", models.CharField(max_length=20)),
                (
                    "header_logo",
                    models.ImageField(
                        blank=True,
                        help_text="Add header logo",
                        null=True,
                        upload_to="media",
                        verbose_name="Header Logo",
                    ),
                ),
                (
                    "footer_logo",
                    models.ImageField(
                        blank=True,
                        help_text="Add footer logo",
                        null=True,
                        upload_to="media",
                        verbose_name="Footer Logo logo",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="StaffDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_id", models.CharField(max_length=20)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="media",
                        verbose_name="Expert Image",
                    ),
                ),
                ("name", models.CharField(max_length=20, verbose_name="Name")),
                ("subject", models.CharField(max_length=50, verbose_name="Subject")),
                (
                    "education",
                    models.CharField(max_length=100, verbose_name="Education"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_id", models.CharField(max_length=20)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="media",
                        verbose_name="Student Image",
                    ),
                ),
                ("name", models.CharField(max_length=20, verbose_name="Student Name")),
                ("testimonial", models.TextField(verbose_name="Student Testinonial")),
                (
                    "additional_detail",
                    models.TextField(
                        blank=True,
                        help_text="Exams appreared, rank scored etc",
                        null=True,
                        verbose_name="Additional Detail",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Section",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_id", models.CharField(max_length=20)),
                ("number", models.IntegerField(verbose_name="Section Number")),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Add a section image if required",
                        null=True,
                        upload_to="media",
                        verbose_name="Image",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Section Title",
                    ),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="Description"),
                ),
                (
                    "short_description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Short Description"
                    ),
                ),
            ],
            options={
                "unique_together": {("page_id", "number")},
            },
        ),
        migrations.CreateModel(
            name="HistoricalData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_id", models.CharField(max_length=20)),
                ("position", models.IntegerField(unique=True, verbose_name="Position")),
                ("title", models.CharField(max_length=50, verbose_name="Title")),
                ("value", models.IntegerField(default=0, verbose_name="Value")),
            ],
            options={
                "ordering": ("position",),
                "unique_together": {("page_id", "position")},
            },
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("page_id", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=200)),
                ("description", ckeditor.fields.RichTextField()),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="education.coursecategory",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
