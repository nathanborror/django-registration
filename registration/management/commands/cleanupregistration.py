"""
A management command which deletes expired accounts (e.g.,
accounts which signed up but never activated) from the database.

Calls ``backend.delete_expired_users()``, which contains the actual
logic for determining which accounts are deleted.

You can supply a custom backend using the ``--backend`` flag, which
takes a dotted import path to the appropriate class.

"""

from optparse import make_option

from django.core.management.base import NoArgsCommand

from registration.backends import get_backend


class Command(NoArgsCommand):
    help = "Delete expired user registrations from the database"
    option_list = NoArgsCommand.option_list + (
            make_option('--backend',
                action='store',
                dest='backend',
                default='registration.backends.default.DefaultBackend',
                help='Specifies the backend to use when removing expired accounts'),
            )

    def handle(self, **options):
        backend = get_backend(options['backend'])
        backend.delete_expired_users()
