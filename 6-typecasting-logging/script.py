import logging

logging.basicConfig(level=logging.ERROR,format="%(levelname)s %(filename)s | %(funcName)s()  %(lineno)d | %(message)s")

# debug, info, warn, error fatal , critical

value = "Hello World!"

try:
    num = int(value)
except Exception as e: # Exception is any kind of exception it can handle
    logging.error(f"Conversion failed {e}")