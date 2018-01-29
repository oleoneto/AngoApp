from ViewsLibraries import *
from .models import Article, Project, Person


def SearchInArticles(keyword):

    tempArray = []
    articlesArray = []

    try:
        docsbyauthorname = Article.objects.filter(author__name__icontains=keyword)
        if docsbyauthorname:
            tempArray.append(docsbyauthorname)

        docsbyauthorslug = Article.objects.filter(author__slug__icontains=keyword)
        if docsbyauthorslug:
            tempArray.append(docsbyauthorslug)

        docsbyslug   = Article.objects.filter(slug__icontains=keyword)
        if docsbyslug:
            tempArray.append(docsbyslug)

        docsbytitle  = Article.objects.filter(title__icontains=keyword)
        if docsbytitle:
            tempArray.append(docsbytitle)

        docsbycontent = Article.objects.filter(content__icontains=keyword)
        if docsbycontent:
            tempArray.append(docsbycontent)

        for set in tempArray:
            for obj in set:
                if obj not in articlesArray:
                    articlesArray.append(obj)

    except Article.DoesNotExist:
        raise Http404()
    return articlesArray


def SearchInProjects(keyword):
    tempArray = []
    projectsArray = []

    try:
        projectsbyauthorname = Project.objects.filter(manager__name__icontains=keyword)
        if projectsbyauthorname:
            tempArray.append(projectsbyauthorname)

        projectsbyauthorslug = Project.objects.filter(manager__slug__icontains=keyword)
        if projectsbyauthorslug:
            tempArray.append(projectsbyauthorslug)

        projectsbyslug = Project.objects.filter(slug__icontains=keyword)
        if projectsbyslug:
            tempArray.append(projectsbyslug)

        projectsbytitle = Project.objects.filter(title__icontains=keyword)
        if projectsbytitle:
            tempArray.append(projectsbytitle)

        projectsbytype = Project.objects.filter(type__icontains=keyword)
        if projectsbytype:
            tempArray.append(projectsbytype)

        projectsbycontent = Project.objects.filter(description__icontains=keyword)
        if projectsbycontent:
            tempArray.append(projectsbycontent)

        for set in tempArray:
            for obj in set:
                if obj not in projectsArray:
                    projectsArray.append(obj)


    except Project.DoesNotExist:
        raise Http404()
    return projectsArray


def SearchInPeople(keyword):

    tempArray = []
    peopleArray = []

    try:
        peoplebyname = Person.objects.filter(name__icontains=keyword)
        if peoplebyname:
            tempArray.append(peoplebyname)

        peoplebyslug = Person.objects.filter(slug__icontains=keyword)
        if peoplebyslug:
            tempArray.append(peoplebyslug)

        # peoplebyposition = Person.objects.filter(position__icontains=keyword)
        # if peoplebyposition:
        #     tempArray.append(peoplebyposition)

        peoplebybio = Person.objects.filter(bio__icontains=keyword)
        if peoplebybio:
            tempArray.append(peoplebybio)

        # peoplebyauthorbio = Person.objects.filter(author_bio__icontains=keyword)
        # if peoplebyauthorbio:
        #     tempArray.append(peoplebyauthorbio)

        for set in tempArray:
            for obj in set:
                if obj not in peopleArray:
                    peopleArray.append(obj)


    except Person.DoesNotExist:
        raise Http404()
    return peopleArray


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

        docs     = SearchInArticles(searchTerm)
        docsTotal = docs.__len__()

        projects = SearchInProjects(searchTerm)
        projectsTotal = projects.__len__()

        people   = SearchInPeople(searchTerm)
        peopleTotal = people.__len__()

        totalResults = docsTotal + projectsTotal + peopleTotal

    else:
        return redirect('/')

    # if(docsTotal == 1):
    #     if not projects:
    #         return redirect('/docs/{}'.format(docs[0].slug))
    # elif(projectsTotal == 1):
    #     if not docs:
    #         return redirect('/portfolio/{}'.format(projects[0].slug))
    # elif(peopleTotal == 1):
    #     if Article.objects.filter(author_id=people[0].id):
    #         return redirect('/docs/autor/{}'.format(people[0].slug))


    return render(request, 'masters/search.html', {
        'main': 'Pesquisar',
        'pageName': 'Search',
        'search': searchTerm,
        'articles': docs,
        'people': people,
        'projects': projects,
        'total': totalResults,
    })