"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail import schema
from woost.models import Item, Publishable


class Attribute(Item):

    members_order = [
        "title",
        "enabled",
        "content_types",
        "scope",
        "attribute_name",
        "code"
    ]

    title = schema.String(
        required = True,
        translated = True,
        unique = True,
        indexed = True,
        descriptive = True
    )

    enabled = schema.Boolean(
        required = True,
        default = True,
        indexed = True
    )

    content_types = schema.Collection(
        items = schema.Reference(class_family = Item),
        default = [Publishable],
        ui_form_control = "cocktail.ui.SplitSelector",
        min = 1
    )

    scope = schema.String(
        required = True,
        enumeration = ["any", "page", "ref"],
        default = "any",
        ui_form_control = "cocktail.ui.RadioSelector",
        indexed = True
    )

    attribute_name = schema.String(
        required = True,
        unique = True,
        indexed = True
    )

    code = schema.CodeBlock(
        language = "python",
        required = True
    )

