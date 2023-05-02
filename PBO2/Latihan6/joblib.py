from joblib import Parallel, delayed

def worker(num):
    """Fungsi untuk menjalankan tugas pada proses multiprocessing"""
    print('Worker', num)
    
if __name__ == '__main__':
