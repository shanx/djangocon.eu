from optparse import make_option


from django.core.management.base import BaseCommand, CommandError
from django.template.loader import render_to_string


from waitlist.models import WaitList

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--batch',
            action='store',
            dest='batch',
            default=None,
            help='Batch to generate invitation mails for'),
        )

    def handle(self, *args, **options):
        batch = options.get('batch')

        if batch is not None:
            waitlist_entries = WaitList.objects.filter(
                batch=int(batch),
                done=False
            )

            for waitlist in waitlist_entries:
                rendered = render_to_string(
                    'waitlist/invitation.txt',
                    { 'waitlist': waitlist }
                )
                print rendered
        else:
            raise CommandError('No batch given')