

#so i think more on variable chuchu siya same2 lang sila unsay gamit i call lang nimo aron ma print siya
print("my name is {name} and i am {age} yrs old".format_map({"name":"Jhoncarl","age":30}))
print()

#i search niya kung aha naka butang ang letter na gusto nimo pangitaon and i print niya ang index kung aha niya nakita
print("JhoncarlNayao".index("J"))
print()

#pag naka in alphabet siya mo print siya og TRUE and kung naka numbers kay i print niya FALSE
print("JhoncarlNayao".isalpha())
print()

# so here icheck niya if numbers imo gibutang TRUE = numbers FALSE = alphabet
print("123123123".isalnum())
print()

#so diri same ra gihapon sa taas i print og true if naka number and false if alphabet
print("JhonCarlnayao".isdigit())
print()

#here ka i check niya if string/alphabet imo gibutang TRUE = string FALSE = int
print("Jhoncarlnayao".isidentifier())
print()

# TRUE = all lower case  FALSE = if upper case bisan isa lang
print("jhoncalnayao".islower())
print()

# TRUE = numbers/int   FALSE = letters/string
print("1231".isnumeric())
print()

#i check niya if printable ba imong gi buhat nga string (i guess)
print("JHONCARLNAYAO".isprintable())
print()

#pag space lang ang naa sa sulod sa " " kay TRUE pag naay unod nga letters or string false
print(" JHONCARL ".isspace())
print()

#naa siyay gina sunod nga capital letter chuchu kada word pinaka una nga letter dapat caps para mo print og TRUE
print("This Is Title".istitle())
print()

#TRUE = uppercase FALSE = lowercase
print("JHONCARL".isupper())
print()

#i think i add niya both first and last ???
print("carl".join("ad"))
print()

#sa right side niya mag add siya og "*" so ang 15 dinhaa mao na ang index pa right 
print("JHONCARLNAYAO".ljust(15,"*"))
print()

#convert into lowercase
print("JHONCARLNAYAO".lower())
print()

#iremove nya ang sa left banda kung unsa imo gusto iremove 
print("removehere JHONCARLNAYAO".lstrip("removehere"))
print()

#
print(str.maketrans("a","1"))
print()

#i think slize niya into three parts imo string ???
print("Jhoncarlnayao".partition("nayao"))
print()

#ireplace lang niya kung unsa gusto nimo ilisan 
print("JHONCARLNAYAO".replace("JHON","NAYAO"))
print()

#
print("JHON CARL NAYAO".rfind("H"))