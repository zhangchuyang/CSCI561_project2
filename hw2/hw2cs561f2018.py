# class APPLICANT:
#     def __init__(self, ID, gender, age, pet, med_cond, car, dl, days):
#         self.ID = ID
#         self.gender = gender
#         self.age = age
#         self.pet = pet
#         self.med_cond = med_cond
#         self.car = car
#         self.dl = dl
#         self.week = []
#         self.programs = []
#         if self.car == "Y" and self.dl == "Y" and self.med_cond == "N": self.programs.append('spla')
#         if self.gender == "F" and self.age > 17 and self.pet == "N":    self.programs.append('lahsa')
#
#         if days[0] == "1":  self.week.append("M")
#         if days[1] == "1":  self.week.append("T")
#         if days[2] == "1":  self.week.append("W")
#         if days[3] == "1":  self.week.append("Th")
#         if days[4] == "1":  self.week.append("F")
#         if days[5] == "1":  self.week.append("Sat")
#         if days[6] == "1":  self.week.append("Sun")
#
# class LAHSA:
#     def __init__(self, b):
#         self.spaces = {"M": 0, "T": 0, "W": 0, "Th": 0, "F": 0, "Sat": 0, "Sun": 0}
#         self.efficiency = 0
#         self.availApplicants = []
#
#     def fits(self, applicant):
#         for days in applicant.week:
#             if self.spaces[days] >= b:  return False
#         return True
#
#     def addApplicants(self, applicant):
#         for days in applicant.week:
#             self.spaces[days] += 1
#             self.efficiency += 1
#
#     def removeApplicants(self, applicant):
#         for days in applicant.week:
#             self.spaces[days] -= 1
#             self.efficiency -= 1
#
# class SPLA:
#     def __init__(self, p):
#         self.spaces = {"M": 0, "T": 0, "W": 0, "Th": 0, "F": 0, "Sat": 0, "Sun": 0}
#         self.greedy_spaces = {"M": 0, "T": 0, "W": 0, "Th": 0, "F": 0, "Sat": 0, "Sun": 0}
#         self.efficiency = 0
#         self.greedy_efficiency = 0
#         self.availApplicants = []
#         self.greedyAvailApplicant = []
#
#     def fits(self, applicant):
#         for days in applicant.week:
#             if self.spaces[days] >= p:  return False
#         return True
#
#     def greedyFits(self, applicant):
#         for days in applicant.week:
#             if self.greedy_spaces[days] >= p:   return False
#         return True
#
#     def addApplicants(self, applicant):
#         for days in applicant.week:
#             self.spaces[days] += 1
#             self.efficiency += 1
#
#     def greedyApplicants(self, applicant):
#         for days in applicant.week:
#             self.greedy_spaces[days] += 1
#             self.greedy_efficiency += 1
#
#
#     def removeApplicants(self, applicant):
#         for days in applicant.week:
#             self.spaces[days] -= 1
#             self.efficiency -= 1
#
# def findLAHSAApplicant(spla, lahsa):
#     max_eff = -1
#     max_applicant = None
#     for applicant in lahsa.availApplicants[:]:
#         lahsa.availApplicants.remove(applicant)
#         isRemoved, isAdded = False
#         if lahsa.fits(applicant):
#             lahsa.addApplicants(applicant)
#             isAdded = True
#             if applicant in spla.availApplicants:
#                 spla.availApplicants.remove(applicant)
#                 isRemoved = True
#         spla_eff, lahsa_eff = splaMax(spla, lahsa)
#         if lahsa_eff > max_eff or (lahsa_eff == max_eff and applicant.ID < max_applicant.ID):
#             max_eff = lahsa_eff
#             max_applicant = applicant
#         lahsa.availApplicants.append(applicant)
#         if isAdded:     lahsa.removeApplicants(applicant)
#         if isRemoved:   spla.availApplicants.append(applicant)
#     return max_applicant
#
# def splaMax(spla, lahsa):
#     if len(spla.availApplicants) == 0 and len(lahsa.availApplicants) == 0:      return spla.efficiency, lahsa.efficiency
#     elif len(spla.availApplicants) == 0:    return lahsaMax(spla, lahsa)
#     spla_eff = -1
#     lahsa_eff = -1
#     for applicant in spla.availApplicants[:]:
#         spla.availApplicants.remove(applicant)
#         isRemoved = False
#         isAdded = False
#         if spla.fits(applicant):
#             spla.addApplicants(applicant)
#             isAdded = True
#             if applicant in lahsa.availApplicants:
#                 lahsa.availApplicants.remove(applicant)
#                 isRemoved = True
#         temp_spla_eff, temp_lahsa_eff = lahsaMax(spla, lahsa)
#         if temp_spla_eff > spla_eff:
#             spla_eff = temp_spla_eff
#             lahsa_eff = temp_lahsa_eff
#         spla.availApplicants.append(applicant)
#         if isAdded:     spla.removeApplicants(applicant)
#         if isRemoved:   lahsa.availApplicants.append(applicant)
#     return spla_eff, lahsa_eff
#
# def lahsaMax(spla, lahsa):
#     if len(spla.availApplicants) == 0 and len(lahsa.availApplicants) == 0:  return spla.efficiency, lahsa.efficiency
#     elif len(lahsa.availApplicants) == 0:   return splaMax(spla, lahsa)
#     spla_eff = -1
#     lahsa_eff = -1
#     for applicant in lahsa.availApplicants[:]:
#         lahsa.availApplicants.remove(applicant)
#         isRemoved = False
#         isAdded = False
#         if lahsa.fits(applicant):
#             lahsa.addApplicants(applicant)
#             isAdded = True
#             if applicant in spla.availApplicants:
#                 spla.availApplicants.remove(applicant)
#                 isRemoved = True
#         temp_spla_eff, temp_lahsa_eff = splaMax(spla, lahsa)
#         if temp_lahsa_eff > lahsa_eff:
#             spla_eff = temp_spla_eff
#             lahsa_eff = temp_lahsa_eff
#         lahsa.availApplicants.append(applicant)
#         if isAdded:     lahsa.removeApplicants(applicant)
#         if isRemoved:   spla.availApplicants.append(applicant)
#     return spla_eff, lahsa_eff
#
# def findSPLAApplicant(spla, lahsa):
#     max_eff = -1
#     max_applicant = None
#     for applicant in spla.availApplicants[:]:
#         spla.availApplicants.remove(applicant)
#         isRemoved = False
#         isAdded = False
#         if spla.fits(applicant):
#             spla.addApplicants(applicant)
#             isAdded = True
#             if applicant in lahsa.availApplicants:
#                 lahsa.availApplicants.remove(applicant)
#                 isRemoved = True
#         spla_eff, lahsa_eff = lahsaMax(spla, lahsa)
#         if spla_eff > max_eff or (spla_eff == max_eff and applicant.ID < max_applicant.ID):
#             max_eff = spla_eff
#             max_applicant = applicant
#         spla.availApplicants.append(applicant)
#         if isAdded:     spla.removeApplicants(applicant)
#         if isRemoved:   lahsa.availApplicants.append(applicant)
#     return max_applicant
#
# f = open('input25.txt')
# fp = open('output.txt', 'w')
# b = int((f.readline()).strip('\n'))
# p = int((f.readline()).strip('\n'))
# l = int((f.readline()).strip('\n'))
# lahsa_chosen = []
# for _ in range(l):
#     lahsa_chosen.append(str((f.readline()).strip('\n')))
# print(lahsa_chosen)
# s = int((f.readline()).strip('\n'))
# print(s)
# spla_chosen = []
# for _ in range(s):
#     spla_chosen.append(str((f.readline()).strip('\n')))
# print(spla_chosen)
# a = int((f.readline()).strip('\n'))
# total_applicant_info = []
# for _ in range(a):
#     total_applicant_info.append(str((f.readline()).strip('\n')))
# print(total_applicant_info)
#
# lahsa = LAHSA(b)
# spla = SPLA(p)
#
# for _ in total_applicant_info:
#     ID = _[0:5]
#     gender = _[5]
#     age = int(_[6:9])
#     pet = _[9]
#     med_cond = _[10]
#     car = _[11]
#     dl = _[12]
#     days = _[13:]
#
#     applicant = APPLICANT(ID, gender, age, pet, med_cond, car, dl, days)
#
#     if applicant.ID in spla_chosen:     spla.addApplicants(applicant)
#     elif applicant.ID in lahsa_chosen:  lahsa.addApplicants(applicant)
#     else:
#         if "spla" in applicant.programs:    spla.availApplicants.append(applicant)
#         if "lahsa" in applicant.programs:   lahsa.availApplicants.append(applicant)
#     print(applicant.ID, applicant.week, applicant.programs)
# spla.greedyAvailApplicant = spla.availApplicants
#
# notFull = True
# for applicant in spla.availApplicants:
#     if spla.greedyFits(applicant):  spla.greedyApplicants(applicant)
#     else:
#         notFull = False
#         break
# if notFull:
#     def findSmallIDForApplicant(spla):
#         maxDays = 0
#         numberOfBiggest = 0
#         sameBiggestList = []
#         minID = "99999"
#         for applicant in spla.greedyAvailApplicant:
#             if "lahsa" in applicant.programs:
#                 if len(applicant.week) > maxDays:
#                     maxDays = len(applicant.week)
#                     maxApplicant = applicant
#                     numberOfBiggest = 0
#                     sameBiggestList = []
#                     sameBiggestList.append(maxApplicant)
#                 elif len(applicant.week) == maxDays:
#                     numberOfBiggest += 1
#                     sameBiggestList.append(applicant)
#         if sameBiggestList == []:   return None
#         if sameBiggestList != [] and len(sameBiggestList) % 2 == 1:
#             for applicant in sameBiggestList:
#                 if applicant.ID < minID:
#                     minID = applicant.ID
#             return minID
#         if sameBiggestList != [] and len(sameBiggestList) %2 == 0:
#             for applicant in sameBiggestList:
#                 spla.greedyAvailApplicant.remove(applicant)
#             findSmallIDForApplicant(spla)
#     ID = findSmallIDForApplicant(spla)
#     if not ID:
#         minDays = 7
#         for applicant in spla.availApplicants:
#             if len(applicant.week) < minDays:
#                 ID = applicant.ID
#                 minDays = len(applicant.week)
#     print("greedy: ", ID)
#     fp.write(ID + "\n")
#
# else:
#     while len(spla_chosen) > len(lahsa_chosen) and len(lahsa.availApplicants) > 0:
#         applicant = findLAHSAApplicant(spla, lahsa)
#         lahsa_chosen.append(applicant.ID)
#         lahsa.addApplicants(applicant)
#         lahsa.availApplicants.remove(applicant)
#         spla.availApplicants.remove(applicant)
#
#     applicant = findSPLAApplicant(spla, lahsa)
#     print("minimax: ", applicant.ID)
#
#     fp.write(applicant.ID + "\n")
# f.close()
# fp.close()


class APPLICANT:
    def __init__(self, ID, gender, age, pet, med_cond, car, dl, days):
        self.ID = ID
        self.gender = gender
        self.age = age
        self.pet = pet
        self.med_cond = med_cond
        self.car = car
        self.dl = dl
        self.week = []
        self.programs = []
        if self.car == "Y" and self.dl == "Y" and self.med_cond == "N": self.programs.append('spla')
        if self.gender == "F" and self.age > 17 and self.pet == "N":    self.programs.append('lahsa')

        if days[0] == "1":  self.week.append("M")
        if days[1] == "1":  self.week.append("T")
        if days[2] == "1":  self.week.append("W")
        if days[3] == "1":  self.week.append("Th")
        if days[4] == "1":  self.week.append("F")
        if days[5] == "1":  self.week.append("Sat")
        if days[6] == "1":  self.week.append("Sun")

class LAHSA:
    def __init__(self, b):
        self.spaces = {"M": 0, "T": 0, "W": 0, "Th": 0, "F": 0, "Sat": 0, "Sun": 0}
        self.efficiency = 0
        self.availApplicants = []

    def fits(self, applicant):
        for days in applicant.week:
            if self.spaces[days] >= b:  return False
        return True

    def addApplicants(self, applicant):
        for days in applicant.week:
            self.spaces[days] += 1
            self.efficiency += 1

    def removeApplicants(self, applicant):
        for days in applicant.week:
            self.spaces[days] -= 1
            self.efficiency -= 1

class SPLA:
    def __init__(self, p):
        self.spaces = {"M": 0, "T": 0, "W": 0, "Th": 0, "F": 0, "Sat": 0, "Sun": 0}
        self.greedy_spaces = {"M": 0, "T": 0, "W": 0, "Th": 0, "F": 0, "Sat": 0, "Sun": 0}
        self.efficiency = 0
        self.greedy_efficiency = 0
        self.availApplicants = []

    def fits(self, applicant):
        for days in applicant.week:
            if self.spaces[days] >= p:  return False
        return True

    def greedFits(self, applicant):
        for days in applicant.week:
            print(self.greedy_spaces)

            if self.greedy_spaces[days] >= p:
                return False
        return True

    def addApplicants(self, applicant):
        for days in applicant.week:
            self.spaces[days] += 1
            self.efficiency += 1

    def greedyApplicants(self, applicant):
        for days in applicant.week:
            self.greedy_spaces[days] += 1
            self.greedy_efficiency += 1
    def removeApplicants(self, applicant):
        for days in applicant.week:
            self.spaces[days] -= 1
            self.efficiency -= 1

def findLAHSAApplicant(spla, lahsa):
    max_eff = -1
    max_applicant = None
    for applicant in lahsa.availApplicants[:]:
        lahsa.availApplicants.remove(applicant)
        isRemoved, isAdded = False
        if lahsa.fits(applicant):
            lahsa.addApplicants(applicant)
            isAdded = True
            if applicant in spla.availApplicants:
                spla.availApplicants.remove(applicant)
                isRemoved = True
        spla_eff, lahsa_eff = splaMax(spla, lahsa)
        if lahsa_eff > max_eff or (lahsa_eff == max_eff and applicant.ID < max_applicant.ID):
            max_eff = lahsa_eff
            max_applicant = applicant
        lahsa.availApplicants.append(applicant)
        if isAdded:     lahsa.removeApplicants(applicant)
        if isRemoved:   spla.availApplicants.append(applicant)
    return max_applicant

def splaMax(spla, lahsa):
    if len(spla.availApplicants) == 0 and len(lahsa.availApplicants) == 0:      return spla.efficiency, lahsa.efficiency
    elif len(spla.availApplicants) == 0:    return lahsaMax(spla, lahsa)
    spla_eff = -1
    lahsa_eff = -1
    for applicant in spla.availApplicants[:]:
        spla.availApplicants.remove(applicant)
        isRemoved = False
        isAdded = False
        if spla.fits(applicant):
            spla.addApplicants(applicant)
            isAdded = True
            if applicant in lahsa.availApplicants:
                lahsa.availApplicants.remove(applicant)
                isRemoved = True
        temp_spla_eff, temp_lahsa_eff = lahsaMax(spla, lahsa)
        if temp_spla_eff > spla_eff:
            spla_eff = temp_spla_eff
            lahsa_eff = temp_lahsa_eff
        spla.availApplicants.append(applicant)
        if isAdded:     spla.removeApplicants(applicant)
        if isRemoved:   lahsa.availApplicants.append(applicant)
    return spla_eff, lahsa_eff

def lahsaMax(spla, lahsa):
    if len(spla.availApplicants) == 0 and len(lahsa.availApplicants) == 0:  return spla.efficiency, lahsa.efficiency
    elif len(lahsa.availApplicants) == 0:   return splaMax(spla, lahsa)
    spla_eff = -1
    lahsa_eff = -1
    for applicant in lahsa.availApplicants[:]:
        lahsa.availApplicants.remove(applicant)
        isRemoved = False
        isAdded = False
        if lahsa.fits(applicant):
            lahsa.addApplicants(applicant)
            isAdded = True
            if applicant in spla.availApplicants:
                spla.availApplicants.remove(applicant)
                isRemoved = True
        temp_spla_eff, temp_lahsa_eff = splaMax(spla, lahsa)
        if temp_lahsa_eff > lahsa_eff:
            spla_eff = temp_spla_eff
            lahsa_eff = temp_lahsa_eff
        lahsa.availApplicants.append(applicant)
        if isAdded:     lahsa.removeApplicants(applicant)
        if isRemoved:   spla.availApplicants.append(applicant)
    return spla_eff, lahsa_eff

def findSPLAApplicant(spla, lahsa):
    max_eff = -1
    max_applicant = None
    for applicant in spla.availApplicants[:]:
        spla.availApplicants.remove(applicant)
        isRemoved = False
        isAdded = False
        if spla.fits(applicant):
            spla.addApplicants(applicant)
            isAdded = True
            if applicant in lahsa.availApplicants:
                lahsa.availApplicants.remove(applicant)
                isRemoved = True
        spla_eff, lahsa_eff = lahsaMax(spla, lahsa)
        if spla_eff > max_eff or (spla_eff == max_eff and applicant.ID < max_applicant.ID):
            max_eff = spla_eff
            max_applicant = applicant
        spla.availApplicants.append(applicant)
        if isAdded:     spla.removeApplicants(applicant)
        if isRemoved:   lahsa.availApplicants.append(applicant)
    return max_applicant

f = open('input8(1).txt')
fp = open('output.txt', 'w')
b = int((f.readline()).strip('\n'))
p = int((f.readline()).strip('\n'))
l = int((f.readline()).strip('\n'))
lahsa_chosen = []
for _ in range(l):
    lahsa_chosen.append(str((f.readline()).strip('\n')))
print(lahsa_chosen)
s = int((f.readline()).strip('\n'))
print(s)
spla_chosen = []
for _ in range(s):
    spla_chosen.append(str((f.readline()).strip('\n')))
print(spla_chosen)
a = int((f.readline()).strip('\n'))
total_applicant_info = []
for _ in range(a):
    total_applicant_info.append(str((f.readline()).strip('\n')))
print(total_applicant_info)

lahsa = LAHSA(b)
spla = SPLA(p)

for _ in total_applicant_info:
    ID = _[0:5]
    gender = _[5]
    age = int(_[6:9])
    pet = _[9]
    med_cond = _[10]
    car = _[11]
    dl = _[12]
    days = _[13:]

    applicant = APPLICANT(ID, gender, age, pet, med_cond, car, dl, days)

    if applicant.ID in spla_chosen:     spla.addApplicants(applicant)
    elif applicant.ID in lahsa_chosen:  lahsa.addApplicants(applicant)
    else:
        if "spla" in applicant.programs:    spla.availApplicants.append(applicant)
        if "lahsa" in applicant.programs:   lahsa.availApplicants.append(applicant)
    print(applicant.ID, applicant.week, applicant.programs)

notFull = True
maxDays = 0
maxApplicant = None
print(spla.availApplicants)
for applicant in spla.availApplicants:
    if spla.fits(applicant):
        spla.greedyApplicants(applicant)
    else:
        notFull = False
        break
if notFull:
    for applicant in spla.availApplicants:
        if "lahsa" in applicant.programs:
            if len(applicant.week) > maxDays:
                maxDays = len(applicant.week)
                maxApplicant = applicant
    if not maxApplicant:
        for applicant in spla.availApplicants:
            if len(applicant.week) > maxDays:
                maxDays = len(applicant.week)
                maxApplicant = applicant
    print("greedy: ", maxApplicant.ID)
    fp.write(maxApplicant.ID + "\n")

else:
    while len(spla_chosen) > len(lahsa_chosen) and len(lahsa.availApplicants) > 0:
        applicant = findLAHSAApplicant(spla, lahsa)
        lahsa_chosen.append(applicant.ID)
        lahsa.addApplicants(applicant)
        lahsa.availApplicants.remove(applicant)
        spla.availApplicants.remove(applicant)

    applicant = findSPLAApplicant(spla, lahsa)
    print("minimax: ", applicant.ID)

    fp.write(applicant.ID + "\n")
f.close()
fp.close()