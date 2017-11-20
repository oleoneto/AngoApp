from ViewsLibraries import *
from .models import *





# SEARCH in Articles
def SearchArticles(keyword, request):
    try:
        articles = Article.objects.filter(title__icontains=keyword).filter(status='p')
        if not articles:
            articles = Article.objects.filter(slug__icontains=keyword).filter(status='p')
            if not articles:
                articles = Article.objects.filter(content__icontains=keyword).filter(status='p')
                if not articles:
                    articles = Article.objects.filter(summary__icontains=keyword).filter(status='p')
                    if not articles:
                        articles = Article.objects.filter(author__name__icontains=keyword).filter(status='p')
                        if not articles:
                            articles = Article.objects.filter(author__bio__icontains=keyword).filter(status='p')
    except Article.DoesNotExist:
        error = True
        raise Http404('No Article')
    return articles


#--------------------------------------


# SEARCH in PEOPLE
def SearchPeople(keyword):
    try:
        people = Person.objects.filter(name__icontains=keyword)
    except Person.DoesNotExist:
        error = True
        raise Http404('No Person')
    return people


#---------------------------------------


# SEARCH in PROJECTS
def SearchProjects(keyword):
    try:
        projects = Project.objects.filter(title__icontains=keyword).filter(status='p')
        if not projects:
            projects = Project.objects.filter(description__icontains=keyword).filter(status='p')
            if not projects:
                projects = Project.objects.filter(author__name__icontains=keyword).filter(status='p')
    except Person.DoesNotExist:
        error = True
        raise Http404('No Project')
    return projects




##############################################

def search(request):
    if request.POST:
        requestKeyword = request.POST['keyword']
        articles = SearchArticles(requestKeyword, request)
        people = SearchPeople(requestKeyword)
        projects = SearchProjects(requestKeyword)
        user = 'user'
        error = False
        totalresults = articles.__len__()+people.__len__()+projects.__len__()
    else:
        return redirect('/')
    if(articles.__len__() == 1):
        if not projects:
            return redirect('/articles/{}'.format(articles[0].slug))
    elif(projects.__len__() == 1):
        if not articles:
            return redirect('/portfolio/{}'.format(projects[0].slug))

    return render(request, 'masters/search.html', {
        'main': 'Pesquisar',
        'pageName': 'Search',
        'r': requestKeyword,
        'error': error,
        'search': request.POST['keyword'],
        'articles': articles,
        'people': people,
        'projects': projects,
        'user': user,
        'total': totalresults,
    })

#####################################################