from ViewsLibraries import *
from Choices import *
from .search import search
from .forms import *

# Create your views here.

# ________ HTTP ERRORS____________________
def error_401(request):
    requestOrigin = request.get_full_path()
    return render(request, 'snippets/snip_error_http.html', {
        'origin': requestOrigin,
        'pageName': '401',
    })

def error_403(request):
    requestOrigin = request.get_full_path()
    return render(request, 'snippets/snip_error_http.html', {
        'origin': requestOrigin,
        'pageName': '403',
    })

def error_404(request):
    requestOrigin = request.get_full_path()
    return render(request, 'snippets/snip_error_http.html', {
        'origin': requestOrigin,
        'pageName': '404',
    })

def error_405(request):
    requestOrigin = request.get_full_path()
    return render(request, 'snippets/snip_error_http.html', {
        'origin': requestOrigin,
        'pageName': '405',
    })

def error_500(request):
    requestOrigin = request.get_full_path()
    return render(request, 'snippets/snip_error_http.html', {
        'origin': requestOrigin,
        'pageName': '500',
    })



#________ USER AUTHENTICATION __________

def userlogin(request):
    return render(request, 'masters/login.html')

def userauth(request):
    session_username = request.POST['username']
    session_password = request.POST['password']
    user = authenticate(request, username=session_username, password=session_password)
    if user is not None:
        login(request, user)
        return redirect('/i/sys/')
    else:
        return render(request, 'snippets/snip_error_http.html', {
            'pageName': '500',
        })





#______________ MAIN SITE ________________

def home(request):
    # if request.LANGUAGE_CODE !=
    persons = Person.objects.filter(status='p').order_by('name')
    projects = Project.objects.filter(status='p').filter(featured=True)
    docs = Article.objects.filter(status='p').order_by('-publishedDate')
    total = projects.count()
    grid = 'col-lg-4 col-md-4 col-sm-12'
    return render(request, 'Website/index.html', {
        'pageName': 'home',
        'persons': persons,
        'projects': projects,
        'docs': docs,
        'project_max': 3,
        'doc_max': 4,
        'grid': grid,
    })

def about(request):
    people = Person.objects.filter(administrator=True).order_by('name')
    total = people.count()
    if total%3 == 0:
        grid = 'col-lg-4 col-md-4 col-sm-12'
    elif total%2 == 0:
        grid = 'col-lg-3 col-md-3 col-sm-12'
    else:
        grid = 'col-lg-4 col-md-4 col-sm-12'
    return render(request, 'Website/about.html', {
        'pageName': 'about',
        'people': people,
        'totalPeople': total,
        'grid': grid,
    })

def projects(request):
    projects = Project.objects.filter(status='p').order_by('-publishedDate')
    featured = Project.objects.filter(status='p').filter(featured=True)
    total = projects.count()

    grid = 'col-lg-4 col-md-4 col-sm-12'

    # This condition is not relevant yet
    # will check for something else later
    if total%3 == 0:
        grid = 'col-lg-4 col-md-4 col-sm-12'

    return render(request, 'Website/portfolio.html', {
        'page': 'portfolio_home',
        'projects': projects,
        'featured': featured,
        'featuredTotal': featured.count(),
        'project_max': 1000,
        'featured_max': 3,
        'grid': grid,
    })

def project_detail(request, keyword):
    try:
        project = Project.objects.get(slug=keyword)
        try:
            photos = Photo.objects.filter(projectName=project.id)
        except Photo.DoesNotExist:
            raise Http404("No photos")
    except Project.DoesNotExist:
        raise Http404('No Project')
    return render(request, 'Website/portfolio.html', {
        'page': 'portfolio_detail',
        'project': project,
        'client': project.client,
        'title': project.title,
        'type': project.type,
        'artwork': project.artwork.url,
        'description': project.description,
        'photos': photos,
    })

def process(request):
    return render(request, 'Website/process.html')

def services(request):
    form=clientForm
    return render(request, 'Website/services.html', {
        'form': form })

def articles(request):
    articles = Article.objects.filter(status='p').order_by('-publishedDate')
    return render(request, 'Website/articles.html', {
        'page': 'articles_home',
        'articles': articles,
        'articles_max': 100,
    })

def article_single(request, keyword):

    relatedArticles = Article.objects.filter(status='p').order_by('-publishedDate')

    try:
        article = Article.objects.get(slug=keyword)
        authorID = article.author_id
        authorTotal = Article.objects.filter(author=authorID).filter(status='p').count()
    except Article.DoesNotExist:
        raise Http404('404 - Article not found')

    return render(request, 'Website/articles.html', {
        'page': 'articles_single',
        'article': article,
        'title': article.title,
        'content': article.content,
        'author': article.get_author(),
        'authorSlug': article.author.slug,
        'authorID': article.author_id,
        'authorPhoto': article.author.photo.url,
        # 'authorBio': article.author.author_bio,
        'authorTotal': authorTotal,
        'date': article.publishedDate,
        'id': article.id,
        'relatedArticles': relatedArticles,
    })


#----------- SEARCH ----------------
# Check Website/search.py



#--------- REDIRECTS --------------
def azinca(request):
    return redirect('https://www.youtube.com/channel/UCxAIq85nPCo1whr8KYwVJkA')
def ekletik(request):
    return redirect('https://ekletik.com')