#!/usr/bin/python
#-*- coding: utf-8 -*-

from ElementoMapa import ElementoMapa
from Decorator import Decorator

class Bomba(ElementoMapa, Decorator):
    def __init__(self):
        self.activa = None

