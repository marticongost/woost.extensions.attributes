#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.events import when
from woost.admin.sections import CRUD
from woost.admin.sections.contentsection import ContentSection
from woost.extensions.attributes.attribute import Attribute

@when(ContentSection.declared)
def fill(e):
    e.source.append(CRUD("attributes", model = Attribute))

