from django.db import models
from django.contrib.auth.models import AbstractUser


class Skill(models.Model):
    skill_name = models.CharField(64)

    def __str__(self):
        return f'{self.skill_name}'


class UserProfile(AbstractUser):
    password = models.CharField()
    ROLE_CHOICES = (
        ('client', 'client'),
        ('freelancer', 'freelancer'),
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=23)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatar_images')
    skills = models.ManyToManyField(Skill)
    social_links = models.URLField()

    def __str__(self):
        return f'{self.username}'


class Category(models.Model):
    category_name = models.CharField(max_length=32)

    def __str__(self):
        return f'{self.category_name}'


class Project(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField()
    budget = models.PositiveSmallIntegerField()
    deadline = models.DateField()
    STATUS_CHOICES = (
        ('open', 'open'),
        ('in_progress', 'in_progress'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled'),
    )
    status = models.CharField(choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_projects')
    skills_required = models.ManyToManyField(Skill)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


class Offer(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    proposed_budget = models.PositiveSmallIntegerField()
    proposed_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project} freelancer is {self.freelancer}'


class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviewer_user')
    target = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='target_user')
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.project}'
        
