# Generated by Django 4.2.3 on 2023-08-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("education", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="contactus",
            name="position",
            field=models.IntegerField(blank=True, null=True, verbose_name="Position"),
        ),
        migrations.AddField(
            model_name="course",
            name="position",
            field=models.IntegerField(blank=True, null=True, verbose_name="Position"),
        ),
        migrations.AddField(
            model_name="coursecategory",
            name="position",
            field=models.IntegerField(blank=True, null=True, verbose_name="Position"),
        ),
        migrations.AddField(
            model_name="faq",
            name="position",
            field=models.IntegerField(blank=True, null=True, verbose_name="Position"),
        ),
        migrations.AddField(
            model_name="lead",
            name="position",
            field=models.IntegerField(blank=True, null=True, verbose_name="Position"),
        ),
        migrations.AddField(
            model_name="samplevideo",
            name="position",
            field=models.IntegerField(blank=True, null=True, verbose_name="Position"),
        ),
        migrations.AddField(
            model_name="section",
            name="position",
            field=models.IntegerField(blank=True, null=True, verbose_name="Position"),
        ),
        migrations.AddField(
            model_name="sitelogo",
            name="position",
            field=models.IntegerField(blank=True, null=True, verbose_name="Position"),
        ),
        migrations.AddField(
            model_name="staffdetail",
            name="position",
            field=models.IntegerField(blank=True, null=True, verbose_name="Position"),
        ),
        migrations.AddField(
            model_name="testimonial",
            name="position",
            field=models.IntegerField(blank=True, null=True, verbose_name="Position"),
        ),
        migrations.AlterField(
            model_name="historicaldata",
            name="position",
            field=models.IntegerField(blank=True, null=True, verbose_name="Position"),
        ),
    ]
