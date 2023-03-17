v = int(input('Input velocity:'))
c = 299792458
light_speed = 299792458 

# 第一個公式求出 r
r = 1/(1-((v**2)/(c**2)))**(0.5)

'''
t_p = t_d / r  

** t_p: the travel time of a person in the ship **
** t_d: the time of light to the destination **

Alpha Centauri: 4.3 Light Years 
Barnard’s Star: 6.0 Light Years 
Betelgeuse (in the Milky Way): 309 Light Years 
Andromeda Galaxy (closest galaxy): 2000000 Light Years 
'''

print('Percentage of light speed =', v/light_speed ) 
print('Travel time to Alpha Centauri =', 4.3/r ) 
print("Travel time to Barnard's Star =", 6.0/r ) 
print("Travel time to Betelgeuse (in the Milky Way) =", 309/r ) 
print("Travel time to Andromeda Galaxy (closest galaxy) =", 2000000/r )


'''<output>

Input velocity: 149896229 
Percentage of light speed = 0.5
Travel time to Alpha Centauri = 3.7239092362730855
Travel time to Barnard's Star = 5.196152422706631
Travel time to Betelgeuse (in the Milky Way) = 267.6018497693915
Travel time to Andromeda Galaxy (closest galaxy) = 1732050.807568877

'''