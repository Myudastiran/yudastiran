# input user

# data input dari user
data = input("masukan data : ")
print("data : ", data, "type = ", type(data))

# jika data adalah angka lakukan casting
angka = float (input("masukan angka : "))
print("data : ", angka, " type = ", type(angka))

# bagaimana jika data adalah boolean?
# jika data adalah boolean
boolean_input = input("masukan boolean (True/False) : ")

# konversi input ke boolean
if boolean_input == "True":
    boolean_data = True
elif boolean_input == "False":
    boolean_data = False

# jika input tidak valid
else:
    boolean_data = None

print("data : ", boolean_data, "type = ", type(boolean_data))

