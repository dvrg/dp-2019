import datetime
print ('Waktu sekarang',datetime.datetime.now())

"""Variabel"""
date = datetime.datetime.now()
print(date)

"""Mengabungkan integer & string"""
number = 10
string = 'Sabil'
print(number, string)

"""Simple Type"""
x = 15
y = '15'
z = 15.1

sum1 = x+x
sum2 = y+y
sum3 = z+z

print(x,y,z)
print(type(x),type(y),type(z))

"""List"""
print(list(range(1,10)))
print(list(range(1,10,2)))

"""Menjumlahkan nilai didalam list"""
student_grades = [4,12.1,6,9]
mysum = sum(student_grades)
print(mysum)
"""Panjang nilai didalam list"""
length = len(student_grades)
print(length)
mean = mysum/length
print(mean)
"""Mencari jumlah nilai dalam list"""
student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grades.count(10.0)) #mencari nilai didalamnya
student = {'sabil':8.0, 'yanuar':7.0,'peby':9.0}
print(student.values()) # menampilkan nilainya
print(student.keys()) # menampilkan stringnya

list1 = ['kimia', 'fisika', 1993, 2017]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

list1 = ['fisika', 'kimia', 1993, 2017]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

#untuk menambahkan objek baru 
list1.append('2019')
print (list1)

#pelatihan
import datetime
my_var=datetime.date.now()
print(my_var)
