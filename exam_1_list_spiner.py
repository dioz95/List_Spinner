list_awal = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

def counterClockwise(A):
    """
    Fungsi untuk melakukan spinning pada sebuah nested list dapat dilakukan dengan 
    metode indexing secara sederhana. Dengan menemukan pola yang cocok untuk output
    yang dikehendaki, proses pembentukan list baru dapat dilakukan dengan foor loop 
    dan fungsi .append() untuk meng-update list awal. Namun saya belum dapat menemukan
    algoritma yang cukup general untuk memproses inputan dengan dimensi yang beragam.
    Fungsi ini hanya berlaku untuk list yang berdimensi 3x3. Namun paling tidak, output
    sesuai yang diminta oleh soal telah berhasil didapatkan.
    """
    d0 = []
    d1 = []
    d2 = []

    for i in range(3):
        i0 = A[i][2]
        i1 = A[i][1]
        i2 = A[i][0]

        d0.append(i0)
        d1.append(i1)
        d2.append(i2)

    d0 = [d0]
    d0.append(d1)
    d0.append(d2)

    return d0

print(counterClockwise(list_awal))