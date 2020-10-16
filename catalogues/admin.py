from django.contrib import admin
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
from .models import School_previous_heads
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
from .models import School_warriors_way
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
from image_cropping import ImageCroppingMixin

admin.site.site_header = "Kakamega School Administration";
# Register your models here.
class School_photo_galleryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(School_photo_gallery, School_photo_galleryAdmin)
admin.site.register(School_bog_chairperson)
admin.site.register(School_pta_chairperson)
admin.site.register(School_principal)
admin.site.register(School_dp_academics)
admin.site.register(School_dp_admin)
admin.site.register(School_languages_hod)
admin.site.register(School_math_hod)
admin.site.register(School_sciences_hod)
admin.site.register(School_humanities_hod)
admin.site.register(School_boarding_hod)
admin.site.register(School_games_hod)
admin.site.register(School_guiding_and_counseling_hod)
admin.site.register(School_technicals_hod)
admin.site.register(School_drama_club)
admin.site.register(School_music_club)
admin.site.register(School_sports_club)
admin.site.register(School_christian_union_club)
admin.site.register(School_muslim_students_club)
admin.site.register(School_journalism_club)
admin.site.register(School_debate_club)
admin.site.register(School_science_engineering_club)
admin.site.register(School_history)
admin.site.register(School_previous_heads)
admin.site.register(School_mission)
admin.site.register(School_vision)
admin.site.register(School_site_map)
admin.site.register(School_library)
admin.site.register(School_dining_hall)
admin.site.register(School_form_one_classes)
admin.site.register(School_form_two_classes)
admin.site.register(School_form_three_classes)
admin.site.register(School_form_four_classes)
admin.site.register(School_transport)
admin.site.register(School_physics_lab)
admin.site.register(School_chemistry_lab)
admin.site.register(School_biology_lab)
admin.site.register(School_computer_lab)
admin.site.register(School_fence)
admin.site.register(School_bakery)
admin.site.register(School_forest)
admin.site.register(School_car_park)
admin.site.register(School_generator)
admin.site.register(School_beautification)
admin.site.register(School_general_information)
admin.site.register(School_alumni)
admin.site.register(School_downloads)
admin.site.register(School_updates)
admin.site.register(School_core_values)
admin.site.register(School_warriors_way)
admin.site.register(School_performance)
admin.site.register(School_peace_club)
admin.site.register(School_languages_department)
admin.site.register(School_math_department)
admin.site.register(School_sciences_department)
admin.site.register(School_humanities_department)
admin.site.register(School_boarding_department)
admin.site.register(School_games_department)
admin.site.register(School_guiding_and_counseling_department)
admin.site.register(School_technicals_department)
admin.site.register(School_teachers)
admin.site.register(School_student_council)
admin.site.register(School_events)
