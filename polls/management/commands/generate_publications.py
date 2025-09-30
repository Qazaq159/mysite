import random
from datetime import timedelta

from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from polls.models import Publication


class Command(BaseCommand):
    help = "Generate 10-15 Publication rows with unique titles and timestamps."

    def add_arguments(self, parser):
        parser.add_argument(
            "--count",
            type=int,
            default=12,
            help="Number of publications to create (must be between 10 and 15). Default: 12",
        )
        parser.add_argument(
            "--flush",
            action="store_true",
            help="Delete all existing Publication rows before generating.",
        )

    def handle(self, *args, **options):
        count: int = options["count"]
        flush: bool = options["flush"]

        if count < 10 or count > 15:
            raise CommandError("--count must be between 10 and 15")

        if flush:
            deleted, _ = Publication.objects.all().delete()
            self.stdout.write(self.style.WARNING(f"Deleted {deleted} existing Publication rows"))

        # Create publications with unique (title, create_date) pairs per model Meta.unique_together
        created = 0
        now = timezone.now()

        # To avoid duplicated titles when re-running without --flush, compute starting index
        existing_titles = set(Publication.objects.values_list("title", flat=True))

        # Generate a shuffled sequence to slightly vary seconds offsets
        second_offsets = list(range(0, max(60, count * 5)))
        random.shuffle(second_offsets)

        i = 1
        attempts = 0
        max_attempts = count * 5
        while created < count and attempts < max_attempts:
            attempts += 1
            title = f"Publication {i}"
            # ensure title uniqueness when combined with create_date anyway, but prefer unique title for clarity
            if title in existing_titles:
                i += 1
                continue

            create_date = now + timedelta(seconds=second_offsets[attempts % len(second_offsets)])
            Publication.objects.create(title=title, create_date=create_date)
            existing_titles.add(title)
            created += 1
            i += 1

        if created < count:
            raise CommandError(f"Only created {created} publications out of requested {count}.")

        self.stdout.write(self.style.SUCCESS(f"Successfully created {created} Publication rows."))
