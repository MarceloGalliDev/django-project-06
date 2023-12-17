#!/usr/bin/env python

# pylint: disable=all

"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # TODO: change this in production
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'authors_api.settings.local')
    try:
        from django.core.management import execute_from_command_line  # type: ignore

        # TODO: change this in production
        import debugpy  # type: ignore
        debugpy.listen(("0.0.0.0", 5678))
        # debugpy.wait_for_client()
        print('Attached!')

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
