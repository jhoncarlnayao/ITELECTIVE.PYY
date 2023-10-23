import math


#BASIC VARIABLES

name="JHON CARL"   #str
age=19            #int
pocketmoney=200.5 #float 

# basic nga i print lang unsa naa saimo sulod sa variable
print(name)
print()

# sakani dinhi kay i print niya kung unsa ang naa sa index 0
print (name[0])
print()

#iprint niya kung sugod sa index 0 hangtod index 3
print (name[0:3])
print()

#Basically i print ra niya og kaduha 
print(name*2)
print()

#diria kay mura rakag nag add og another string  tas imo ra gitapad
print(name+" NAYAO")
print()

#icapitalize niya ang first letter 
print("jhoncarlnayao".capitalize())
print()

#ilower case naya tanan na naka capital
print("JHONCARLNAYAO".casefold())
print()

#so here kay i adjust niya ang space gikan sa pinaka una in math kay x chuchu siya
print("JhonCarlNayao".center(60))
print()

#i count niya pila ka letter/word imong gi butang sa sulod sa count 
print("Jhon Carl Nayao Carl".count("Carl"))
print()

#indicates that the string is of type "bytes." It's a way to represent and handle binary data.
print("Jhon Carl Nayao".encode())
print()

#short explanation gina search niya unsa imong gibutang sa endswith og ang imong gibutang sa endswith naasa list mo
#print siya og true and false kung dili niya makita
print("JhonCarlNayao , Kitty".endswith("Kitty"))
print()

#i think here medj libog siya pero more on spacing siya ? like gina adjust nya spacing kada word pero dapat
#mag gamit kag "\t" aron ma adjust
print("JHON\tCARL\tNAYAO".expandtabs(50))
print()

#kung unsa imo ibutang sa sulod sa find() kay iya na pangitaon sa gi butang nimo na string or int pag makita niya
#i print niya unsa nga index like kung aha niya na kita naindex
print("Jhon Carl Nayao".find("h"))
print()

#so here kay mura siya og variable pero ang kalahian needn imo mag butang og "{}"
# tas ang isulod nimo ana didto nimo itype sa format() inshort mura ra siyag variable
print("my name is {}".format("Jhon Carl Nayao"))
print()

#
print("Jhoncarl nayao".replace("nayao","jhoncarl"))





