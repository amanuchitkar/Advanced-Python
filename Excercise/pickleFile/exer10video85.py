import pickle

f = open('iris.txt')
r = f.read().splitlines()
f1 = open("ti.pkl", "wb")
f1.write(pickle.dumps(r))
f1.close()

f2 = open("ti.pkl", "rb")
f2.readable()
x = pickle.load(f2)
print(x)
f.close()
f2.close()
