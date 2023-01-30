# Generated by Django 4.1.3 on 2022-11-29 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CnabReader",
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
                ("tipo", models.CharField(max_length=13)),
                ("data", models.CharField(max_length=8)),
                ("valor", models.IntegerField()),
                ("cpf", models.CharField(max_length=11)),
                ("cartao", models.CharField(max_length=12)),
                ("hora", models.CharField(max_length=8)),
                ("dono", models.CharField(max_length=14)),
                ("loja", models.CharField(max_length=19)),
            ],
        ),
        migrations.CreateModel(
            name="UploadFile",
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
                ("cnab_file", models.FileField(upload_to="uploads")),
            ],
        ),
    ]
