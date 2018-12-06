import logging

LOG_FILENAME = 'logging_example.out'
logging.basicConfig(
    filename=LOG_FILENAME,
    level=logging.DEBUG,
)

logging.debug('This message should go to the log file')

with open(LOG_FILENAME, 'rt') as f:
    body = f.read()

print('FILE:')
print(body)

"""
After running the script, the log message is written to logging_example.out:

$ python3 logging_file_example.py

FILE:
DEBUG:root:This message should go to the log file
"""