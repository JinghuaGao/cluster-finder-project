#creat random catalog to test the cluster finding program
import numpy as np
import scipy as sp
from astropy.cosmology import WMAP9 as cosmo
from scipy.stats import cosine
import astropy.units as u
import random


n_cluster=1000 # number of clusters to set




def ztod_l(z):
	'return the distance from redshift z'
	return cosmo.luminosity_distance(z)
def ztod_a(z):
	'return the distance from redshift z'
	return cosmo.angular_diameter_distance(z)





#produce the mock ceters galaxys
raCenter=sp.random.random_sample(n_cluster)*2*np.pi
decCenter=cosine.rvs(size=n_cluster)/2
	#creat the redshift distribution along a exp function
zCenter=[]
while (len(zCenter)<n_cluster):
	x=5-random.expovariate(1)
	if((x>0.02)&(x<3)):
		zCenter.append(x/3.0)
	


#produce the member galaxies
catalog=[]
n_members=range(n_cluster)

for j in range(n_cluster):
	n_members[j]=sp.random.randint(100,1000) # randomly set the member number
	dia=(n_members[j]/1000+(sp.random.rand()-0.5)*0.03)*10*u.Mpc # give the diameter and add a 0.05 scatter.
	scale=dia/ztod_a(zCenter[j])/6  #the sigma that ra and dec should have.
	z_scale=dia/(ztod_l(zCenter[j]+0.005)-ztod_l(zCenter[j]-0.005))/6
	print 'the',j,'cluster: center at',raCenter[j]*180/np.pi,decCenter[j]*180/np.pi,zCenter[j],'has',n_members[j],'galaxies'
	for i in range(n_members[j]):
		raMem=raCenter[j]+sp.random.randn()*scale
		decMem=decCenter[j]+sp.random.randn()*scale
		zMem=zCenter[j]+sp.random.randn()*0.01*z_scale
		catalog.append([raMem,decMem,zMem])


catalog=np.array(catalog) #change shape to np.narray
num=np.arange(catalog.shape[0])
num=num.reshape(-1,1)
cat=np.append(num,catalog,axis=1)

np.savetxt('galaxy_mock.txt',cat,fmt='%d %f %f %f',header='num    ra    dec   redshift')


num=np.arange(n_cluster)
n_members=np.array(n_members)
raCenter=raCenter
decCenter=decCenter
zCenter=np.array(zCenter)
log=np.zeros([n_cluster,5])

log[:,0]=num
log[:,1]=n_members
log[:,2]=raCenter
log[:,3]=decCenter
log[:,4]=zCenter
np.savetxt('clusters.log',log,fmt='%d %d %f %f %f')





#set the back ground
#bias=sp.random.randn(n_member,3) #3d standard nromed distribution
#pass










