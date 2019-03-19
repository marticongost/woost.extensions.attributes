"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from woost.models import ExtensionAssets
from .attribute import Attribute


def create_default_attributes():

    assets = ExtensionAssets("attributes")

    assets.require(
        Attribute,
        "default_attributes.publishable",
        title = assets.TRANSLATIONS,
        attribute_name = "data-woost-publishable",
        scope = "page",
        code = "value = publishable"
    )

    assets.require(
        Attribute,
        "default_attributes.type",
        title = assets.TRANSLATIONS,
        attribute_name = "data-woost-type",
        code = "value = publishable.__class__"
    )

    assets.require(
        Attribute,
        "default_attributes.path",
        title = assets.TRANSLATIONS,
        attribute_name = "data-woost-path",
        code = "value = reversed(list(app.ascend_navigation()))"
    )

    assets.require(
        Attribute,
        "default_attributes.locale",
        title = assets.TRANSLATIONS,
        attribute_name = "data-woost-locale",
        scope = "page",
        code = "from cocktail.translations import get_language\n"
               "value = get_language()"
    )

    assets.require(
        Attribute,
        "default_attributes.role",
        title = assets.TRANSLATIONS,
        attribute_name = "data-woost-roles",
        scope = "page",
        code = "value = list(app.user.iter_roles())"
    )

    assets.require(
        Attribute,
        "default_attributes.target",
        title = assets.TRANSLATIONS,
        attribute_name = "data-woost-target",
        scope = "ref",
        code = "value = publishable"
    )

def install():
    create_default_attributes()

