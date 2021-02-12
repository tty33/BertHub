PATH = 'data/'
SEED = 2020
EPOCHS = 5
BATCH_SIZE = 2
MAX_LENGTH = 128
LEARNING_RATE = 1e-5
NAME = 'hfl/chinese-bert-wwm'

# pytorch dataloader num_wokers
import sys
NUM_WORKERS = 0 if sys.platform == 'win32' else 4