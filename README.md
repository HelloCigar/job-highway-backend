# JobHighway

> We have JobStreet. How about a faster one? JobHighway, perhaps?

A full stack job posting web app built with **Nuxt 3** and **Django REST Framework**. This is the **backend** repo (Django), deployed on **Railway**.

Technologies used:
 - [Django](https://www.djangoproject.com/) for managing requests and making communication with the database easier.
 - [Django REST framework](https://www.django-rest-framework.org/) for providing the REST API on top of Django.
 - [PostgreSQL](https://www.postgresql.org/), the database hosted on Railway, managed by Django.

**Note: Some endpoints can only be accessed with valid auth tokens, such as delete/edit.**
API endpoints:
- **root**: https://job-highway-backend-production.up.railway.app/api/v1

- `[root]/jobs/`
- `[root]/jobs/categories/`
- `[root]/jobs/newest/`
- `[root]/jobs/[id]/`
- `[root]/jobs/[id]/delete/`
- `[root]/jobs/[id]/edit/`
- `[root]/jobs/my-jobs/`
- `[root]/jobs/create/`
