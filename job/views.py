from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions

from .models import Job, Category
from .serializers import JobSerializer, JobDetailSerializer, CategorySerializer
from .forms import JobForm

class CategoriesView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class NewestJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all().order_by('-created_at')[:5]
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)


class JobDetailView(APIView):
    def get(self,request, pk, format=None):
        job = Job.objects.get(pk=pk)
        serializer = JobDetailSerializer(job)
        return Response(serializer.data)
    
class BrowseJobsView(APIView):
    def get(self,request, format=None):
        jobs = Job.objects.all()
        query = request.GET.get('query', '')
        # remove leading and trailing whitespaces
        query = query.strip()
        if query:
            jobs = jobs.filter(title__icontains=query) | jobs.filter(company_name__icontains=query) | jobs.filter(position_location__icontains=query)
        categories = request.GET.get('categories', '')
        if categories:
            jobs = jobs.filter(category_id__in=categories.split(','))
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

class MyJobsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        jobs = Job.objects.filter(created_by=request.user)
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)

class CreateJobView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        form = JobForm(request.data)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()
            return Response({'status': 'created'})
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        category = Category.objects.get(pk=request.data['category'])
        job = Job.objects.get(pk=pk, created_by=request.user)
        job.category = category
        job.save()
        if job:
            return Response({'status': 'updated'})
        
    def delete(self, request, pk):
        job = Job.objects.get(pk=pk, created_by=request.user)
        job.delete()
        return Response({'status': 'deleted'})