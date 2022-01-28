# RAD-ASS: the RADius-mASS relationship of exoplanets

# Import Packages

import numpy as np
import matplotlib.pyplot as plt

# Latex & universal fontsize for plotting

plt.rc('text',usetex=True)
fontsize=15
plt.rc('xtick',labelsize=fontsize)
plt.rc('ytick',labelsize=fontsize)

# Graph Design

plt.figure("RAD ASS Graph",figsize=(16,9))
plt.title("RAD ASS Relationships")
plt.grid(axis="both",color="#4d50ff")

plt.xlabel(r'Planetary Mass $[M_{Earth}]$', color="#b76e79",
    fontsize="14",family="cursive")
plt.ylabel(r'Planetary Radius $[M_{Earth}]$', color="#b76e79", 
    fontsize="14",family="cursive")
plt.xscale('log')
plt.yscale('log')

# Load exoplanet_data

exo_data = np.loadtxt("./01-RAD_ASS_DATA.txt")
mass = exo_data[:,0]
radii = exo_data[:,1]

# Set upper and lower bound parameters

mass_lower_log = np.log(mass[mass<80])
mass_upper_log = np.log(mass[mass>80])
radius_lower_log = np.log(radii[mass<80])
radius_upper_log = np.log(radii[mass>80])

#

upper_bound_fit=np.polyfit(mass_lower_log, radius_lower_log,1)
lower_bound_fit=np.polyfit(mass_upper_log, radius_upper_log,1)
print(upper_bound_fit,lower_bound_fit)

# Turn the m&b into a polynomial

upper_bound_function = np.poly1d(upper_bound_fit)
lower_bount_function = np.poly1d(lower_bound_fit)

#

lower_region = np.linspace(-4,4.9,10)
upper_region = np.linspace(4.9,8,10)

# Plot the functions

plt.plot(np.exp(lower_region),np.exp(upper_bound_function(lower_region)),color="#b76e79")
plt.plot(np.exp(upper_region),np.exp(lower_bount_function(upper_region)),color="#b76e79")

# Sol_Sys_Mass_Rad_Data

Planets = ((0.055,0.3829, "Mercury","#bf4d3e",10),
    
    (0.815,0.9499, "Venus","#a1cb58",12),
    
    (1,1, "Earth","#077454",12),
    
    (0.107,0.533,"Mars","#ba3443",10),
    
    (317.8,11.209,"Jupiter","#ea8a21",60),
    
    (95.159,9.449,"Saturn","#e7c550",30),
    
    (14.536,4.007,"Uranus","#7463e3",15),
    
    (17.147,3.883,"Neptune","#1252cf",17),
    
    (0.00218,0.1868,"Pluto","#9ab6cc",5))

# Exoplanet_Plot

plt.plot(mass, radii, marker ="o", label= "Exoplanets",markerfacecolor='none',markeredgecolor="#d9b2b8",linestyle='none',markersize=8)

for mass_p, radius, name, color, markersize in Planets:
    plt.plot(mass_p, radius, markersize=markersize, label=name, color=color,marker="o",
    linestyle='none',markeredgewidth=0.0)
    
plt.legend(loc=2, numpoints=1,labelspacing=3.5)

plt.savefig('./03-RAD_ASS_figure.png',transparent=True,dpi=300)

plt.show()