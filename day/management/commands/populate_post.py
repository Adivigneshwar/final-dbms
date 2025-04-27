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
        
        # Just use numeric values without the "Rs" prefix
        prices = [
            200, 800, 600, 1200,
            150, 500, 300, 2000,
            100, 750, 400, 250,
            1500, 1000, 1800, 2500,
            50, 2200, 100, 80,
            200, 300, 150, 120,
            180, 350, 200, 250,
            700, 500
        ]
        
        # Use your local image files from the img directory
        img_urls = [
            "img/para.png", "img/insulin.jpg", "img/antoseptic.jpg", "img/syrup.jpg", "img/bandage.jpg", 
            "img/vitamin.jpg", "img/pain.jpg", "img/bp.jpg", "img/hand.jpg", 
            "img/digital.jpg", "img/antobiotic.jpg", "img/cold.jpg", "img/nebulizer.jpg", 
            "img/first.jpg", "img/Glucometer.jpg", "img/stethoscope.jpg", "img/mask.jpg","img/pulse.jpg", 
            "img/cough.jpg", "img/oral.jpg", "img/Hand Gloves.jpg", "img/Antacid Tablets.jpg","img/Hot Water Bag.jpg", 
            "img/Ear Drops.jpg", "img/Eye Drops.jpg", "img/Wound Dressing.jpg", "img/Face Shield.jpg","img/Sanitizing Wipes.jpg", 
            "img/Digital Weighing Scale.jpg", "img/Medical Scissors.jpg"
        ]
        
        # If you have more products than images, cycle through the images
        local_images = []
        for i in range(len(titles)):
            img_index = i % len(img_urls)
            local_images.append(img_urls[img_index])
        
        categories = Cate.objects.all()
        
        for title, price, img_path in zip(titles, prices, local_images):
            category = random.choice(categories)
            
            # Ensure only one entry per title
            Post.objects.filter(title=title).delete()
            
            # Create a new post with local image path
            Post.objects.create(
                title=title,
                price=price,  # Now using numeric values
                img_url=img_path,
                cate=category
            )
            
            self.stdout.write(self.style.SUCCESS(f"Updated post: {title} with image: {img_path}"))
        
        self.stdout.write(self.style.SUCCESS("Completed inserting/updating Data!"))