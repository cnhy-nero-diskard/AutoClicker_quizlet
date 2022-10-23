import sys
import logging
FORMAT = '%(levelname) - %(asctime)s -AutoClicker %(message)s'
FORMAT = ("%(levelname)  %(message)s")
FORMAT = ("%(asctime)s  %(name)s  %(levelname)s  %(message)s")

logger = logging.getLogger('otog')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)

console = logging.StreamHandler(sys.stdout)
console.setFormatter(formatter)
logger.addHandler(console)

file_handler = logging.FileHandler('testtube.log', mode='a')
file_handler.setFormatter(formatter)


logger.addHandler(file_handler)
#logging.basicConfig(filename='test.log',level=logging.WARNING,format = FORMAT)



try:
    for i in range(10,0,-1):
        logger.info("{} reps".format(i))
        89/i
    89/0
except:
    logger.warning("hola")
    print("Ching")