import numpy as np

matrise = np.array([[1,2,3],
                    [1,2,3],
                    [1,2,3],
                    [1,2,3]])

hoyde = len(matrise)
print("hoyde: ", hoyde)

hoydeVec = np.full(
  shape=hoyde,
  fill_value=1,
  dtype=np.int
).reshape(4,1)
print("hoydeVec: ", hoydeVec)

hoydeVec2 = np.full(
  shape=hoyde+1,
  fill_value=1,
  dtype=np.int
)
print("hoydeVec: ", hoydeVec2)

newImg = np.block([[hoydeVec2],[hoydeVec, matrise, hoydeVec], [hoydeVec2]])
print("newIMG: \n",newImg)