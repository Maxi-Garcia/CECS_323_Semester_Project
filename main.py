import logging

from sqla_util import *

import ClassHandling


def main():
    logging.basicConfig()
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)
    logging.getLogger("sqlalchemy.pool").setLevel(logging.DEBUG)

    # Drop For Development
    metadata.drop_all(bind=engine)

    # Create Tables for Entity Classes
    metadata.create_all(bind=engine)

    ClassHandling.test_building()


if __name__ == '__main__':
    main()
