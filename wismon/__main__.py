"""
Allow the package to be executed with python -m
"""
import sys

if __name__ == '__main__':
    from . import main

    sys.exit(main())
