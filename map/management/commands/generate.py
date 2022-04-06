from django.core.management.base import BaseCommand
from django.conf import settings
from map.views import _render_index
import os


class Command(BaseCommand):
    help = 'Generate Static index.html for deploying'

    def handle(self, *args, **options):
        filepath = os.path.join(settings.BASE_DIR, ".deploy", "index.html")
        content = _render_index()
        with open(filepath, 'w') as f:
            f.write(content)
        self.stdout.write(f"Successfully generate index.html to {filepath}")
