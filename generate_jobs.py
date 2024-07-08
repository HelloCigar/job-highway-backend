import os
import django
import random


# Set up Django environment
os.environ['DJANGO_SETTINGS_MODULE'] = 'job_posting_backend.settings'
django.setup()


from datetime import datetime, timedelta
from django.contrib.auth.models import User
from job.models import Category, Job

# Sample data
categories = ['Engineering', 'Marketing', 'Design', 'Sales', 'Finance']
titles = ['Software Engineer', 'Marketing Specialist', 'Product Designer', 'Sales Manager', 'Financial Analyst']
descriptions = [
    'We are looking for a skilled professional.',
    'Join our dynamic team.',
    'Exciting opportunity in a growing company.',
    'Looking for a talented individual.',
    'Be a part of our success story.'
]
salaries = ['70k-90k', '50k-70k', '60k-80k', '80k-100k', '55k-75k']
locations = ['New York, NY', 'San Francisco, CA', 'Chicago, IL', 'Austin, TX', 'Seattle, WA']
company_names = ['TechCorp', 'MarketPro', 'DesignWorks', 'SalesForce', 'FinancePlus']
emails = ['hr@techcorp.com', 'jobs@marketpro.com', 'careers@designworks.com', 'apply@salesforce.com', 'recruitment@financeplus.com']

# Create categories
for cat in categories:
    Category.objects.get_or_create(title=cat)

# Generate and insert job data
for _ in range(50):  # Generate 50 jobs
    category = Category.objects.order_by('?').first()
    title = random.choice(titles)
    description = random.choice(descriptions)
    salary = random.choice(salaries)
    location = random.choice(locations)
    company_name = random.choice(company_names)
    company_location = random.choice(locations)
    company_email = random.choice(emails)
    created_at = datetime.now() - timedelta(days=random.randint(0, 365))
    created_by = User.objects.order_by('?').first()

    Job.objects.create(
        category=category,
        title=title,
        description=description,
        position_salary=salary,
        position_location=location,
        company_name=company_name,
        company_location=company_location,
        company_email=company_email,
        created_at=created_at,
        created_by=created_by
    )

print("Job data has been generated and inserted into the database.")
