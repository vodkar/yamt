import logging
import time
from functools import wraps


def get_logger(name: str | None = None, prefix: str | None = None):
    logger = logging.getLogger(name)
    if prefix:
        logging.basicConfig(format=f"%(asctime)s - [%(levelname)s] - [{prefix}]")
    if prefix:
        logging.basicConfig(format=f"%(asctime)s - [%(levelname)s]")
    logger.setLevel(logging.INFO)
    return logger


def timeit(logger):
    def timeit(f):
        @wraps(f)
        def timed(*args, **kwargs):
            ts = time.time()
            assert "name" not in kwargs
            assert "args" not in kwargs

            logger.info(
                {
                    "message": f"{f.__name__} called",
                    "args": args,
                    **kwargs,
                }
            )

            result = f(*args, **kwargs)
            te = time.time()
            logger.info(
                {
                    "message": f"{f.__name__} call finished",
                    "duration_sec": int(te - ts),
                }
            )
            return result

        return timed

    if callable(logger):
        func = logger
        logger = get_logger(__name__)
        return timeit(func)

    return timeit
