from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name = "samrat",
        email = "pudasaini.samrat@gmail.com",
        is_staff = True,
        is_superuser = True,
        phone = "9860123456",
        gender= "Male"
        )
        user.set_password("samrat9860")
        user.save()

    dependencies = [

    ]

    operations = [
        migrations.RunPython(seed_data)
    ]