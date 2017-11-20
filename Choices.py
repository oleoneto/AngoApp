# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import date


STATUS_CHOICES = (
    ('d', 'Draft'),
    ('p', 'Published'),
)

IDIOMAS = (
    ('en', 'English'),
    ('es', 'Español'),
    ('fr', 'Français'),
    ('it', 'Italiano'),
    ('pt', 'Português'),
    ('ro', 'Roumain'),
)


TOPICS = (
    ('code', 'Coding'),
    ('news', 'Notícias'),
    ('exp', 'Experimentos'),
    ('aulas', 'Aulas'),

    # Scripting...
    ('rb', 'Ruby'),
    ('py', 'Python'),
    ('sh', 'ShellScript'),
    ('md', 'Markdown'),

    # C-based...
    ('c', 'C'),
    ('cpp', 'C++'),
    ('csp', 'C#'),
    ('java', 'Java'),
    ('ru', 'Rust'),

    # Mobile...
    ('swift', 'Swift'),
    ('m', 'Objective-C'),

    # Web development
    ('html', 'HTML'),
    ('css', 'CSS'),
    ('js', 'JavaScript'),
    ('web','HTML, CSS, JavaScript'),

    # Server-side
    ('node', 'NodeJS'),
    ('dj', 'Django'),
    ('rails', 'Ruby on Rails'),

    # Others
    ('as', 'Apple Script'),
    ('r', 'R')
)


SOLICIT_CHOICES = (
        ('a', 'Produção de Áudio'),
        ('i', 'Ilustração'),
        ('v', 'Produção e/ou Edição de Vídeo'),
        ('f', 'Fotografia'),
        ('w', 'Criação de Website'),
        ('d', 'Registrar Domínio'),
        ('l', 'Logotipo'),
    )

TOPIC_CHOICES  = (
       ('N', 'News'),
       ('T', 'Technology'),
       ('A', 'Audio'),
       ('V', 'Video'),
       ('S', 'Science'),
       ('P', 'Programming'),
       ('G', 'General'),
       ('C', 'Culture'),
       ('W', 'Web'),
    )