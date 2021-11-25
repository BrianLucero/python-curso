#                                                         https://github.com/BrianLucero/Python.git

lU = [9,4]
lD = [4,4]
lT = [3,7]
tU = (lU,lD,lT)

lCu = [1,1]
lCi = [7,7]
lS = [2,6]
tD = (lCu,lCi,lS)

lSi = [2,2]
lO = [20,20]
lN = [6,8]
tT = (lSi,lO,lN)

Ptupla = (tU, tD, tT)

nRepetir = set(tU[0]) 
nRepetirU = list(nRepetir) 
nRepetir = set(tU[1])
nRepetirD = list(nRepetir) 
nRepetir = set(tU[2]) 
nRepetirT = list(nRepetir) 
ntupla = (nRepetirU, nRepetirD, nRepetirT)
tU = ntupla

nRepetir = set(tD[0]) 
nRepetirU = list(nRepetir) 
nRepetir = set(tD[1]) 
nRepetirD = list(nRepetir) 
nRepetir = set(tD[2])
nRepetirT = list(nRepetir) 
ntupla = (nRepetirU, nRepetirD, nRepetirT)
tD = ntupla

nRepetir = set(tT[0]) 
nRepetirU = list(nRepetir) 
nRepetir = set(tT[1]) 
nRepetirD = list(nRepetir) 
nRepetir = set(tT[2]) 
nRepetirT = list(nRepetir) 
ntupla = (nRepetirU, nRepetirD, nRepetirT)
tT = ntupla

print("tupla original: ", Ptupla)
nTupla = (tU, tD, tT)
print("nueva tupla: ", nTupla)