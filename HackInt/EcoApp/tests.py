from django.test import TestCase
from faker import Faker
from .models import User, Certification, Company, Supplier, ForumPost

# Create your tests here.
def generate_random_data(num):
    fake = Faker()
    
    for _ in range(num):
        # Create a User
        user = User.objects.create_user(username=fake.user_name(), password="testpassword", is_company=True)
        
        # Create a Company
        company = Company.objects.create(
            user=user,
            sustainability_score=fake.random_int(min=0, max=100),
            improvements_needed=fake.text()
        )
        
        # Create a Certification
        certification = Certification.objects.create(
            name=fake.company_suffix(),
            requirements=fake.text(),
            application_process=fake.text(),
            benefits=fake.text()
        )
        
        # Create a Supplier
        supplier = Supplier.objects.create(
            name=fake.company(),
            sustainable_products=fake.text()
        )
        
        # Create a Forum Post
        ForumPost.objects.create(
            title=fake.sentence(),
            content=fake.text(),
            company=company
        )

# # Call the function to generate 200 records
# generate_random_data(200)
