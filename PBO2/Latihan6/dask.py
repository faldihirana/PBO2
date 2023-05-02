import dask.bag as db

def worker(num):
    """Fungsi untuk menjalankan tugas pada proses multiprocessing"""
    print('Worker', num)

if __name__ == '__main__':
    bag = db.from_sequence(range(5))

    bag.map(worker).compute()