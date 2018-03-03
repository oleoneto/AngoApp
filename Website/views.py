from ViewsLibraries import *
from Choices import *
from .search import SearchViewController
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage


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
    people = Person.objects.filter(administrator=True).order_by('-name')
    partners = Partner.objects.order_by('name')

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
        'partners':partners,
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
    if request.POST:
        form = MessageForm(request.POST)
        if form.is_valid():
            first_name_from_html = request.POST['first_name']
            last_name_from_html = request.POST['last_name']
            email_from_html = request.POST['email']
            cellphone_from_html = request.POST['cellphone']
            content_from_html = request.POST['content']
            #message_from_html = request.POST['message']
            tipo_de_servico_from_html = request.POST['tipo_de_servico']


            message_object = Message(first_name=first_name_from_html, last_name=last_name_from_html
                                     ,email=email_from_html,cellphone=cellphone_from_html,
                                     message=content_from_html,tipo_de_servico=tipo_de_servico_from_html)
            message_object.save()

            # #send email to the user
            subject = 'Contacto com a AngoApp'
            message = 'Obrigado por entrar em contacto com a AngoApp.'

            from_email = 'angoapp2016@gmail.com'
            message_from_client='tipo de servico: '+tipo_de_servico_from_html+'\nMENSAGEM: '+ content_from_html +'\n\n nome: '+first_name_from_html+' '+last_name_from_html+ '\n numero de telefone: ' + cellphone_from_html + '\nemail: ' + email_from_html
            try:
                #send notification to the client and to angoapp email
                email_to_client = EmailMessage(subject, message, to=[email_from_html])
                email_to_angoapp = EmailMessage('PEDIDO PELO WEBSITE',message_from_client, to=[from_email])
                email_to_client.send()
                email_to_angoapp.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/")
    else:
        form = MessageForm()
    return render(request, 'Website/services.html', {
        'form': form,
    })

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