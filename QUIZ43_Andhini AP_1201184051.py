listGPA = [2.1, 2.5, 4, 3]

def bonus(GPA):
    tambahan = 500000
    bonus = GPA*500000
    return bonus

for GPA in listGPA:
    if GPA > 2.5:
        print("Selamat! Anda mendapatkan bonus sebesar Rp", bonus(GPA))
    else:
        print("Maaf, Anda belum beruntung")