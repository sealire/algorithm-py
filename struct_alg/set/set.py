Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
Months = {"Jan", "Feb", "Mar"}
Dates = {21, 22, 17}
print(Days)
print(Months)
print(Dates)

Days.add("Sun")
print(Days)

for d in Days:
    print(d)

Days.discard("Sun")
print(Days)

DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
AllDays = DaysA | DaysB
print(AllDays)

DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
AllDays = DaysA & DaysB
print(AllDays)

DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Wed", "Thu", "Fri", "Sat", "Sun"])
AllDays = DaysA - DaysB
print(AllDays)

DaysA = set(["Mon", "Tue", "Wed"])
DaysB = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)
