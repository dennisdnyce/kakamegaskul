from PIL import Image
from django.db import models
from image_cropping import ImageRatioField
from django.utils import timezone
from django.core.validators import URLValidator

# Create your models here.
class School_photo_gallery(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, default='edit this description')
    photo = models.ImageField(upload_to='uploads/')
    cropping = ImageRatioField('photo', '1024x768')
    created_date = models.DateTimeField(
              default=timezone.now)
    published_date = models.DateTimeField(
              blank=True, null=True)

    class Meta:
        verbose_name = 'school photo gallery'
        verbose_name_plural = 'school photo galleries'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.title

class School_events (models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    event_title = models.CharField(max_length=200)
    event_description = models.TextField()
    event_date = models.DateTimeField(
           blank=True, null=True)

    class Meta:
        verbose_name = 'school event'
        verbose_name_plural = 'school events'

    def publish(self):
       self.event_date = timezone.now()
       self.save()

    def __str__(self):
        return self.event_title

class School_bog_chairperson(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    class Meta:
        verbose_name = 'school BOG Chairperson'
        verbose_name_plural = 'school BOG Chairperson'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_pta_chairperson(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    class Meta:
        verbose_name = 'school PTA Chairperson'
        verbose_name_plural = 'school PTA Chairperson'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_principal(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
              default=timezone.now)
    published_date = models.DateTimeField(
              blank=True, null=True)

    class Meta:
        verbose_name = 'school Principal'
        verbose_name_plural = 'school Principal'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_dp_academics(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
              default=timezone.now)
    published_date = models.DateTimeField(
              blank=True, null=True)

    class Meta:
        verbose_name = 'school DP Academics'
        verbose_name_plural = 'school DP Academics'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_dp_admin(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school DP Admin'
        verbose_name_plural = 'school DP Admin'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_teachers(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Teachers'
        verbose_name_plural = 'school Teachers'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_student_council(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Students Council'
        verbose_name_plural = 'school Students Council'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_languages_hod(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Languages HOD'
        verbose_name_plural = 'school Languages HOD'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_math_hod(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Math HOD'
        verbose_name_plural = 'school Math HOD'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_sciences_hod(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Sciences HOD'
        verbose_name_plural = 'school Sciences HOD'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_humanities_hod(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Humanities HOD'
        verbose_name_plural = 'school Humanities HOD'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_technicals_hod(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200, null=True)
    few_words = models.TextField(null=True)
    photo = models.ImageField(upload_to='uploads/', null=True)
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Technical Studies HOD'
        verbose_name_plural = 'school Technical Studies HOD'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_boarding_hod(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Boarding HOD'
        verbose_name_plural = 'school Boarding HOD'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_games_hod(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Games HOD'
        verbose_name_plural = 'school Games HOD'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_guiding_and_counseling_hod(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Guiding and Counciling HOD'
        verbose_name_plural = 'school Guiding and Counciling HOD'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_languages_department(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Languages Department'
        verbose_name_plural = 'school Languages Department'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_math_department(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Math Department'
        verbose_name_plural = 'school Math Department'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_sciences_department(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Sciences Department'
        verbose_name_plural = 'school Sciences Department'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_humanities_department(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Humanities Department'
        verbose_name_plural = 'school Humanities Department'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_technicals_department(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200, null=True)
    few_words = models.TextField(null=True)
    photo = models.ImageField(upload_to='uploads/', null=True)
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Technicals Department'
        verbose_name_plural = 'school Technicals Department'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_boarding_department(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Boarding Department'
        verbose_name_plural = 'school Boarding Department'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_games_department(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Games Department'
        verbose_name_plural = 'school Games Department'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_guiding_and_counseling_department(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    name = models.CharField(max_length=200)
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Guiding and Counciling Department'
        verbose_name_plural = 'school Guiding and Counciling Department'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.name

class School_drama_club(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Drama Club'
        verbose_name_plural = 'school Drama Club'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_music_club(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Music Club'
        verbose_name_plural = 'school Music Club'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_sports_club(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Sports Club'
        verbose_name_plural = 'school Sports Club'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_christian_union_club(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Christian Union Club'
        verbose_name_plural = 'school Christian Union Club'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_muslim_students_club(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Muslim Students Club'
        verbose_name_plural = 'school Muslim Students Club'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_journalism_club(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Journalism Club'
        verbose_name_plural = 'school Journalism Club'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_debate_club(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Debate Club'
        verbose_name_plural = 'school Debate Club'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_science_engineering_club(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Science Engineering Club'
        verbose_name_plural = 'school Science Engineering Club'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_peace_club(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Peace Club'
        verbose_name_plural = 'school Peace Club'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_history(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school History'
        verbose_name_plural = 'school History'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_previous_heads(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    school_head = models.CharField(max_length=200)
    start_year = models.CharField(max_length=200)
    end_year = models.CharField(max_length=200)
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Previous Heads'
        verbose_name_plural = 'school Previous Heads'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.school_head        

class School_mission(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    class Meta:
        verbose_name = 'school Mission'
        verbose_name_plural = 'school Mission'

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
         return self.text

class School_vision(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    class Meta:
        verbose_name = 'school Vision'
        verbose_name_plural = 'school Vision'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_site_map(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Site Map'
        verbose_name_plural = 'school Site Map'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_library(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Library'
        verbose_name_plural = 'school Library'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_dining_hall(models.Model):
       author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
       text = models.TextField()
       photo = models.ImageField(upload_to='uploads/')
       created_date = models.DateTimeField(
             default=timezone.now)
       published_date = models.DateTimeField(
              blank=True, null=True)

       class Meta:
           verbose_name = 'school Dining Hall'
           verbose_name_plural = 'school Dining Hall'

       def publish(self):
          self.published_date = timezone.now()
          self.save()

       def __str__(self):
           return self.text

class School_form_one_classes(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    class Meta:
        verbose_name = 'school Form One Classes'
        verbose_name_plural = 'school Form One Classes'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_form_two_classes(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    class Meta:
        verbose_name = 'school Form Two Classes'
        verbose_name_plural = 'school Form Two Classes'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_form_three_classes(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Form Three Classes'
        verbose_name_plural = 'school Form Three Classes'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_form_four_classes(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    class Meta:
        verbose_name = 'school Form Four Classes'
        verbose_name_plural = 'school Form Four Classes'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_transport(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Transport'
        verbose_name_plural = 'school Transport'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_physics_lab(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Physics Lab'
        verbose_name_plural = 'school Physics Lab'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_chemistry_lab(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Chemistry Lab'
        verbose_name_plural = 'school Chemistry Lab'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_biology_lab(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Biology Lab'
        verbose_name_plural = 'school Biology Lab'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_computer_lab(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Computer Lab'
        verbose_name_plural = 'school Computer Lab'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_fence(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Fence'
        verbose_name_plural = 'school Fence'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_bakery(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Bakery'
        verbose_name_plural = 'school Bakery'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_forest(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Forest'
        verbose_name_plural = 'school Forest'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_car_park(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
           default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    class Meta:
        verbose_name = 'school Car Park'
        verbose_name_plural = 'school Car Park'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_generator(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Generator'
        verbose_name_plural = 'school Generator'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_beautification(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    text = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school Beautification'
        verbose_name_plural = 'school Beautification'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.text

class School_general_information(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    school_logo = models.ImageField(upload_to='uploads/')
    school_twitterlink = models.TextField(validators=[URLValidator()])
    school_facebooklink = models.TextField(validators=[URLValidator()])
    mail_icon = models.ImageField(upload_to='uploads/', null=True)
    current_year = models.IntegerField(default=2007)
    school_address = models.TextField()
    school_website = models.TextField(null=True)
    school_emailaddress = models.CharField(max_length=200)
    address_icon = models.ImageField(upload_to='uploads/', null=True)
    school_phone_number = models.CharField(max_length=200)
    other_phone_number = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(
          default=timezone.now)
    published_date = models.DateTimeField(
          blank=True, null=True)

    class Meta:
        verbose_name = 'school General Information'
        verbose_name_plural = 'school General Information'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.school_address

class School_anthem (models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    stanza = models.TextField()
    created_date = models.DateTimeField(
           default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    class Meta:
        verbose_name = 'school Anthem'
        verbose_name_plural = 'school Anthem'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.stanza

class School_warriors_way (models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    stanzas = models.TextField()
    created_date = models.DateTimeField(
           default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    class Meta:
        verbose_name = 'school Warriors Way'
        verbose_name_plural = 'school Warriors Way'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.stanzas        

class School_core_values (models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    core_value = models.CharField(max_length=300)
    created_date = models.DateTimeField(
           default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    class Meta:
        verbose_name = 'school Core Value'
        verbose_name_plural = 'school Core Values'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.core_value

class School_updates (models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    news_title = models.CharField(max_length=200)
    news_description = models.TextField()
    created_date = models.DateTimeField(
           default=timezone.now)
    published_date = models.DateTimeField(
           blank=True, null=True)

    class Meta:
        verbose_name = 'school Update'
        verbose_name_plural = 'school Updates'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.news_title

class School_alumni(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    alumni_year = models.CharField(max_length=5, default='2015')
    few_words = models.TextField()
    photo = models.ImageField(upload_to='uploads/')
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    class Meta:
        verbose_name = 'school Alumnus'
        verbose_name_plural = 'school Alumni'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.few_words

class School_downloads(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    document_name = models.CharField(max_length=200)
    document_file = models.FileField(upload_to='uploads/')
    created_date = models.DateTimeField(
         default=timezone.now)
    published_date = models.DateTimeField(
         blank=True, null=True)

    class Meta:
        verbose_name = 'school Download'
        verbose_name_plural = 'school Downloads'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
        return self.document_name

class School_performance(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING,)
    kcse_year = models.CharField(max_length=5, default='2007')
    grades_A_plain = models.IntegerField(default=00)
    grades_A_minus = models.IntegerField(default=00)
    grades_B_plus = models.IntegerField(default=00)
    grades_B_plain = models.IntegerField(default=00)
    grades_B_minus = models.IntegerField(default=00)
    grades_C_plus = models.IntegerField(default=00)
    grades_C_plain = models.IntegerField(default=00)
    grades_C_minus = models.IntegerField(default=00)
    grades_D_plus = models.IntegerField(default=00)
    grades_D_plain = models.IntegerField(default=00)
    grades_D_minus = models.IntegerField(default=00)
    grades_E = models.IntegerField(default=00)
    grades_F = models.IntegerField(default=00)
    school_mean_score = models.FloatField(default=00)
    university_qualified = models.IntegerField(default=00)
    total_students = models.IntegerField(default=00)
    created_date = models.DateTimeField(
             default=timezone.now)
    published_date = models.DateTimeField(
             blank=True, null=True)

    class Meta:
        verbose_name = 'school Performance'
        verbose_name_plural = 'school Performance'

    def publish(self):
       self.published_date = timezone.now()
       self.save()

    def __str__(self):
          return self.kcse_year
