areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print(areas_pis[1]) 
print(areas_pis[13])
print(areas_pis[7])
print(areas_pis[0] + str(areas_pis[1]) + areas_pis[2]) 
print(areas_pis[2] + str(areas_pis[3]) + areas_pis[4] + str(areas_pis[5]) + areas_pis[6] + 
      str(areas_pis[7]) + areas_pis[8] + str(areas_pis[9]) + areas_pis[10] + str(areas_pis[11])
        + areas_pis[12] + str(areas_pis[13]))
print(areas_pis[5] + areas_pis[13])

areas_pis[9] = 10
print(areas_pis)

areas_pis.extend(["Pati_interior", 2.78])
print(areas_pis)

print(areas_pis[1]+ areas_pis[3] + areas_pis[5] + areas_pis[7] + areas_pis[9] + areas_pis[11] + areas_pis[13] + areas_pis[15])
      