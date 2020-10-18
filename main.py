from Processor import Processor
from Memory import Memory
import threading
import time


if __name__ == "__main__":

    processor = []
    for i in range(4):
        processor.append(Processor(i,1))
    m = Memory(2)

    processor[0].writeCache('1001','ffff')
    print(processor[0].readCache('1001'))