# This Python file uses the following encoding: utf-8

from __future__ import unicode_literals
from django.http import HttpRequest, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login


# REST Api Imports...
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAdminUser

from Serializers import *



"""

Written by Leo Neto
Updated on November 19, 2017

"""