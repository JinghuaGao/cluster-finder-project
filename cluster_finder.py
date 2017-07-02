#input the galaxy catalog to find the cluters in the sky.
#the algorithm is from the science paper 27 june 2014 VOL 344 

import numpy as np
import scipy as sp
import astropy as ap
from astropy.coordinates import SkyCoord
from astropy.cosmology import WMAP9 as cosmo
from astropy import units as u
import scipy.spatial.distance as dis
from scipy import cos,sin,arccos

#difine the important parameters 
catalog=np.loadtxt('redshiftcat.txt') #the catalog containing the galaxies of position.
size=catalog.shape[0] #the number of galaxies contained in the catalog.
d_c=0.02 #criteria defining the sky field for search neighbors.
d_c_larger=0.04 #criteria defining the sky field for searching galaxy of higher density
n_c=0.008*u.Mpc #criteria difining the cluster radial to find members in.



def ztod(z):
	'return the distance from redshift z'
	return cosmo.angular_diameter_distance(z)



class galaxy(object):
	def __init__(self,num,cat=catalog):
		self.Id=num
		self.Ra=cat[num,1]
		self.Dec=cat[num,2]
		self.redshift=cat[num,3]

		try:
			self.errorclass=cat[num,5]
			self.redshifterror=cat[num,4]
		except:
			self.errorclass='spectra'
		self.skycoord=SkyCoord(ra=self.Ra*u.radian, dec=self.Dec*u.radian, distance=ztod(self.redshift))
	
	def sepration(self,g,z):
		'caculate the galaxy distance from each other, g should be object of galaxy class'
		dis=ztod(z)*arccos(cos(g.Dec)*cos(self.Dec)*cos(g.Ra-self.Ra)+sin(g.Dec)*sin(self.Dec))
		return dis

	def neighbors(self):
		'return the id of neighbors for self'
		mask1=catalog[:,1]<self.Ra+d_c/cos(self.Dec)
		mask2=catalog[:,1]>self.Ra-d_c/cos(self.Dec)
		mask3=catalog[:,2]>self.Dec-d_c 
		mask4=catalog[:,2]<self.Dec+d_c 
		mask5=catalog[:,3]>self.redshift-0.025 
		mask6=catalog[:,3]<self.redshift+0.025 
		ids=np.arange(size)[mask1*mask2*mask3*mask4*mask5*mask6]
		return ids
	

	def lden(self):
		'the local density for the object'
		meanz=sp.mean([galaxy(i).redshift for i in self.neighbors()])
		a=[self.sepration(galaxy(i),meanz) for i in self.neighbors()]
		count=0
		for b in a:
			if(b<n_c):
				count=count+1
		return count
	

class block(object):
	def __init__(ra,dec,cat=catalog):

def theata(self):
	'the distance from galaxies of higher density'
	ids=self.neighbors()
	a=self.lden()
	if(self.lden()>10):
		c1=np.array([galaxy(i).lden() for i in ids])
		c2=np.array([self.seperation(self,galaxy(i)) for i in ids])
		c2=c2[c1>a]
		try:
			theata=np.min(c2)
		except:
			theata=ztod(self.redshift)*0.02
	else:
		theata=-10
		print 'density too low for galaxy',self.num
	return theata








