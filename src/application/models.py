from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from ckeditor.fields import RichTextField


class Employee(models.Model):
    EMP_RANKS = (
        ('CEO', 'Chief Executive Officer'),
        ('DIR', 'Director'),
        ('MAN', 'Manager'),
        ('WOR', 'Worker'),
        ('OTH', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='emp/profiles/', null=True, blank=True)
    contact_no = models.CharField(
        max_length=18, null=True, blank=True, help_text='employee phone or landline number'
    )
    address = models.TextField(
        null=True, blank=True, help_text='Complete address within area/street, city state and country etc.'
    )
    nic = models.CharField(max_length=50, null=True, blank=True, help_text='National Identification Card or ID card')
    org_id = models.CharField(max_length=50, null=True, blank=True, help_text='Organizational Registration Number or ID')
    rank = models.CharField(
        max_length=3, null=True, blank=True, choices=EMP_RANKS,
        help_text='Employee Rank/Post/Destination within organization'
    )
    date_of_birth = models.DateField(null=True, blank=True, help_text='Date of Birth - Format must be YYYY-MM-DD')
    joined_on = models.DateField(null=True, blank=True, help_text='Date of Joining - Format must be YYYY-MM-DD')
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Employees'

    def __str__(self):
        return f"{self.pk} {self.user.first_name} {self.user.last_name}"


class Task(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(
        max_length=1000, null=False, blank=False, help_text='small description of this task 25-100 characters'
    )
    detailed_description = RichTextField(
        null=True, blank=True, help_text='Here you can define task details rules and all other possible requirements'
    )
    start_time = models.DateTimeField(
        null=False, blank=False, help_text='Start date and time of the task format must be YYYY-MM-DD'
    )
    end_time = models.DateTimeField(
        null=False, blank=False, help_text='End date and time of the task format must be YYYY-MM-DD'
    )
    is_active = models.BooleanField(
        null=False, blank=False, default=True,
        help_text='If you check this it means the task is active and if you disable it it will be removed temporary'
    )
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now_add=True, help_text='End date and time of the task')

    class Meta:
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return f"{self.pk} {self.name} start {self.start_time} to end {self.end_time}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Task, self).save(*args, **kwargs)


@receiver(post_save, sender=User)
def save_employee_on_user(sender, instance, created, **kwargs):
    if created:
        if instance.id is None:
            emp = Employee(user=User.objects.get(pk=instance.id))
            emp.save()
        else:
            emp = Employee(user=User.objects.get(pk=instance.id))
            emp.save()
