#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.translations import translations
from woost.models import add_setting, LocaleMember

translations.load_bundle("woost.extensions.attributes.settings")

add_setting(
    LocaleMember(
        "x_attributes_language"
    )
)

