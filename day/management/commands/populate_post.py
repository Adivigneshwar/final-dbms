from typing import Any
from day.models import Post,Cate
from django.core.management import BaseCommand
import random 

class Command(BaseCommand):
    help="summa"
    def handle(self, *args, **options):
            titles=["Future of AI", "Smart Cities", "Space Exploration", "Quantum Computing", "Cybersecurity Trends", "Renewable Energy", "Gaming Evolution", "Biotech Innovations", "Social Media Impact", "AI in Workforce"]
            content=[
                "AI is transforming industries, automating tasks, and enhancing decision-making.",  
            "Smart cities integrate technology to improve infrastructure, transportation, and sustainability.",  
            "Space exploration advances with Mars missions, space tourism, and satellite innovations.",  
            "Quantum computing promises faster problem-solving for complex computations and encryption.",  
            "Cybersecurity trends focus on AI-driven threat detection and blockchain security.",  
            "Renewable energy adoption grows with solar, wind, and battery storage advancements.",  
            "Gaming evolution includes cloud gaming, virtual reality, and AI-generated content.",  
            "Biotech innovations enhance healthcare with gene editing, personalized medicine, and AI diagnostics.",  
            "Social media impact shapes public opinion, digital marketing, and personal privacy concerns.",  
            "AI in the workforce automates tasks, enhances productivity, and creates new job opportunities."
            ]
            img_url=[
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
            cate = Cate.objects.all()
            for title, content, img_url in zip(titles,content,img_url):
                catee=random.choice(cate)
                Post.objects.create(title=title,content=content,img_url=img_url,cate=catee)
            self.stdout.write(self.style.SUCCESS("Completed inserting Data!"))