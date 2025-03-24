# in, not, not in, is, is not
# and, or

val = input("value dao: ")

if int(val) > 10:
    print(f"{val} boro")
    print("10 er cheye")
elif int(val)==10:
    print(f"{val} soman 10 er")
else: 
    print(f"{val} choto")
    print("10 er cheye")

alive = True
if alive is True:
    print("beche asi")
else:
    print("more gesi")

single = True
if single is not True:
    print("Amar biye hoye gese")
else:
    print("amar biye hoy nai")

if alive == True and single == True:
    print("tumi biye korar joggo")
else:
    print("tumi biye korar joggo na")
