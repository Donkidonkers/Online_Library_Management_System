from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g Science Fiction)')

    def _str_(self):
        return self.name

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Book(models.Model):
    title = models.CharField(max_length=200)

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character ISBN number')

    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def _str_(self):
        return self.title

import uuid

class BookInstance(models.Model):
    """Model representing a specific copy of a book"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book Availability',
    )
    class Meta:
        ordering = ['due_back']

    def _str_(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.book.title})'
    

class Author(models.Model):
    """Model representing an author. """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null = True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)
    class Meta:
        ordering = ['last_name', 'first_name']

    def _str_(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'

class Language(models.Model):
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    
