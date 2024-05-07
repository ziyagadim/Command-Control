# import logging
# logger = logging.getLogger()
# logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG,
#                     format='[%(levelname)s]%(asctime)s:%(message)s', datefmt='%d-%m-%Y %I:%M:%S %p')

# logger.info('So should this')

import time
day = time.gmtime()
# cur_date = day.tm_mday + 
print(f'[INFO]{day.tm_mday}-{day.tm_mon}-{day.tm_year}')
date = time.asctime().split()
print(f'[INFO]{date[2]}-{date[1]}-{date[4]} {date[3]}:')

print(time.asctime())

