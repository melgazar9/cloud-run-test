import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s -- %(levelname)s -- %(message)s')

def log():
    logging.info('*** INFO ***')
    logging.warning('*** WARNING ***')
    logging.critical('*** CRITICAL ***')
    return

if __name__ == '__main__':
    log()
