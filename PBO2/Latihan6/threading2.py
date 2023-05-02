import threading

def worker(num):
    """Fungsi untuk menjalankan tugas pada thread baru"""
    print('Worker', num)

if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)
for t in threads:
    t.join()