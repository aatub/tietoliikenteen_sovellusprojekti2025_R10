import numpy as np
import matplotlib.pyplot as plt

def random_xyz():
    x= np.random.randint(1200,1800)
    y= np.random.randint(1200,1800)
    z=np.random.randint(1200,1800)
    return x,y,z

data = np.zeros((600,4))
data[0:100,:] = np.array([1800,1500,1500,0])
data[100:200,:] = np.array([1200,1500,1500,1])
data[200:300,:] = np.array([1500,1800,1500,2])
data[300:400,:] = np.array([1500,1200,1500,3])
data[400:500,:] = np.array([1500,1500,1800,4])
data[500:600,:] = np.array([1500,1500,1200,5])
data[:,0:3] = data[:,0:3] + 70*np.random.rand(600, 3)

y_data = data[:,3]

x_data = data[:,0:3]
N=600

kp=np.zeros((6,3))
for i in range(6):
    kp[i,:]=random_xyz()
    print(random_xyz())
    
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_data[:,0],x_data[:,1], x_data[:,2],color="pink")
ax.scatter(kp[:,0], kp[:,1], kp[:,2], color="black")
ax.set_xlabel("X-akseli")
ax.set_ylabel("Y-akseli")
ax.set_zlabel("Z-akseli")

plt.show() 

labels=np.zeros(N)
distance=np.zeros(6)
for step in range(5):
    for i in range (N):
        for k in range(6):
            distance[k]=np.sqrt(np.sum((x_data[i]-kp[k])**2))
        labels[i]=np.argmin(distance)

    for k in range(6):
        if np.sum(labels==k)>0:
            kp[k]= x_data[labels==k].mean(axis=0)
        else:
            kp[k,:]=random_xyz()

print(kp[:])
np.max(kp,axis=0)
np.min(kp,axis=0)
print("maximit",np.max(kp,axis=0))
print("minimit",np.min(kp,axis=0))


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x_data[:,0],x_data[:,1], x_data[:,2],color="pink")
ax.scatter(kp[:,0], kp[:,1], kp[:,2], color="black", marker="*", s=400)
ax.set_xlabel("X-akseli")
ax.set_ylabel("Y-akseli")
ax.set_zlabel("Z-akseli")

for i in range(N):
    c = int(labels[i])
    ax.plot(
        [x_data[i,0], kp[c,0]],
        [x_data[i,1], kp[c,1]],
        [x_data[i,2], kp[c,2]],
        color="gray",
        alpha=0.2
    )

plt.show()

