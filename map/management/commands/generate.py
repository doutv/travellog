from django.core.management.base import BaseCommand
from django.conf import settings
from map.views import _render_index
import os
from PIL import Image, ImageOps
import glob
from distutils.dir_util import copy_tree


def copy_and_compress_photos(max_width=1024, quality=70):
    # copy photos/ to .deploy/photos
    from_dir = settings.MEDIA_ROOT
    save_dir = os.path.join(settings.BASE_DIR, ".deploy", "photos")
    copy_tree(from_dir, save_dir)
    photo_exts = ("**/*.png", "**/*.JPG", "**/*.jpeg", "**/*.jpg")
    photos = []
    for photo_exts in photo_exts:
        photos.extend(glob.glob(photo_exts, root_dir=save_dir))
    for photo in photos:
        photo_path = os.path.join(save_dir, photo)
        max_photo_size = 100*1024  # 100KB
        if os.stat(photo_path).st_size < max_photo_size:
            continue
        with open(photo_path, "rb") as f:
            img = Image.open(f)
            img = ImageOps.exif_transpose(img)
            width, height = img.size
            new_width = max_width
            new_height = round(height * max_width / width)
            img = img.resize((new_width, new_height))
            img.save(photo_path, optimize=True, quality=quality)


class Command(BaseCommand):
    help = 'Generate Static index.html for deploying'

    def handle(self, *args, **options):
        copy_and_compress_photos()
        static_from_dir = os.path.join(
            settings.BASE_DIR, "map", "static")
        static_save_dir = os.path.join(
            settings.BASE_DIR, ".deploy", "static")
        copy_tree(static_from_dir, static_save_dir)
        filepath = os.path.join(settings.BASE_DIR, ".deploy", "index.html")
        content = _render_index()
        with open(filepath, 'w') as f:
            f.write(content)
        self.stdout.write(f"Successfully generate index.html to {filepath}")
