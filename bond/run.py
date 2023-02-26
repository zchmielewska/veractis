import sys

from cashflower import start
from bond.settings import settings


if __name__ == "__main__":
    start("bond", settings, sys.argv)
