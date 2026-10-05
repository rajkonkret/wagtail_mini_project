from django.db import models

from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page


class HomePage(Page):

    hero_title = models.CharField(
        max_length=100,
        blank=True,
    )

    body = StreamField(
        [
            ("heading", blocks.CharBlock()),
            ("paragraph", blocks.RichTextBlock()),
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("hero_title"),
        FieldPanel("body"),
    ]