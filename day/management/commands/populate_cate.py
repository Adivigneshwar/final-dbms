from typing import Any
from day.models import Cate
from django.core.management import BaseCommand


class Command(BaseCommand):
    help="summa"
    def handle(self, *args, **options):
           
            categories = [
            'Prescription Medicines',
            "Over-the-Counter (OTC) Medicines",
            "First Aid & Wound Care",
            "Medical Devices & Equipment",
            "Personal Protection & Hygiene",
            "Diabetes & Health Monitoring",
            "Mother & Baby Care"
]
           
            for cate_name in zip(categories):
                
                Cate.objects.create(name=cate_name)
            self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))