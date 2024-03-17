import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=64)),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="books",
                        to="library.genre",
                    ),
                ),
            ],
        ),
    ]