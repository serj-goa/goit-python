from database.db import engine
from database.models import Base
from seed import make_seed


if __name__ == '__main__':
    # After running this file go to run_select.py

    Base.metadata.bind = engine
    make_seed()
