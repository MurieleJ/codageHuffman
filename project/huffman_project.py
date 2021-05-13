import heapq
import networkx as nx
import matplotlib.pyplot as plt
import queue
import random

infinity = 1000


abra = 'abracadabra'
long = 'Errare human est. Cogito, ergo sum. Dubito ergo cogito, cogito ergo sum, sum ergo Deus est '
exemple= 'Hello World'
ascii=[99,105,97]

#for c in 'Je vais à la pêche le dimanche.': 
#    print(c, ord(c))    # fonction ord() permet d'obtenir le code ASCII d'un caractère 
#for s in ascii:
#   print(chr(s))       # fonction chr() permet d'obtenir le caractère correspondant au code ASCII
#print([(k, chr(k)) for k in range(256)]) #pour obtenir les caractèes correspondant aux 256 codes ASCII

def integer_to_binary(n):    
#fonction qui prend un entier n et renvoie sa représentation binaire sous forme d'une chaîne de 8 caractères
    s = ''
    for k in range(8):
        s = str(n % 2) + s 
        n = n // 2
    return s
#print(integer_to_binary(54))

def coder_ascii(u): 
#fonction qui prend un mot u et renvoie sa représentation binaire sous forme d'une chaîne de x bits
    s = ''
    for a in u:
        s = s + integer_to_binary(ord(a))
    return s
#print(coder_ascii(long))
#print(len(coder_ascii(long)))
print('Hello World en code ASCII : ', coder_ascii(exemple))
print('Le nombre de bits pour Hello World en ASCII est de ', len(coder_ascii(exemple)))

code_long_fixe = {'a': '000', 'b': '001', 'c': '010', 'd' : '011', 'e' : '100', 'f' : '101'}
code_long_var = {'a': '0', 'b': '101', 'c': '100', 'd' : '111', 'e' : '1101', 'f' : '1100'}
#codage de Huffman pour Hello World TO DO : àimplémenter
code_long_var_ex = {'H': '1111', 'e': '010', 'l': '10', 'o' : '00', 'W' : '1101', 'r' : '1110', 'd' : '011', ' ' : '1100'}



def coder(s, code): 
#fonction qui prend une chaîne de caractère s et renvoie sa représentation dans le code "code"
    s1 = ''
    for a in s:
        s1 = s1 + code[a]
    return s1
print('Le codage de Huffman pour Hello World : ', coder(exemple,code_long_var_ex))
print('Le nombre de bits du codage de Huffman pour Hello World est de :' , len(coder(exemple,code_long_var_ex)))
print('Le taux de compression de Hello World avec le codage de Huffman est : ',1-(len(coder(exemple,code_long_var_ex)))/(len(coder_ascii(exemple)))  )

def sous_ascii(): 
    c = {}
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 0123456789,;:.' 
    for a in s:
        c[a] = integer_to_binary(ord(a)) 
    return c
code_ascii_partiel = sous_ascii()

def coder_ascii(u):
# fonction qui prend un mot u et renvoie sa représentation en code binaire
    return coder(u, code_ascii_partiel)


#print(coder('babaca', code_long_fixe))
#print(coder('babaca', code_long_var))
#print(coder_ascii('babaca'))
#print(coder(exemple, code_ascii_partiel))



############# decodage
def inverser(code):  #on créé uhn dictionnaire inverse
    d = {}
    for a in code: 
        d[code[a]] = a
    return d

inv_code_ascii_partiel=inverser(code_ascii_partiel)
#print(inv_code_ascii_partiel)

def decoder_ascii(s): 
    s1 = ''
    for k in range(len(s) // 8):
        a = s[8 * k: 8 * (k + 1)] 
        s1 = s1 + inv_code_ascii_partiel[a]
    return s1
v = coder_ascii(exemple) 
#print(v)
print('Le décodage ASCII de Hello World : ',decoder_ascii(v))


def est_prefixe(s1, s2): 
#fonction qui vérifie si deux chaines de caractère sont préfixes
    n = len(s1)
    return n <= len(s2) and s2[:n] == s1
#print(est_prefixe('ab', 'abc'))

def decoder(s, inv_code, dbg=False, pad=0):
#la fonction prend en paramètres une chaîne de 0 et de 1 et un "code inverse". 
# Elle renvoie la liste des mots dont le code est la chaîne s
    if dbg: print(pad * '.' + 'mot', s)
    if s == '':
        if dbg: print(pad * '.' + 'mot trouvé', s)
        return [''] 
    else:
        cs = [c for c in inv_code if est_prefixe(c, s)] 
        if dbg: print(pad * '.' + 'prefixes', *cs)
        sols = []
        for c in cs:
            m = len(c)
            sols1 = decoder(s[m:], inv_code, dbg, pad + 4) 
            sols = sols + [inv_code[c] + s1 for s1 in sols1]
        return sols
#inv_code = inverser(code_long_var)
inv_code = inverser(code_long_var_ex)
#s1 = coder('babacadaa', code_long_var) 
s1 = coder(exemple, code_long_var_ex)
#print(s1)
s2 = decoder(s1, inv_code) 
print('Le décodage de Huffman pour Hello World est :', s2) 

#### création de la table de codage
## création du dictionnaire

def table_frequences(texte):
#fonction qui renvoie le dictionnaire des occurences du texte d'entrée 
    table = {}
    for caractere in texte:
        if caractere in table:
            table[caractere] = table[caractere] + 1
        else:
            table[caractere] = 1
    return table

print('table de fréquence de Hello World ', table_frequences(exemple))


def faire_arbre(code): 
#prend en paramètre un code préfixe et renvoie l'arbre du code
    t = []
    for a in code:
        t = inserer_arbre(t, a, code[a])
    return t

def gauche(t):
# fonction qui renvoie le fils gauche de l'arbre t (arbre vide si t est vide)
    if t == []: return []
    elif t[0] == 'F':
        raise Exception('Feuille inattendue')
    else:
        return t[1]

def droit(t):
# fonction qui renvoie le fils droit de l'arbre t (arbre vide si t est vide)
    if t == []: return []
    elif t[0] == 'F':
        raise Exception('Feuille inattendue')
    else:
        return t[2]

def inserer_arbre(t, a, c): 
#insère un caractère a de code c dans l'arbre t
# renvoie un nouvel arbre, qui contient une nouvelle feuille d'étiquette a
    if c == '':
        return ['F', a] 
    elif c[0] == '0':
        t1 = inserer_arbre(gauche(t), a, c[1:])
        return ['N', t1, droit(t)] 
    else:
        t1 = inserer_arbre(droit(t), a, c[1:]) 
        return ['N', gauche(t), t1]

t = faire_arbre(code_long_var_ex) #code obtenu "manuellement"
print('Arbre obtenu avec codage Huffman fait à la main (entrée : code préfixe)', t)


def histogramme(u): 
#fonction qui calcule l'histogramme d'un mot
# Elle prend en paramètre un mot u et renvoie un dictionnaire qui associe à chaque lettre de u 
# le nombre d'occurences de celle-ci dans u
    h = {}
    for a in u:
        if a in h: 
            h[a] += 1 
        else: 
            h[a] = 1
    return h

print('L''histogramme de Hello World : ', histogramme(exemple))


def longueur(h, c): 
#prend en paramètres un histogramme h et un code c. 
# Elle renvoie l'entier B(c)
    s=0
    for a in h:
        s += h[a] * len(c[a])
    return s

def faire_arbre(h, dbg=False): 
#fonction qui créé l'arbre (non graphique) de Huffman, en entrée, elle prend un histogramme
    Q = []
    for a in h:
        heapq.heappush(Q, (h[a], ['F', a]))
    if dbg: print('File initiale :', Q) 
    for k in range(len(h) - 1):
        px, x = heapq.heappop(Q)
        py, y = heapq.heappop(Q)
        z = ['N', x, y]
        heapq.heappush(Q, (px + py, z))
        if dbg: print('Étape %d : %s' % (k, Q))
    return heapq.heappop(Q)[1]

t = faire_arbre(histogramme(exemple), dbg=True)
#t2 = faire_arbre(histogramme("Le professeur David Albert Huffman (9 août 1925 - 7 octobre 1999) fut un pionnier dans le domaine de l'informatique. Durant toute sa vie, Huffman apporta des contributions importantes à l'étude des machines à états finis. Mais Huffman est principalement connu pour l'invention du codage de Huffman utilisé dans presque toutes les applications qui impliquent la compression et la transmission de données numériques comme les fax, les modems, les réseaux informatiques et la télévision à haute définition."), dbg=True)
print('Arbre obtenu avec codage de Huffman par histogramme ', t)
#print(t2)

def faire_codes_aux(t, s): 
    if t[0] == 'F':
        return {t[1]: ''} 
    else:
        c1 = faire_codes_aux(t[1], '0') 
        c2 = faire_codes_aux(t[2], '1') 
        for k in c1: 
            c1[k] = '0' + c1[k] 
        for k in c2:
            c2[k] = '1' + c2[k] 
        c1.update(c2)
        return c1 

def faire_codes(t):
#fonction qui créé le code de Huffman, en entrée elle prend un arbre
    return faire_codes_aux(t, None)

t = faire_arbre(histogramme("Hello World"), dbg=True)
s = faire_codes(t)
print('Le code de Huffman de l''arbre (obtenu avec Histo) ', s)
#d = faire_code(t2)
#print(d)


def decoder_prefixe(s, t): 
#Si un code c préfixe et et t son arbre
# Pour décoder une chaîne s de 0 et de 1, on prend les caractères de s l'un après l'autre. 
# Si le caractère est un 0, on descend à gauche dans l'arbre. 
# Si c'est un 1, on descend à droite. 
# Lorsqu'on atteint une feuille on stocke la lettre qui est à cette feuille et on repart à la racine de l'arbre.
    t1 = t
    s1 = ''
    k = 0
    while k < len(s):
        if t1[0] == 'F':
            s1 = s1 + t1[1]
            t1 = t
        elif s[k] == '0':
            t1 = gauche(t1)
            k = k+1 
        else:
            t1 = droit(t1)
            k=k+1 
    return s1+ t1[1]


#t = faire_arbre(code_long_var_ex, dbg=True)
#s = coder(exemple, code_long_var_ex)
t = faire_arbre(code_long_var_ex)
s = coder(exemple, code_long_var_ex)
print('Le codage de la chaine s1 est ',s)
s1 = decoder_prefixe(s, t)
print('Le décodage de la chaine s est ', s1)