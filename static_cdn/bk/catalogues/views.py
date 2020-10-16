from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

from .models import School_photo_gallery
from .models import School_bog_chairperson
from .models import School_pta_chairperson
from .models import School_principal
from .models import School_dp_academics
from .models import School_dp_admin
from .models import School_languages_hod
from .models import School_math_hod
from .models import School_sciences_hod
from .models import School_humanities_hod
from .models import School_boarding_hod
from .models import School_games_hod
from .models import School_guiding_and_counseling_hod
from .models import School_technicals_hod
from .models import School_drama_club
from .models import School_music_club
from .models import School_sports_club
from .models import School_christian_union_club
from .models import School_muslim_students_club
from .models import School_journalism_club
from .models import School_debate_club
from .models import School_science_engineering_club
from .models import School_history
from .models import School_mission
from .models import School_vision
from .models import School_site_map
from .models import School_library
from .models import School_dining_hall
from .models import School_form_one_classes
from .models import School_form_two_classes
from .models import School_form_three_classes
from .models import School_form_four_classes
from .models import School_transport
from .models import School_physics_lab
from .models import School_chemistry_lab
from .models import School_biology_lab
from .models import School_computer_lab
from .models import School_fence
from .models import School_bakery
from .models import School_forest
from .models import School_car_park
from .models import School_generator
from .models import School_beautification
from .models import School_general_information
from .models import School_alumni
from .models import School_downloads
from .models import School_updates
from .models import School_core_values
from .models import School_anthem
from .models import School_performance
from .models import School_peace_club
from .models import School_languages_department
from .models import School_math_department
from .models import School_sciences_department
from .models import School_humanities_department
from .models import School_boarding_department
from .models import School_games_department
from .models import School_guiding_and_counseling_department
from .models import School_technicals_department
from .models import School_teachers
from .models import School_student_council
from .models import School_events

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
def index(request):
    # this is your new view
    gallery = School_photo_gallery.objects.all()
    updater = School_updates.objects.all()
    jane = School_events.objects.all()
    general = School_general_information.objects.filter()
    return render(request, 'index.html', {'gallery':gallery, 'updater':updater, 'jane':jane, 'general':general})


def contact(request):
    con = School_general_information.objects.all()
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            your_email = form.cleaned_data['your_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, your_email, ['info@kakamegaschool.sc.ke'], fail_silently=False)
            except BadHeaderError:
                return redirect('failure')
            return redirect('success')
    return render(request, "contact.html", {'con':con, 'form': form})

def successView(request):  
    sucks = School_general_information.objects.all()
    return render(request, "success.html", {'sucks': sucks})  

def errorView(request):  
    sucker = School_general_information.objects.all()
    return render(request, "success.html", {'sucker': sucker})      

def bog(request):
    # this is your new view
    bogchair = School_bog_chairperson.objects.filter()
    genea = School_general_information.objects.filter()
    return render(request, 'bog.html', {'bogchair':bogchair, 'genea':genea})

def pta(request):
    # this is your new view
    ptachair = School_pta_chairperson.objects.filter()
    geneap = School_general_information.objects.filter()
    return render(request, 'pta.html', {'ptachair':ptachair, 'geneap':geneap})

def principal(request):
    # this is your new view
    principal = School_principal.objects.filter()
    genepa = School_general_information.objects.filter()
    return render(request, 'principal.html', {'principal':principal, 'genepa':genepa})

def deputies(request):
    # this is your new view
    dpacademics = School_dp_academics.objects.filter()
    dpadmin = School_dp_admin.objects.all()
    genead = School_general_information.objects.filter()
    return render(request, 'deputies.html', {'dpacademics':dpacademics, 'dpadmin':dpadmin, 'genead':genead})

def teachers(request):
        # this is your new view
    teach = School_teachers.objects.filter()
    generiht = School_general_information.objects.filter()
    return render(request, 'teachers.html', {'teach':teach, 'generiht':generiht})

def students(request):
        # this is your new view
    study = School_student_council.objects.filter()
    generihs = School_general_information.objects.filter()
    return render(request, 'students.html', {'study':study, 'generihs':generihs})

def hods(request):
        # this is your new view
    langues = School_languages_hod.objects.all()
    scies = School_sciences_hod.objects.all()
    board = School_boarding_hod.objects.all()
    game = School_games_hod.objects.all()
    guide = School_guiding_and_counseling_hod.objects.all()
    hume = School_humanities_hod.objects.all()
    maths = School_math_hod.objects.all()
    tech = School_technicals_hod.objects.all()
    geneids = School_general_information.objects.filter()
    return render(request, 'hods.html', {'langues':langues, 'scies':scies, 'board':board, 'game':game, 'guide':guide, 'hume':hume, 'maths':maths, 'tech':tech, 'geneids':geneids})

def languages(request):
        # this is your new view
    ldep = School_languages_department.objects.all()
    geneil = School_general_information.objects.filter()
    return render(request, 'deplang.html', {'ldep':ldep, 'geneil':geneil})

def sciences(request):
        # this is your new view
    sdep = School_sciences_department.objects.all()
    geneis = School_general_information.objects.filter()
    return render(request, 'depscie.html', {'sdep':sdep, 'geneis':geneis})

def boarding(request):
        # this is your new view
    bdep = School_boarding_department.objects.all()
    geneib = School_general_information.objects.filter()
    return render(request, 'depboard.html', {'bdep':bdep, 'geneib':geneib})

def games(request):
        # this is your new view
    gdep = School_games_department.objects.all()
    geneig = School_general_information.objects.filter()
    return render(request, 'depgame.html', {'gdep':gdep, 'geneig':geneig})

def guidance(request):
        # this is your new view
    gudep = School_guiding_and_counseling_department.objects.all()
    geneigu = School_general_information.objects.filter()
    return render(request, 'depguide.html', {'gudep':gudep, 'geneigu':geneigu})

def humanities(request):
        # this is your new view
    hdep = School_humanities_department.objects.all()
    geneih = School_general_information.objects.filter()
    return render(request, 'dephuman.html', {'hdep':hdep, 'geneih':geneih})

def mathematics(request):
        # this is your new view
    mdep = School_math_department.objects.all()
    geneim = School_general_information.objects.filter()
    return render(request, 'depmath.html', {'mdep':mdep, 'geneim':geneim})

def technicals(request):
        # this is your new view
    tdep = School_technicals_department.objects.all()
    geneit = School_general_information.objects.filter()
    return render(request, 'deptech.html', {'tdep':tdep, 'geneit':geneit})

def bakery(request):
        # this is your new view
    bake = School_bakery.objects.all()
    genej = School_general_information.objects.filter()
    return render(request, 'facbake.html', {'bake':bake, 'genej':genej})
def library(request):
        # this is your new view
    libra = School_library.objects.all()
    genek = School_general_information.objects.filter()
    return render(request, 'faclib.html', {'libra':libra, 'genek':genek})
def laboratories(request):
        # this is your new view
    phylab = School_physics_lab.objects.all()
    chemlab = School_chemistry_lab.objects.filter()
    biolab = School_biology_lab.objects.filter()
    complab = School_computer_lab.objects.filter()
    genel = School_general_information.objects.filter()
    return render(request, 'faclab.html', {'phylab':phylab, 'chemlab':chemlab, 'biolab':biolab, 'complab':complab, 'genel':genel})
def dininghall(request):
        # this is your new view
    dine = School_dining_hall.objects.all()
    genem = School_general_information.objects.filter()
    return render(request, 'facdine.html', {'dine':dine, 'genem':genem})
def classrooms(request):
        # this is your new view
    one = School_form_one_classes.objects.all()
    two = School_form_two_classes.objects.filter()
    three = School_form_three_classes.objects.filter()
    four = School_form_four_classes.objects.filter()
    genen = School_general_information.objects.filter()
    return render(request, 'facclass.html', {'one':one, 'two':two, 'three':three, 'four':four, 'genen':genen})
def transport(request):
        # this is your new view
    trans = School_transport.objects.all()
    geneo = School_general_information.objects.filter()
    return render(request, 'factrans.html', {'trans':trans, 'geneo':geneo})
def schoolfence(request):
        # this is your new view
    fence = School_fence.objects.all()
    genep = School_general_information.objects.filter()
    return render(request, 'facfence.html', {'fence':fence, 'genep':genep})
def forest(request):
        # this is your new view
    forest = School_forest.objects.all()
    geneq = School_general_information.objects.filter()
    return render(request, 'facforest.html', {'forest':forest, 'geneq':geneq})
def carpark(request):
        # this is your new view
    park = School_car_park.objects.all()
    gener = School_general_information.objects.filter()
    return render(request, 'facpark.html', {'park':park, 'gener':gener})
def generator(request):
        # this is your new view
    gene = School_generator.objects.all()
    genes = School_general_information.objects.filter()
    return render(request, 'facgene.html', {'gene':gene, 'genes':genes})
def beautification(request):
        # this is your new view
    beu = School_beautification.objects.all()
    genet = School_general_information.objects.filter()
    return render(request, 'facbeauty.html', {'beu':beu, 'genet':genet})


def scienceengineering(request):
        # this is your new view
    scie = School_science_engineering_club.objects.all()
    genera = School_general_information.objects.filter()
    return render(request, 'scieeng.html', {'scie':scie, 'genera':genera})
def peace(request):
        # this is your new view
    peac = School_peace_club.objects.all()
    generaaa = School_general_information.objects.filter()
    return render(request, 'copeace.html', {'peac':peac, 'generaaa':generaaa})
def christianunion(request):
        # this is your new view
    scu = School_christian_union_club.objects.all()
    generb = School_general_information.objects.filter()
    return render(request, 'cocu.html', {'scu':scu, 'generb':generb})
def muslimstudents(request):
        # this is your new view
    sms = School_muslim_students_club.objects.all()
    generc = School_general_information.objects.filter()
    return render(request, 'coms.html', {'sms':sms, 'generc':generc})
def debate(request):
        # this is your new view
    debate = School_debate_club.objects.all()
    generd = School_general_information.objects.filter()
    return render(request, 'codebate.html', {'debate':debate, 'generd':generd})
def drama(request):
        # this is your new view
    dram = School_drama_club.objects.all()
    genere = School_general_information.objects.filter()
    return render(request, 'codrama.html', {'dram':dram, 'genere':genere})
def journalism(request):
        # this is your new view
    journ = School_journalism_club.objects.all()
    generf = School_general_information.objects.filter()
    return render(request, 'cojournalism.html', {'journ':journ, 'generf':generf})
def music(request):
        # this is your new view
    mus = School_music_club.objects.all()
    generg = School_general_information.objects.filter()
    return render(request, 'comusic.html', {'mus':mus, 'generg':generg})
def sports(request):
        # this is your new view
    spor = School_sports_club.objects.all()
    generh = School_general_information.objects.filter()
    return render(request, 'cosports.html', {'spor':spor, 'generh':generh})


def performance(request):
        # this is your new view
    perform = School_performance.objects.filter()
    generi = School_general_information.objects.filter()
    return render(request, 'acperformance.html', {'perform':perform, 'generi':generi})

def university(request):
        # this is your new view
    performu = School_performance.objects.filter()
    generiu = School_general_information.objects.filter()
    return render(request, 'university.html', {'performu':performu, 'generiu':generiu})


def history(request):
        # this is your new view
    history = School_history.objects.filter()
    generih = School_general_information.objects.filter()
    return render(request, 'history.html', {'history':history, 'generih':generih})

def philosophy(request):
        # this is your new view
    mission = School_mission.objects.filter()
    vision = School_vision.objects.filter()
    coresp = School_core_values.objects.filter()
    anthp = School_anthem.objects.filter()
    generiv = School_general_information.objects.filter()
    return render(request, 'philosophy.html', {'mission':mission, 'vision':vision, 'coresp':coresp, 'anthp':anthp, 'generiv':generiv})

def location(request):
        # this is your new view
    sitemap = School_site_map.objects.all()
    generiloc = School_general_information.objects.filter()
    return render(request, 'location.html', {'sitemap':sitemap, 'generiloc':generiloc})

def updates(request):
        # this is your new view
    update = School_updates.objects.all()
    genern = School_general_information.objects.filter()
    return render(request, 'stupdates.html', {'update':update, 'genern':genern})

def alumnae(request):
        # this is your new view
    alum = School_alumni.objects.all()
    genero = School_general_information.objects.filter()
    return render(request, 'alumnae.html', {'alum':alum, 'genero':genero})

def downloads(request):
        # this is your new view
    downer = School_downloads.objects.all()
    generoed = School_general_information.objects.filter()
    return render(request, 'downloads.html', {'downer':downer, 'generoed':generoed})

def anthem(request):
        # this is your new view
    anth = School_anthem.objects.filter()
    ant = School_general_information.objects.all()
    return render(request, 'anthem.html', {'anth':anth, 'ant':ant})

def corevalues(request):
        # this is your new view
    cores = School_core_values.objects.filter()
    core = School_general_information.objects.all()
    return render(request, 'corevalues.html', {'cores':cores, 'core':core})

def search(request):
         # this is your new view
 if 'q' in request.GET and request.GET['q']:
     q = request.GET['q']
     scorer = School_general_information.objects.filter()
     updated = School_updates.objects.filter(news_title__icontains=q)
     alumnews = School_alumnae.objects.filter(name__icontains=q)
     return render(request, 'search_results.html', {'alumnews':alumnews, 'scorer':scorer, 'updated':updated, 'query':q})

 else:
     return HttpResponse('Please submit a search term.')

