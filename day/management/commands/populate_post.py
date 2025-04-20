from typing import Any
from day.models import Post, Cate
from django.core.management import BaseCommand
import random 

class Command(BaseCommand):
    help = "Populate or update posts"
    
    def handle(self, *args, **options):
        titles = [
            "Paracetamol", "Insulin Injection", "Antiseptic Cream", "Cough Syrup",
            "Bandages", "Vitamin Supplements", "Pain Relief Gel",
            "Blood Pressure Monitor", "Hand Sanitizer", "Digital Thermometer",
            "Antibiotic Ointment", "Cold Tablets", "Nebulizer", "First Aid Kit",
            "Glucometer", "Stethoscope", "Surgical Mask", "Pulse Oximeter",
            "Cough Lozenges", "Oral Rehydration Salts", "Hand Gloves", 
            "Antacid Tablets", "Hot Water Bag", "Ear Drops",
            "Eye Drops", "Wound Dressing", "Face Shield", "Sanitizing Wipes",
            "Digital Weighing Scale", "Medical Scissors"
        ]
        
        prices = [
            "Rs 200", "Rs 800", "Rs 600", "Rs 1200",
            "Rs 150", "Rs 500", "Rs 300", "Rs 2000",
            "Rs 100", "Rs 750", "Rs 400", "Rs 250",
            "Rs 1500", "Rs 1000", "Rs 1800", "Rs 2500",
            "Rs 50", "Rs 2200", "Rs 100", "Rs 80",
            "Rs 200", "Rs 300", "Rs 150", "Rs 120",
            "Rs 180", "Rs 350", "Rs 200", "Rs 250",
            "Rs 700", "Rs 500"
        ]
        
        img_urls = [
            "https://picsum.photos/id/12/200/300",
            "https://picsum.photos/id/13/200/300",
            "https://picsum.photos/id/14/200/300",
            "https://picsum.photos/id/15/200/300",
            "https://picsum.photos/id/16/200/300",
            "https://picsum.photos/id/17/200/300",
            "https://picsum.photos/id/18/200/300",
            "https://picsum.photos/id/9/200/300",
            "https://picsum.photos/id/10/200/300",
            "https://picsum.photos/id/11/200/300", 
            "https://picsum.photos/id/12/200/300",
            "https://picsum.photos/id/13/200/300",
            "https://picsum.photos/id/14/200/300",
            "https://picsum.photos/id/15/200/300",
            "https://picsum.photos/id/16/200/300",
            "https://picsum.photos/id/17/200/300",
            "https://picsum.photos/id/18/200/300",
            "https://picsum.photos/id/9/200/300",
            "https://picsum.photos/id/10/200/300",
            "https://picsum.photos/id/11/200/300",
        ]

        categories = Cate.objects.all()

        for title, price, img_url in zip(titles, prices, img_urls):
            category = random.choice(categories)

            # Ensure only one entry per title
            Post.objects.filter(title=title).delete()
            
            # Create a new post
            Post.objects.create(
                title=title,
                price=price,
                img_url=img_url,
                cate=category
            )

            self.stdout.write(self.style.SUCCESS(f"Updated post: {title}"))

        self.stdout.write(self.style.SUCCESS("Completed inserting/updating Data!"))
