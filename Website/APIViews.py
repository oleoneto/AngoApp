from ViewsLibraries import *

"""

Written by Leo Neto
Updated on November 19, 2017

CRUD - Create (Post), Retrieve (Get), Update (Put) and Delete (Delete)

"""


#_____________ PERSON API

# GET all instances of Person
class PersonListAPIView(ListAPIView):
    queryset = Person.objects.filter(status='p')
    serializer_class = PersonSerializer

# GET a single instance of Person
class PersonDetailAPIView(RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


#_____________ PROJECTS API

# GET all instances of Portfolio Project
class ProjectListAPIView(ListAPIView):
    queryset = Project.objects.filter(status='p')
    serializer_class = ProjectSerializer

# GET a single instance of Portfolio Project
class ProjectDetailAPIView(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailAPIViewSlug(RetrieveAPIView):
    queryset = Project.objects.all()#.filter(status='p')
    serializer_class = ProjectSerializer
    lookup_field = ('slug')