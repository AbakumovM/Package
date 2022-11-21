from aplication.salary import calculate_salary 
from aplication.db.people import get_employees
from datetime import datetime
import emoji
from tqdm import tqdm
from time import sleep 


def get_tqdm():
    for i in tqdm(range(100)):
        sleep(0.01)


if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.now(),emoji.emojize(':calendar::watch:'))
    get_tqdm()
