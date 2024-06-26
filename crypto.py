n=str(input("Enter the plain text: "))

dict = {
    'a':"v345353v33",
    'b':"2ef34f343f",
    'c':"v34535rv33",
    'd':"2ef34f243f",
    'e':"v34535ev33",
    'f':"2ef34ef43f",
    'g':"v3453sev33",
    'h':"2ef232d43f",
    'i':"v343d23v33",
    'j':"2ef34fd43f",
    'k':"v345353v33",
    'l':"22f34f343f",
    'm':"vd45353v33",
    'n':"3ef34f343f",
    'o':"4345353v33",
    'p':"5ef34f343f",
    'q':"6345353v33",
    'r':"7ef34f343f",
    's':"8345353v33",
    't':"9ef34f343f",
    'u':"0345353v33",
    'v':"1ef34f343f",
    'w':"q345353v33",
    'x':"eef34f343f",
    'y':"t345353v33",
    'z':"pef34f343f",

}


en = ""
print("The Encryption of text is: ", end="")
for char in n:
    for item in dict:
        if char == item:
            en += dict.get(item)

print(en)




