from django.db import models
from django.urls import reverse


def attachment_path(instance, filename):
    return "driver/" + str(instance.driver.id) + "/attachments/" + filename


def poster_path(instance, filename):
    return "driver/" + str(instance.id) + "/poster/" + filename


"""def c_poster_path(instance, filename):
    return "circuit/" + str(instance.id) + "/poster/" + filename"""
# Create your models here.


class Constructor(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Constructor name",
                            help_text="Enter a constructor team (Mercedes, McLaren...)")
    constructor_wins = models.IntegerField(default=0, blank=True, null=True, verbose_name="Number of victories")
    wcc = models.IntegerField(default=0, blank=True, null=True, verbose_name="Number of championships")
    history = models.TextField(blank=True, null=True, verbose_name="History")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def driver_count(self, obj):
        return obj.driver_set.count()


class Driver(models.Model):
    name = models.CharField(max_length= 50, unique=True, verbose_name="Driver name",
                            help_text="Enter the name of the F1 driver (Lewis Hamilton, Max Verstappen...)")
    poster = models.ImageField(upload_to=poster_path, blank=True, null=True, verbose_name="Poster")
    nationality = models.CharField(max_length=30, verbose_name="Nationality")
    birth = models.DateField(help_text="Please use the following format: <em>YYYY-MM-DD</em>.",
                             verbose_name="Birth")
    teams = models.ForeignKey(Constructor,
                              help_text="Select the constructor team the driver has been racing for",
                              on_delete=models.CASCADE, verbose_name="Team")
    driver_wins = models.IntegerField(default=0, blank=True, null=True, verbose_name="Number of victories")
    wdc = models.IntegerField(default=0, blank=True, null=True, verbose_name="Number of championships")
    biography = models.TextField(blank=True, null=True, verbose_name="Biography")

    class Meta:
        ordering = ["-driver_wins", "name"]

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("driver-detail", args=[str(self.id)])

    def birth_year(self):
        return self.birth


"""class Circuit(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="Track id",
                             help_text="Please enter the the track id respectively"
                                       " to its order in the 2021 calendar (Bahrain - id 1)")
    name = models.CharField(max_length=70, unique=True, verbose_name="Track name",
                            help_text="Enter a name of an F1 track (Suzuka, Catalunya...)")
    country = models.CharField(max_length=30, verbose_name="Country")
    c_poster = models.ImageField(upload_to=c_poster_path, blank=True, null=True, verbose_name="Poster")
    first_race = models.DateField(verbose_name="First race at the track",
                                      help_text="Please use the following format: <em>YYYY-MM-DD</em>.")
    laps = models.IntegerField(default=55, verbose_name="Number of laps")
    winner = models.ForeignKey(Driver, blank=True, null=True, verbose_name="2021 winner",
                               help_text="Enter the winner of this circuit from this year (2021)",
                               on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.country}"
        """


class Attachment(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name="File")
    '''TYPE_OF_ATTACHMENT = (
        ('audio', 'Audio'),
        ('image', 'Image'),
        ('text', 'Text'),
        ('video', 'Video'),
        ('other', 'Other')
    )'''

    '''type = models.CharField(max_length=5, choices=TYPE_OF_ATTACHMENT, blank=True,
                            default='image', help_text='Select allowed attachment type', verbose_name="Attachment type")'''
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    """circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)"""

    class Meta:
        #ordering = ["-last_update"]
        order_with_respect_to = 'driver'

    def __str__(self):
        return f"{self.title}"

    @property
    def filesize(self):
        x = self.file.size
        y = 512000
        if x < y * 1000:
            value = round(x / 1024, 2)
            ext = ' KB'
        elif x < y * 1000 ** 2:
            value = round(x / 1024 ** 2, 2)
            ext = ' MB'
        else:
            value = round(x / 1024 ** 3, 2)
            ext = ' GB'
        return str(value) + ext


