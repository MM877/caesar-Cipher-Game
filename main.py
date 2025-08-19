print("""_,aaaaaaaaaaaaaaaaaaa,_                _,aaaaaaaaaaaI    Iaa,_
  ,P"                     "Y,            ,P"            I    I   "Y,
 d'    ,aaaaaaaaaaaaaaa,    `b          d'    ,aaaaaaaaaI    I,    `b
d'   ,d"            ,aaabaaaa8aaaaaaaaaa8aaaadaaa,      I    I"b,   `b
I    I  ,adba,      I                            I      `"YP"'  I    I
Y,   `Y,I    I      `aaaaaaaaaaaaaaaaaaaaaaaaaaaa'            ,P'   ,P
 Y,   `bI    Iaaaaaaaaad'   ,P          Y,   `baaaaaaaaaaaaaaad'   ,P
  `b,   I    I            ,d'            `b,                     ,d'
    `baaI    Iaaaaaaaaaaad'                `baaaaaaaaaaaaaaaaaaad'
        I    I
        I    I                 
    _,aaI    Iaaaaaaaaaaa,_                _,aaaaaaaaaaaaaaaaaaa,_
  ,P"   I    I            "Y,            ,P"                     "Y,
 d'    ,I    Iaaaaaaaaa,    `b          d'    ,aaaaaaaaaaaaaaa,    `b
d'   ,d"I    I      ,aaabaaaa8aaaaaaaaaa8aaaadaaa,            "b,   `b
I    I  `"YP"'      I                            I              I    I
Y,   `Y,            `aaaaaaaaaaaaaaaaaaaaaaaaaaaa'            ,P'   ,P
 Y,   `baaaaaaaaaaaaaaad'   ,P          Y,   `baaaaaaaaaaaaaaad'   ,P
  `b,                     ,d'            `b,                     ,d'
    `baaaaaaaaaaaaaaaaaaad'                `baaaaaaaaaaaaaaaaaaad'
'""")

# alphabet = [chr(i) for i in range(65, 91)] 

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G',
    'H', 'I', 'J', 'K', 'L', 'M', 'N',
    'O', 'P', 'Q', 'R', 'S', 'T', 'U',
    'V', 'W', 'X', 'Y', 'Z'
]

direction=input("type encode to encrypt   or decode to decrypt \n")

text= input("type ur message ").lower()
shift = int(input("type the shift number \n"))

# function encrypt original_text and shift  

        