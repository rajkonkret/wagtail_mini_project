from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks

class HomePage(Page):
    body = StreamField([
        ("heading", blocks.CharBlock()),
        ("paragraph", blocks.RichTextBlock()),
        ("quote", blocks.TextBlock()),
    ], use_json_field=True, blank=True)

    content_panels = Page.content_panels + ["body"]
