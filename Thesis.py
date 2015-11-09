
# coding: utf-8

# In[102]:

from rdflib import *
import numpy as np
import pylab
import os
import matplotlib.pyplot as plt
import matplotlib
import FuXi
from pandas import *
from IPython.lib.pretty import pprint
from tabulate import tabulate


# In[103]:

#Getting RDF datasets 
#Parsing Datasets
g = Graph()
g.parse("http://lamp.cse.fau.edu/~dterrel3/PoliceHomicides.rdf")
print("graph has %s statements." % len(g))


# In[104]:

#Getting Police Death Statistics 
#Displaying RDF Model
for s, p, o in g:
   if (s, p, o) not in g:
       raise Exception("It better be!")
#Printing Raw RDF DCAT Data
print( g.serialize(format='n3') )


# In[107]:

policeKillings = g.query("""
    SELECT ?state ?city ?race ?name ?armed ?cause ?age
         {  
            ?s :state ?state .
            ?s :city   ?city  .
            ?s :race  ?race .
            ?s :name  ?name .
            ?s :armed  ?armed .
            ?s :cause  ?cause .
            ?s :age  ?age .
            FILTER regex(?race, "^", "i")}
            LIMIT 50
    """)
#Print out Query
print("----------------------------- Police Homicides 2015 Figures------------------------\n")
headers = ['state','city','race','name','armed','cause','age']
#deathsByRace = tabulate(policeKillings,headers, tablefmt="fancy_grid")
deathsByRace = tabulate(policeKillings,headers)
print deathsByRace


# In[118]:

#Displaying the number of deaths for each race
#Running SPARQL Query to aggregaete RDF data
tbr = g.query("""
    SELECT DISTINCT ?race (COUNT(?race) AS ?rCount)
    WHERE{?s :race ?race.}
    GROUP BY ?race 
    ORDER BY DESC(?rCount)
    """)
#Print out Query
print("-----------------------------Total Homicides caused by Police ordered by Race------------------------\n")
headers2 = ['race','TOTAL DEATHS' ]
print tabulate(tbr,headers2,tablefmt="fancy_grid")


# In[122]:

#Displaying the number of deaths for each race
#Running SPARQL Query to aggregaete RDF data
la = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Los Angeles", "i") ||
            regex(?city, "Pomona", "i")||
            regex(?city, "Long Beach", "i")||
            regex(?city, "Needles", "i")||
            regex(?agency, "Long Beach", "i")||
            regex(?agency, "Los Angeles", "i")||
            regex(?city, "South El Monte", "i"))}
    ORDER BY DESC(?cCount)
    """)
headers2 = ['Agency','Metro Area','TOTAL DEATHS' ]
print tabulate(la,headers2,tablefmt="fancy_grid")
houst = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Houston", "i") ||
            regex(?city, "Missouri City", "i")||
            regex(?agency, "Missouri City", "i")||
            regex(?agency, "Houston", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(houst,headers2,tablefmt="fancy_grid")
mia = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "West Palm Beach", "i")||
            regex(?city, "Miami", "i")||
            regex(?agency, "Palm Beach", "i")||
            regex(?agency, "Broward", "i")||
            regex(?agency, "Fort Lauderdale", "i")||
            regex(?agency, "Miami", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(mia,headers2,tablefmt="fancy_grid")
ny = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "New York", "i")||
            regex(?city, "Newark", "i")||
            regex(?city, "Jersey City", "i")||
            regex(?agency, "Jersey City", "i")||
            regex(?agency, "Newark", "i")||
            regex(?agency, "New York", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(ny,headers2,tablefmt="fancy_grid")
bal = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Baltimore", "i")||
            regex(?city, "Columbia", "i")||
            regex(?city, "Towson", "i")||
            regex(?agency, "Baltimore", "i")||
            regex(?agency, "Columbia", "i")||
            regex(?agency, "Towson", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(bal,headers2,tablefmt="fancy_grid")
bos = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Boston", "i")||
            regex(?city, "Cambridge", "i")||
            regex(?city, "Newton", "i")||
            regex(?agency, "Boston", "i")||
            regex(?agency, "Cambridge", "i")||
            regex(?agency, "Newton", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(bos,headers2,tablefmt="fancy_grid")
char = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Charlotte", "i")||
            regex(?city, "Concord", "i")||
            regex(?city, "Gastonia,", "i")||
            regex(?agency, "Charlotte", "i")||
            regex(?agency, "Concord", "i")||
            regex(?agency, "Gastonia,", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(char,headers2,tablefmt="fancy_grid")
atl = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Atlanta", "i")||
            regex(?city, "Roswell", "i")||
            regex(?agency, "Sandy Springs", "i")||
            regex(?city, "Sandy Springs", "i")||
            regex(?agency, "Roswell", "i")||
            regex(?agency, "Atlanta", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(atl,headers2,tablefmt="fancy_grid")
chi = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Chicago", "i")||
            regex(?agency, "Chicago", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(chi,headers2,tablefmt="fancy_grid")
phoe = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Phoenix", "i")||
           regex(?city, "Mesa", "i")||
           regex(?city, "Scottsdale", "i")||
           regex(?agency, "Phoenix", "i")||
           regex(?agency, "Mesa", "i")||
            regex(?agency, "Scottsdale", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(phoe,headers2,tablefmt="fancy_grid")
dal = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Dallas", "i")||
            regex(?city, "Fort Worth", "i")||
            regex(?city, "Arlington", "i")||
            regex(?agency, "Fort Worth", "i")||
            regex(?agency, "Dallas", "i")||
            regex(?agency, "Arlington", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(dal,headers2,tablefmt="fancy_grid")
detr = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Detroit", "i")||
            regex(?city, "Warren", "i")||
            regex(?city, "Dearborn", "i")||
            regex(?agency, "Detroit", "i")||
            regex(?agency, "Warren", "i")||
            regex(?agency, "Dearborn", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(detr,headers2,tablefmt="fancy_grid")
denv = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Denver", "i")||
            regex(?city, "Aurora", "i")||
            regex(?city, "Lakewood", "i")||
            regex(?agency, "Denver", "i")||
            regex(?agency, "Aurora", "i")||
            regex(?agency, "Lakewood", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(denv,headers2,tablefmt="fancy_grid")
minn = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Minneapolis", "i")||
            regex(?city, "St Paul", "i")||
            regex(?city, "Bloomington", "i")||
            regex(?agency, "Minneapolis", "i")||
            regex(?agency, "St Paul", "i")||
            regex(?agency, "Bloomington", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(minn,headers2,tablefmt="fancy_grid")
phil = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Philadelphia", "i")||
            regex(?city, "Camden", "i")||
            regex(?city, "Wilmington", "i")||
            regex(?agency, "Philadelphia", "i")||
            regex(?agency, "Camden", "i")||
            regex(?agency, "Wilmington", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(phil,headers2,tablefmt="fancy_grid")
pitt = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Pittsburgh", "i")||
            regex(?agency, "Pittsburgh", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(pitt,headers2,tablefmt="fancy_grid")
port = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Portland", "i")||
            regex(?city, "Vancouver", "i")||
            regex(?city, "Hillsboro", "i")||
            regex(?agency, "Portland", "i")||
            regex(?agency, "Vancouver", "i")||
            regex(?agency, "Hillsboro", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(port,headers2,tablefmt="fancy_grid")
rivers = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Riverside", "i")||
            regex(?city, "San Bernardino", "i")||
            regex(?city, "Ontario", "i")||
            regex(?agency, "Riverside", "i")||
            regex(?agency, "San Bernardino", "i")||
            regex(?agency, "Ontario", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(rivers,headers2,tablefmt="fancy_grid")
stl = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "St Louis", "i")||
            regex(?agency, "St Louis", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(stl,headers2,tablefmt="fancy_grid")
sanant = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "San Antonio", "i")||
            regex(?city, "New Braunfels", "i")||
            regex(?agency, "San Antonio", "i")||
            regex(?agency, "New Braunfels", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(sanant,headers2,tablefmt="fancy_grid")
sand = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "San Diego", "i")||
            regex(?city, "Carlsbad", "i")||
            regex(?agency, "San Diego", "i")||
            regex(?agency, "Carlsbad", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(sand,headers2,tablefmt="fancy_grid")
sanf = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "San Francisco", "i")||
            regex(?city, "Oakland", "i")||
            regex(?city, "Hayward", "i")||
            regex(?agency, "San Francisco", "i")||
            regex(?agency, "Hayward", "i")||
            regex(?agency, "Oakland", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(sanf,headers2,tablefmt="fancy_grid")
seat = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Seattle", "i")||
            regex(?city, "Tacoma", "i")||
            regex(?city, "Bellevue", "i")||
            regex(?agency, "Seattle", "i")||
            regex(?agency, "Tacoma", "i")||
            regex(?agency, "Bellevue", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(seat,headers2,tablefmt="fancy_grid")
tamp = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Tampa", "i")||
            regex(?city, "St Petersburg", "i")||
            regex(?city, "Clearwater", "i")||
            regex(?agency, "Tampa", "i")||
            regex(?agency, "St Petersburg", "i")||
            regex(?agency, "Clearwater", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(tamp,headers2,tablefmt="fancy_grid")
dc = g.query("""
    SELECT DISTINCT ?agency ?city (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
    FILTER (regex(?city, "Washington", "i")||
            regex(?city, "Arlington", "i")||
            regex(?city, "Alexandria", "i")||
            regex(?agency, "Washington", "i")||
            regex(?agency, "Arlington", "i")||
            regex(?agency, "Alexandria", "i"))}
    ORDER BY DESC(?cCount)
    """)
print tabulate(dc,headers2,tablefmt="fancy_grid")


# In[124]:

#Displaying the number of deaths for each race
#Running SPARQL Query to aggregaete RDF data
la = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Los Angeles", "i") ||
            regex(?city, "Pomona", "i")||
            regex(?city, "Long Beach", "i")||
            regex(?city, "Needles", "i")||
            regex(?agency, "Long Beach", "i")||
            regex(?agency, "Los Angeles", "i")||
            regex(?city, "South El Monte", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
headers2 = ['Agency','Metro Area','Race','TOTAL DEATHS' ]
print tabulate(la,headers2,tablefmt="fancy_grid")
houst = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Houston", "i") ||
            regex(?city, "Missouri City", "i")||
            regex(?agency, "Missouri City", "i")||
            regex(?agency, "Houston", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(houst,headers2,tablefmt="fancy_grid")
mia = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "West Palm Beach", "i")||
            regex(?city, "Miami", "i")||
            regex(?agency, "Palm Beach", "i")||
            regex(?agency, "Broward", "i")||
            regex(?agency, "Fort Lauderdale", "i")||
            regex(?agency, "Miami", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(mia,headers2,tablefmt="fancy_grid")
ny = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "New York", "i")||
            regex(?city, "Newark", "i")||
            regex(?city, "Jersey City", "i")||
            regex(?agency, "Jersey City", "i")||
            regex(?agency, "Newark", "i")||
            regex(?agency, "New York", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(ny,headers2,tablefmt="fancy_grid")
bal = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Baltimore", "i")||
            regex(?city, "Columbia", "i")||
            regex(?city, "Towson", "i")||
            regex(?agency, "Baltimore", "i")||
            regex(?agency, "Columbia", "i")||
            regex(?agency, "Towson", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)    
    """)
print tabulate(bal,headers2,tablefmt="fancy_grid")
bos = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Boston", "i")||
            regex(?city, "Cambridge", "i")||
            regex(?city, "Newton", "i")||
            regex(?agency, "Boston", "i")||
            regex(?agency, "Cambridge", "i")||
            regex(?agency, "Newton", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(bos,headers2,tablefmt="fancy_grid")
char = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Charlotte", "i")||
            regex(?city, "Concord", "i")||
            regex(?city, "Gastonia,", "i")||
            regex(?agency, "Charlotte", "i")||
            regex(?agency, "Concord", "i")||
            regex(?agency, "Gastonia,", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(char,headers2,tablefmt="fancy_grid")
atl = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Atlanta", "i")||
            regex(?city, "Roswell", "i")||
            regex(?agency, "Sandy Springs", "i")||
            regex(?city, "Sandy Springs", "i")||
            regex(?agency, "Roswell", "i")||
            regex(?agency, "Atlanta", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(atl,headers2,tablefmt="fancy_grid")
chi = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Chicago", "i")||
            regex(?agency, "Chicago", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(chi,headers2,tablefmt="fancy_grid")
phoe = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Phoenix", "i")||
           regex(?city, "Mesa", "i")||
           regex(?city, "Scottsdale", "i")||
           regex(?agency, "Phoenix", "i")||
           regex(?agency, "Mesa", "i")||
            regex(?agency, "Scottsdale", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(phoe,headers2,tablefmt="fancy_grid")
dal = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Dallas", "i")||
            regex(?city, "Fort Worth", "i")||
            regex(?city, "Arlington", "i")||
            regex(?agency, "Fort Worth", "i")||
            regex(?agency, "Dallas", "i")||
            regex(?agency, "Arlington", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(dal,headers2,tablefmt="fancy_grid")
detr = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Detroit", "i")||
            regex(?city, "Warren", "i")||
            regex(?city, "Dearborn", "i")||
            regex(?agency, "Detroit", "i")||
            regex(?agency, "Warren", "i")||
            regex(?agency, "Dearborn", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(detr,headers2,tablefmt="fancy_grid")
denv = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Denver", "i")||
            regex(?city, "Aurora", "i")||
            regex(?city, "Lakewood", "i")||
            regex(?agency, "Denver", "i")||
            regex(?agency, "Aurora", "i")||
            regex(?agency, "Lakewood", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(denv,headers2,tablefmt="fancy_grid")
minn = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Minneapolis", "i")||
            regex(?city, "St Paul", "i")||
            regex(?city, "Bloomington", "i")||
            regex(?agency, "Minneapolis", "i")||
            regex(?agency, "St Paul", "i")||
            regex(?agency, "Bloomington", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(minn,headers2,tablefmt="fancy_grid")
phil = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Philadelphia", "i")||
            regex(?city, "Camden", "i")||
            regex(?city, "Wilmington", "i")||
            regex(?agency, "Philadelphia", "i")||
            regex(?agency, "Camden", "i")||
            regex(?agency, "Wilmington", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(phil,headers2,tablefmt="fancy_grid")
pitt = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Pittsburgh", "i")||
            regex(?agency, "Pittsburgh", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(pitt,headers2,tablefmt="fancy_grid")
port = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Portland", "i")||
            regex(?city, "Vancouver", "i")||
            regex(?city, "Hillsboro", "i")||
            regex(?agency, "Portland", "i")||
            regex(?agency, "Vancouver", "i")||
            regex(?agency, "Hillsboro", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(port,headers2,tablefmt="fancy_grid")
rivers = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Riverside", "i")||
            regex(?city, "San Bernardino", "i")||
            regex(?city, "Ontario", "i")||
            regex(?agency, "Riverside", "i")||
            regex(?agency, "San Bernardino", "i")||
            regex(?agency, "Ontario", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(rivers,headers2,tablefmt="fancy_grid")
stl = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "St Louis", "i")||
            regex(?agency, "St Louis", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(stl,headers2,tablefmt="fancy_grid")
sanant = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "San Antonio", "i")||
            regex(?city, "New Braunfels", "i")||
            regex(?agency, "San Antonio", "i")||
            regex(?agency, "New Braunfels", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(sanant,headers2,tablefmt="fancy_grid")
sand = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "San Diego", "i")||
            regex(?city, "Carlsbad", "i")||
            regex(?agency, "San Diego", "i")||
            regex(?agency, "Carlsbad", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(sand,headers2,tablefmt="fancy_grid")
sanf = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "San Francisco", "i")||
            regex(?city, "Oakland", "i")||
            regex(?city, "Hayward", "i")||
            regex(?agency, "San Francisco", "i")||
            regex(?agency, "Hayward", "i")||
            regex(?agency, "Oakland", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(sanf,headers2,tablefmt="fancy_grid")
seat = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Seattle", "i")||
            regex(?city, "Tacoma", "i")||
            regex(?city, "Bellevue", "i")||
            regex(?agency, "Seattle", "i")||
            regex(?agency, "Tacoma", "i")||
            regex(?agency, "Bellevue", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(seat)
tamp = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Tampa", "i")||
            regex(?city, "St Petersburg", "i")||
            regex(?city, "Clearwater", "i")||
            regex(?agency, "Tampa", "i")||
            regex(?agency, "St Petersburg", "i")||
            regex(?agency, "Clearwater", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(tamp,headers2,tablefmt="fancy_grid")
dc = g.query("""
    SELECT DISTINCT ?agency ?city ?race (COUNT(*) AS ?cCount)
    WHERE{?s :city ?city .
          ?s :agency ?agency .
          ?s :race ?race .
    FILTER (regex(?city, "Washington", "i")||
            regex(?city, "Arlington", "i")||
            regex(?city, "Alexandria", "i")||
            regex(?agency, "Washington", "i")||
            regex(?agency, "Arlington", "i")||
            regex(?agency, "Alexandria", "i"))}
    GROUP BY ?race
    ORDER BY DESC(?cCount)
    """)
print tabulate(dc,headers2,tablefmt="fancy_grid")

