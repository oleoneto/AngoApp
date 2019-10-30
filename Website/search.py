from ViewsLibraries import *
from django.db.models import Q
from .models import Article, Project, Person


def SearchInArticles(keyword):
    return Article.objects.filter(
        Q(author__name__icontains=keyword) |
        Q(author__slug__icontains=keyword) |
        Q(slug__icontains=keyword) |
        Q(title__icontains=keyword) |
        Q(content__icontains=keyword)
    )


def SearchInProjects(keyword):
    return Project.objects.filter(
        Q(manager__name__icontains=keyword) |
        Q(manager__slug__icontains=keyword) |
        Q(slug__icontains=keyword) |
        Q(title__icontains=keyword) |
        Q(type__icontains=keyword) |
        Q(description__icontains=keyword)
    )


def SearchInPeople(keyword):
    return Person.objects.filter(
        Q(name__icontains=keyword) |
        Q(slug__icontains=keyword) |
        Q(position__icontains=keyword) |
        Q(bio__icontains=keyword) |
        Q(author_bio__icontains=keyword)
    )

def SearchViewController(request):

    """
    :param request: HTTP Request
    :return: multiple arrays with all available model objects [note: return types are not QuerySets]
    """

    """
    Restricted access to the search results page for only when the HTTP Request is through a POST.
    If not the case, the browser should redirect to the homepage.
    """
    if request.POST:
        searchTerm = request.POST['keyword']
        articles = SearchInArticles(searchTerm)
        projects = SearchInProjects(searchTerm)
        people   = SearchInPeople(searchTerm)
        total = len(article) + len(projects) + len(people)
    else:
        return redirect('/')

    return render(request, 'masters/search.html', {
        'main': 'Pesquisar',
        'pageName': 'Search',
        'search': searchTerm,
        'articles': articles,
        'people': people,
        'projects': projects,
        'total': total,
    })
