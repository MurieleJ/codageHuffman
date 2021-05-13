from manim import *
import numpy as np


class CircleWithContent(VGroup):
    def __init__(self, content):
        super().__init__()
        self.circle = Circle()
        self.circle.set_fill(BLACK, opacity=1)
        self.content = content
        self.add(self.circle, content)
        content.move_to(self.circle.get_center())

    def clear_content(self):
        self.remove(self.content)
        self.content = None

    @override_animate(clear_content)
    def _clear_content_animation(self):
        anim = Uncreate(self.content)
        self.clear_content()
        return anim


#######################
#
# T I T R E
#
#######################

class Titre(Scene):
    def construct(self):
        
        ech = .5 # pour régler l'échelle
        l0 = Tex(r'Codage de Huffman').scale(1.5)
        l1 = Tex(r'Murièle Jacquier').scale(ech).next_to(l0, direction=DOWN, aligned_edge=LEFT)
        l2 = Tex(r'Simon Verdan').scale(ech).next_to(l1, direction=DOWN, aligned_edge=LEFT)
        l3 = Tex(r'GymInf 2021').scale(ech).next_to(l2, direction=DOWN, aligned_edge=LEFT)
        l4 = Tex(r'ASD I').scale(ech).next_to(l3, direction=DOWN, aligned_edge=LEFT)
        
        
        self.add(l0,l1,l2,l3,l4)
        self.wait(10)




#######################
#
# I N T R O
#
#######################

class Intro(Scene):
    def construct(self):
        
        ech = .5 # pour régler l'échelle
        l0 = Tex(r'Introduction du problème').scale(ech).move_to(np.array([-4,3.5 ,0]))
        l1 = Tex(r'(ici on décrit le problème résolu par le codage de Huffman)').scale(ech).next_to(l0, direction=DOWN, aligned_edge=LEFT)
        l2 = Tex(r'ex : Hello World et image 10x10').scale(ech).next_to(l1, direction=DOWN, aligned_edge=LEFT)
        l3 = Tex(r'Domaine (où comment pourquoi) + exemple générique').scale(ech).next_to(l2, direction=DOWN, aligned_edge=LEFT)
        l4 = Tex(r'Partie historique ?').scale(ech).next_to(l3, direction=DOWN, aligned_edge=LEFT)
        l5 = Tex(r'Codage préfixe ? (exemple du livre ou exemple ci-dessus)').scale(ech).next_to(l4, direction=DOWN, aligned_edge=LEFT)

        
        self.add(l0,l1,l2,l3,l4,l5)
        self.wait(10)

#########################
#
# T E X T E    A R B R E
#
#########################

class TexteArbre(Scene):
    def construct(self):
        
        ech = .5 # pour régler l'échelle
        l0 = Tex(r'100 caractères').scale(.7).move_to(np.array([-5, 3, 0]))
        l0b = Tex(r'lettres A..F').scale(.7).next_to(l0, direction=DOWN, aligned_edge=LEFT)
        
        
        l1 = Tex(r'DBAEECCAAADAADBACAAB').scale(ech).move_to(np.array([0, 1, 0]))
        l2 = Tex(r'BFDAFAAEAADADCAEABAD').scale(ech).next_to(l1, direction=DOWN, aligned_edge=LEFT)
        l3 = Tex(r'CCCAADAFFAABAAEADDCF').scale(ech).next_to(l2, direction=DOWN, aligned_edge=LEFT)
        l4 = Tex(r'ADAAEBDDDBAACCAAAABA').scale(ech).next_to(l3, direction=DOWN, aligned_edge=LEFT)
        l5 = Tex(r'BBDEECAAABBAAACAADAE').scale(ech).next_to(l4, direction=DOWN, aligned_edge=LEFT)

# TODO : en haut à gauche afficher 100 caractères, lettres A..F
# TODO : grouper, pousser à gauche, passer en ascii, afficher en haut à gauche ascii 7 bits et 700 bits
# TODO : ensuite revenir au texte de départ, le laisser à gauche, et afficher les fréquences en changeant les couleurs des lettres

        echA = .35
        as0 = Tex(r'100 caractères').scale(.7).move_to(np.array([-5, 3, 0]))
        as0b = Tex(r'ASCII 7 bits').scale(.7).next_to(as0, direction=DOWN, aligned_edge=LEFT)
        as0c = Tex(r'700 bits').set_color(RED).scale(.8).next_to(as0b, direction=DOWN, aligned_edge=LEFT)
        as1 = Tex(r'10001001000010100000110001011000101100001110000111000001100000110000011000100100000110000011000100100001010000011000011100000110000011000010').scale(echA).move_to(np.array([0, -1, 0]))
        as2 = Tex(r'10000101000110100010010000011000110100000110000011000101100000110000011000100100000110001001000011100000110001011000001100001010000011000100').scale(echA).next_to(as1, direction=DOWN, aligned_edge=LEFT)
        as3 = Tex(r'10000111000011100001110000011000001100010010000011000110100011010000011000001100001010000011000001100010110000011000100100010010000111000110').scale(echA).next_to(as2, direction=DOWN, aligned_edge=LEFT)
        as4 = Tex(r'10000011000100100000110000011000101100001010001001000100100010010000101000001100000110000111000011100000110000011000001100000110000101000001').scale(echA).next_to(as3, direction=DOWN, aligned_edge=LEFT)
        as5 = Tex(r'10000101000010100010010001011000101100001110000011000001100000110000101000010100000110000011000001100001110000011000001100010010000011000101').scale(echA).next_to(as4, direction=DOWN, aligned_edge=LEFT)


        





        #l6 = Tex(r"Analyse des fréquences d'apparition des lettres :").scale(ech).next_to(l5, direction=DOWN, aligned_edge=LEFT)
        #l7 = Tex(r'A : 45\,\%\ ; B : 13\,\%\ ; C : 12\,\%\ ; D : 16\,\%\ ; E : 9\,\%\ ; F : 5\,\%').scale(ech).next_to(l6, direction=DOWN, aligned_edge=LEFT)
        
        self.play(ShowCreation(l0))
        self.play(ShowCreation(l0b))
        self.play(ShowCreation(l1))
        self.play(ShowCreation(l2))
        self.play(ShowCreation(l3))
        self.play(ShowCreation(l4))
        self.play(ShowCreation(l5))
        self.wait(5)

        self.play(Transform(l0,as0))
        self.play(Transform(l0b,as0b))
        self.wait(.5)

        self.play(Transform(l1,as1))
        self.play(Transform(l2,as2))
        self.play(Transform(l3,as3))
        self.play(Transform(l4,as4))
        self.play(Transform(l5,as5))
        self.wait(.5)
        self.play(ShowCreation(as0c))

        self.wait(5)

        self.play(ShowCreation(l0))
        self.play(ShowCreation(l0b))
        self.play(ShowCreation(l1))
        self.play(ShowCreation(l2))
        self.play(ShowCreation(l3))
        self.play(ShowCreation(l4))
        self.play(ShowCreation(l5))

        self.wait(5)



        echA = .35 
        margeBoite = .5 
        t6 = Text("A:45").set_color(WHITE).scale(echA).shift(np.array([-1.5, -2, 0]))
        t4 = Text("B:13").set_color(WHITE).scale(echA).next_to(t6, direction=RIGHT, aligned_edge=LEFT, buff=margeBoite)
        t3 = Text("C:12").set_color(WHITE).scale(echA).next_to(t4, direction=RIGHT, aligned_edge=LEFT, buff=margeBoite)
        t5 = Text("D:16").set_color(WHITE).scale(echA).next_to(t3, direction=RIGHT, aligned_edge=LEFT, buff=margeBoite)
        t2 = Text("E:9 ").set_color(WHITE).scale(echA).next_to(t5, direction=RIGHT, aligned_edge=LEFT, buff=margeBoite)
        t1 = Text("F:5").set_color(WHITE).scale(echA).next_to(t2, direction=RIGHT, aligned_edge=LEFT, buff=margeBoite)

        bufferVal = .15
        f1 = SurroundingRectangle(t1, buff = bufferVal)
        b1 = BackgroundRectangle(f1,fill_color=BLACK,fill_opacity=1)
        f2 = SurroundingRectangle(t2, buff = bufferVal)
        b2 = BackgroundRectangle(f2,fill_color=BLACK,fill_opacity=1)
        f3 = SurroundingRectangle(t3, buff = bufferVal)
        b3 = BackgroundRectangle(f3,fill_color=BLACK,fill_opacity=1)
        f4 = SurroundingRectangle(t4, buff = bufferVal)
        b4 = BackgroundRectangle(f4,fill_color=BLACK,fill_opacity=1)
        f5 = SurroundingRectangle(t5, buff = bufferVal)
        b5 = BackgroundRectangle(f5,fill_color=BLACK,fill_opacity=1)
        f6 = SurroundingRectangle(t6, buff = bufferVal)
        b6 = BackgroundRectangle(f6,fill_color=BLACK,fill_opacity=1)
  
        x1 = VGroup(b1,f1,t1)
        x2 = VGroup(b2,f2,t2)
        x3 = VGroup(b3,t3,f3)
        x4 = VGroup(b4,t4,f4)
        x5 = VGroup(b5,t5,f5)
        x6 = VGroup(b6,t6,f6)

        self.play(ShowCreation(x6))
        self.play(ShowCreation(x4))
        self.play(ShowCreation(x3))
        self.play(ShowCreation(x5))
        self.play(ShowCreation(x2))
        self.play(ShowCreation(x1))

        self.wait(10)


#######################
#
# A R B R E
#
#######################

class Arbre(Scene):
    def construct(self):
        
        
        ### ALGO
        ech = .5 # pour régler l'échelle
        a0 = Tex(r'\textsc{Huffman}$(C)$').scale(ech).move_to(np.array([-5.75,3.5 ,0]))
        a1 = Tex(r'$1\quad n \leftarrow \vert C \vert$').scale(ech).next_to(a0, direction=DOWN, aligned_edge=LEFT)
        a2 = Tex(r'$2\quad Q \leftarrow C$').scale(ech).next_to(a1, direction=DOWN, aligned_edge=LEFT)
        a3 = Tex(r'$3\quad$\textbf{pour} $i \leftarrow 1$ \textbf{à} $n-1$').scale(ech).next_to(a2, direction=DOWN, aligned_edge=LEFT)
        a4 = Tex(r'$4\quad\quad$ \textbf{faire} allouer un nouveau n\oe ud $z$').scale(ech).next_to(a3, direction=DOWN, aligned_edge=LEFT)
        a5 = Tex(r'$5\quad\quad\quad$ gauche$[z] \leftarrow x \leftarrow$ \textsc{Extraire-Min}$(Q)$').scale(ech).next_to(a4, direction=DOWN, aligned_edge=LEFT)
        a6 = Tex(r'$6\quad\quad\quad$ droite$[z] \leftarrow y \leftarrow$ \textsc{Extraire-Min}$(Q)$').scale(ech).next_to(a5, direction=DOWN, aligned_edge=LEFT)
        a7 = Tex(r'$7\quad\quad\quad f[z] \leftarrow f[x] + f[y]$').scale(ech).next_to(a6, direction=DOWN, aligned_edge=LEFT)
        a8 = Tex(r'$8\quad\quad\quad$\textsc{Insérer}$(Q,z)$').scale(ech).next_to(a7, direction=DOWN, aligned_edge=LEFT)
        a9 = Tex(r'$9$ \textbf{retourner} \textsc{Extraire-Min}$(Q)$').scale(ech).next_to(a8, direction=DOWN, aligned_edge=LEFT)
        boucleValue = Tex(r'Valeurs pour la boucle :').scale(ech).next_to(a9, direction=DOWN, aligned_edge=LEFT)
        nValue = Tex(r'$n = 6$').scale(ech).next_to(boucleValue, direction=DOWN, aligned_edge=LEFT)
        iValue = Tex(r'$i = $').scale(ech).next_to(nValue, direction=DOWN, aligned_edge=LEFT)
        boucleValue.set_color(ORANGE)
        nValue.set_color(ORANGE)
        iValue.set_color(ORANGE)

        
        self.add(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9)
        
        
        self.wait(2)

        
        echA = .35 
        t1 = Text("f:5").set_color(WHITE).scale(echA).move_to(np.array([-1, 3, 0]))
        t2 = Text("e:9 ").set_color(WHITE).scale(echA).shift(np.array([0.2, 3, 0]))
        t3 = Text("c:12").set_color(WHITE).scale(echA).shift(np.array([1.5, 3, 0]))
        t4 = Text("b:13").set_color(WHITE).scale(echA).shift(np.array([2.9, 3, 0]))
        t5 = Text("d:16").set_color(WHITE).scale(echA).shift(np.array([4.3, 3, 0]))
        t6 = Text("a:45").set_color(WHITE).scale(echA).shift(np.array([5.7, 3, 0]))
        
        bufferVal = .15
        f1 = SurroundingRectangle(t1, buff = bufferVal)
        b1 = BackgroundRectangle(f1,fill_color=BLACK,fill_opacity=1)
        f2 = SurroundingRectangle(t2, buff = bufferVal)
        b2 = BackgroundRectangle(f2,fill_color=BLACK,fill_opacity=1)
        f3 = SurroundingRectangle(t3, buff = bufferVal)
        b3 = BackgroundRectangle(f3,fill_color=BLACK,fill_opacity=1)
        f4 = SurroundingRectangle(t4, buff = bufferVal)
        b4 = BackgroundRectangle(f4,fill_color=BLACK,fill_opacity=1)
        f5 = SurroundingRectangle(t5, buff = bufferVal)
        b5 = BackgroundRectangle(f5,fill_color=BLACK,fill_opacity=1)
        f6 = SurroundingRectangle(t6, buff = bufferVal)
        b6 = BackgroundRectangle(f6,fill_color=BLACK,fill_opacity=1)
  
        x1 = VGroup(b1,f1,t1)
        x2 = VGroup(b2,f2,t2)
        x3 = VGroup(b3,t3,f3)
        x4 = VGroup(b4,t4,f4)
        x5 = VGroup(b5,t5,f5)
        x6 = VGroup(b6,t6,f6)




# on affiche la valeur de n
        self.wait(.5)
        a1.set_color(RED)
        self.wait(.5)
        self.play(ShowCreation(boucleValue))
        self.play(ShowCreation(nValue))
        self.wait(1)
        a1.set_color(WHITE)
        self.wait(1)


# on affiche l'arbre Q 
        a2.set_color(RED)
        self.wait(.5)
        self.play(ShowCreation(x1))
        self.play(ShowCreation(x2))
        self.play(ShowCreation(x3))
        self.play(ShowCreation(x4))
        self.play(ShowCreation(x5))
        self.play(ShowCreation(x6))
        a2.set_color(WHITE)
        self.wait(1)

# on démarre la boucle, on affiche i
        i1 = Tex(r'$1$').scale(ech).move_to(np.array([-5.95,-2.22, 0]))
        i1.set_color(ORANGE)
        a3.set_color(RED)
        self.wait(.5)
        self.play(ShowCreation(iValue))
        self.play(ShowCreation(i1))
        self.wait(1)
        a3.set_color(WHITE)
        


#####  Étape (b)
        a4.set_color(RED)
        self.wait(.5)
        t00 = Text("00")
        x00 = CircleWithContent(t00).scale(echA).shift(np.array([2, 0, 0]))
        l21 = Line(np.array([1.75, -.25, 0]),np.array([1.4, -.75, 0]));
        l22 = Line(np.array([2.25, -0.25, 0]),np.array([2.6, -.75, 0]));
        self.add(x00)
        self.play(ShowCreation(l21))
        self.play(ShowCreation(l22))
        self.wait(1)
        a4.set_color(WHITE)
        
        a5.set_color(RED)
        self.wait(.5)
        self.play(x1.animate.move_to(np.array([1.2, -1, 0])))
        self.wait(1)
        a5.set_color(WHITE)

        a6.set_color(RED)
        self.wait(.5)
        self.play(x2.animate.move_to(np.array([2.8, -1, 0])))
        self.wait(1)
        a6.set_color(WHITE)

        t21 = Text("14")
        x21 = CircleWithContent(t21).scale(echA).shift(np.array([2, 0, 0]))
        a7.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(x00,x21))
        a7.set_color(WHITE)

        tl20 = Text("0").set_color(WHITE).scale(.3).move_to(np.array([1.4, -0.5, 0]))
        tl21 = Text("1").set_color(WHITE).scale(.3).move_to(np.array([2.6, -0.5, 0]))
        self.play(ShowCreation(tl20))
        self.play(ShowCreation(tl21))
       
        n14 = VGroup(l21,l22,x21,x1,x2,tl20,tl21)
        a8.set_color(RED)
        self.wait(.5)
        self.play(x3.animate.move_to(np.array([-1, 3, 0])))
        self.play(x4.animate.move_to(np.array([0.2, 3, 0])))
        self.play(n14.animate.move_to(np.array([2.2, 2.55, 0])))
        a8.set_color(WHITE)

        self.wait(1)


# on poursuit la boucle, on affiche i
        i2 = Tex(r'$2$').scale(ech).move_to(np.array([-5.95,-2.22, 0]))
        i2.set_color(ORANGE)
        a3.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(i1,i2))
        self.wait(1)
        a3.set_color(WHITE)
        
#####  Étape (c)
        a4.set_color(RED)
        self.wait(.5)
        t01 = Text("00")
        x01 = CircleWithContent(t01).scale(echA).shift(np.array([2, 0, 0]))
        l31 = Line(np.array([1.75, -.25, 0]),np.array([1.4, -.75, 0]));
        l32 = Line(np.array([2.25, -0.25, 0]),np.array([2.6, -.75, 0]));
        self.add(x01)
        self.play(ShowCreation(l31))
        self.play(ShowCreation(l32))
        self.wait(1)
        a4.set_color(WHITE)
  
            
        a5.set_color(RED)
        self.wait(.5)
        self.play(x3.animate.move_to(np.array([1.2, -1, 0])))
        self.wait(1)
        a5.set_color(WHITE)

        a6.set_color(RED)
        self.wait(.5)
        self.play(x4.animate.move_to(np.array([2.8, -1, 0])))
        self.wait(1)
        a6.set_color(WHITE)

        t31 = Text("25")
        x31 = CircleWithContent(t31).scale(echA).shift(np.array([2, 0, 0]))
        a7.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(x01,x31))
        a7.set_color(WHITE)

        tl30 = Text("0").set_color(WHITE).scale(.3).move_to(np.array([1.4, -0.5, 0]))
        tl31 = Text("1").set_color(WHITE).scale(.3).move_to(np.array([2.6, -0.5, 0]))
        self.play(ShowCreation(tl30))
        self.play(ShowCreation(tl31))
       
        n25 = VGroup(l31,l32,x31,x3,x4,tl30,tl31)
        a8.set_color(RED)
        self.wait(.5)
        self.play(n14.animate.move_to(np.array([1, 2.55, 0])))
        self.play(x5.animate.move_to(np.array([2.5, 3, 0])))
        self.play(n25.animate.move_to(np.array([4, 2.55, 0]))) # old : 4.2
        a8.set_color(WHITE)



# on poursuit la boucle, on affiche i
        i3 = Tex(r'$3$').scale(ech).move_to(np.array([-5.95,-2.22, 0]))
        i3.set_color(ORANGE)
        a3.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(i2,i3))
        self.wait(1)
        a3.set_color(WHITE)
       

#####  Étape (d)
        a4.set_color(RED)
        self.wait(.5)
        t02 = Text("00")
        x02 = CircleWithContent(t02).scale(echA).shift(np.array([2, 0, 0]))
        l41 = Line(np.array([1.75, -.25, 0]),np.array([1.4, -.75, 0]));
        l42 = Line(np.array([2.25, -0.25, 0]),np.array([2.6, -.75, 0]));
        self.add(x02)
        self.play(ShowCreation(l41))
        self.play(ShowCreation(l42))
        self.wait(1)
        a4.set_color(WHITE)
  
          
        a5.set_color(RED)
        self.wait(.5)
        self.play(n14.animate.move_to(np.array([1.2, -1.5, 0])))
        self.wait(1)
        a5.set_color(WHITE)
        
        a6.set_color(RED)
        self.wait(.5)
        self.play(x5.animate.move_to(np.array([2.8, -1, 0])))
        self.wait(1)
        a6.set_color(WHITE)

        t41 = Text("30")
        x41 = CircleWithContent(t41).scale(echA).shift(np.array([2, 0, 0]))
        a7.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(x02,x41))
        a7.set_color(WHITE)

        tl40 = Text("0").set_color(WHITE).scale(.3).move_to(np.array([1.4, -0.5, 0]))
        tl41 = Text("1").set_color(WHITE).scale(.3).move_to(np.array([2.6, -0.5, 0]))
        self.play(ShowCreation(tl40))
        self.play(ShowCreation(tl41))
       
        n30 = VGroup(l41,l42,x41,n14,x5,tl40,tl41)
        a8.set_color(RED)
        self.wait(.5)
        
        self.play(n25.animate.move_to(np.array([1, 2.55, 0])))
        self.play(n30.animate.move_to(np.array([4, 2, 0])))
        a8.set_color(WHITE)
        


# on poursuit la boucle, on affiche i
        i4 = Tex(r'$4$').scale(ech).move_to(np.array([-5.95,-2.22, 0]))
        i4.set_color(ORANGE)
        a3.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(i3,i4))
        self.wait(1)
        a3.set_color(WHITE)
       

#####  Étape (e)
        a4.set_color(RED)
        self.wait(.5)
        t03 = Text("00")
        x03 = CircleWithContent(t03).scale(echA).shift(np.array([2, 0, 0]))
        l51 = Line(np.array([1.75, -.25, 0]),np.array([.8, -.75, 0]));
        l52 = Line(np.array([2.25, -0.25, 0]),np.array([3.2, -.75, 0]));
        self.add(x03)
        self.play(ShowCreation(l51))
        self.play(ShowCreation(l52))
        self.wait(1)
        a4.set_color(WHITE)
  
          
        a5.set_color(RED)
        self.wait(.5)
        self.play(n25.animate.move_to(np.array([.6, -1.5, 0])))
        self.wait(1)
        a5.set_color(WHITE)
        
        a6.set_color(RED)
        self.wait(.5)
        self.play(n30.animate.move_to(np.array([3.02, -2.05, 0]))) # old y=-2 x=3.1 x=3.05
        self.wait(1)
        a6.set_color(WHITE)

        t51 = Text("55")
        x51 = CircleWithContent(t51).scale(echA).shift(np.array([2, 0, 0]))
        a7.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(x03,x51))
        a7.set_color(WHITE)

        tl50 = Text("0").set_color(WHITE).scale(.3).move_to(np.array([.8, -0.5, 0]))
        tl51 = Text("1").set_color(WHITE).scale(.3).move_to(np.array([3.2, -0.5, 0]))
        self.play(ShowCreation(tl50))
        self.play(ShowCreation(tl51))
       
        n55 = VGroup(l51,l52,x51,n25,n30,tl50,tl51)
        a8.set_color(RED)
        self.wait(.5)
        
        
        self.play(x6.animate.move_to(np.array([0, 3.5, 0]))) # old y=3
        self.play(n55.animate.move_to(np.array([4, 2, 0]))) # old y=1.5
        a8.set_color(WHITE)
        
# on poursuit la boucle, on affiche i
        i5 = Tex(r'$5$ (dernière itération)').scale(ech).move_to(np.array([-4.9,-2.22, 0])) # old x=-5.55 x=5
        i5.set_color(ORANGE)
        a3.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(i4,i5))
        self.wait(1)
        a3.set_color(WHITE)
       

#####  Étape (f)
        a4.set_color(RED)
        self.wait(.5)
        t04 = Text("00")
        x04 = CircleWithContent(t04).scale(echA).shift(np.array([2, 0, 0]))
        l61 = Line(np.array([1.75, -.25, 0]),np.array([.8, -.75, 0]));
        l62 = Line(np.array([2.25, -0.25, 0]),np.array([3.2, -.75, 0]));
        self.add(x04)
        self.play(ShowCreation(l61))
        self.play(ShowCreation(l62))
        self.wait(1)
        a4.set_color(WHITE)
  
          
        a5.set_color(RED)
        self.wait(.5)
        self.play(x6.animate.move_to(np.array([.6, -1, 0])))
        self.wait(1)
        a5.set_color(WHITE)
        
        a6.set_color(RED)
        self.wait(.5)
        self.play(n55.animate.move_to(np.array([3.5, -2.5, 0]))) # old : y=-2.1 x=3.1 x=3.35
        self.wait(1)
        a6.set_color(WHITE)

        t61 = Text("100")
        x61 = CircleWithContent(t61).scale(echA).shift(np.array([2, 0, 0]))
        a7.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(x04,x61))
        a7.set_color(WHITE)

        tl60 = Text("0").set_color(WHITE).scale(.3).move_to(np.array([.8, -0.5, 0]))
        tl61 = Text("1").set_color(WHITE).scale(.3).move_to(np.array([3.2, -0.5, 0]))
        self.play(ShowCreation(tl60))
        self.play(ShowCreation(tl61))
       
        n100 = VGroup(l61,l62,x61,x6,n55,tl60,tl61)
        a8.set_color(RED)
        self.wait(.5)
        
        self.play(n100.animate.move_to(np.array([3, 1, 0]))) # old y=2 y=1.5
        a8.set_color(WHITE)

        self.wait(2)

# dernière étape : l'extraction du min donne la racine de l'arborescence 
        a9.set_color(RED)
        self.wait(2)
        a9.set_color(WHITE)

        self.wait(3)



#######################
#
# LIMITATIONS
#
#######################

class Limitations(Scene):
    def construct(self):

        ech = .5 # pour régler l'échelle
        l0 = Tex(r'Limitations du codage de Huffman').scale(1.5).move_to(np.array([-1,3.5 ,0]))
        l1 = Tex(r'Le codage de Huffman impose d''utiliser un nombre entier de bits pour un symbole source').scale(1).next_to(l0, direction=DOWN, aligned_edge=LEFT)
        l2 = Tex(r'codage Huffman sur des blocs de n symboles').scale(0.7).next_to(l1, direction=DOWN, aligned_edge=LEFT)
        l3 = Tex(r'Le codage de Huffman évalue les probabilités des symboles au début, donc il n''est pas adapté dans le cas d''une source dont les propriétés statistiques évoluent').scale(1).next_to(l2, direction=DOWN, aligned_edge=LEFT)
        l4 = Tex(r'codage de Huffman adaptatif').scale(0.7).next_to(l3, direction=DOWN, aligned_edge=LEFT)
        
        
        self.play(Write(l0))
        self.wait(1)
        self.play(Write(l1))
        self.wait(1)
        self.play(Write(l2))
        self.wait(3)  
        self.play(Write(l3))
        self.wait(1)
        self.play(Write(l4))
        self.wait(10)


class Caractéristiques(Scene):
    def construct(self):

        ech = .5 # pour régler l'échelle
        l0 = Tex(r'Caractéristiques du code de Huffman').scale(1.5).move_to(np.array([-1,3.5 ,0]))
        l1 = Tex(r'Non-unicité').scale(1).next_to(l0, direction=DOWN, aligned_edge=LEFT)
        l2 = Tex(r'On peut produire des arbres différents pour un même alphabet').scale(0.7).next_to(l1, direction=DOWN, aligned_edge=LEFT)
        l3 = Tex(r'choix pour les éléments de même fréquence').scale(0.7).next_to(l2, direction=DOWN, aligned_edge=LEFT)
        l4 = Tex(r'   choix gauche/droite pour chaque noeud').scale(0.7).next_to(l3, direction=DOWN, aligned_edge=LEFT)
        l5 = Tex(r'Conséquences').scale(1).next_to(l4, direction=DOWN, aligned_edge=LEFT)
        l6 = Tex(r'Pour décoder, il faut fournir le code ou au moins donner les règles sur les choix').scale(0.7).next_to(l5, direction=DOWN, aligned_edge=LEFT)
        
        
        self.play(Write(l0))
        self.wait(1)
        self.play(Write(l1))
        self.wait(1)
        self.play(Write(l2))
        self.wait(1)  
        self.play(Write(l3),Write(l4))
        self.wait(3)
        self.play(Write(l5),Write(l6))
        self.wait(10)
        


#######################
#
# P R E U V E
#
#######################

class Preuve(Scene):
    def construct(self):
        
        ech = .5 # pour régler l'échelle
        l0 = Tex(r'Preuve').scale(2).move_to(np.array([-4,3.5 ,0]))
         l1 = Tex(r'2 étapes pour démontrer que l''algorithme glouton de Huffman est correct').scale(0.7).next_to(l0, direction=DOWN, aligned_edge=LEFT)
        l2 = Tex(r'Etape 1 : Lemme des fréquences faibles').scale(0.7).next_to(l1, direction=DOWN, aligned_edge=LEFT)  
        l3 = Tex(r'Soit C un alphabet dans lequel chaque caractère c in C a la fréquence c.freq.').scale(0.5).next_to(l2, direction=DOWN, aligned_edge=LEFT)
        l4 = Tex(r'Soient x et y deux caractères de C ayant les fréquences les plus basses.').scale(0.5).next_to(l3, direction=DOWN, aligned_edge=LEFT)
        l5 = Tex(r'Alors il existe un codage préface optimal pour C dans lequel les mots de code pour x et y ont la même longueur et ne diffèrent que par le dernier bit').scale(0.5).next_to(l4, direction=DOWN, aligned_edge=LEFT)
        l6 = Tex(r'Etape 2 : Lemme de propagation de l''optimalité').scale(0.7).next_to(l5, direction=DOWN, aligned_edge=LEFT)
        l7 = Tex(r'Soit C un alphabet dans lequel chaque caractère c in C a la fréquence c.freq.').scale(0.5).next_to(l6, direction=DOWN, aligned_edge=LEFT)
        l8 = Tex(r'Soient x et y deux caractères de C ayant la fréquence minimale.').scale(0.5).next_to(l7, direction=DOWN, aligned_edge=LEFT)
        l9 = Tex(r'Soit C'' l''alphabet C privé des caractères x et y et complété par un nouveau caractère, de sorte que C''=C-(x,y)U(z)').scale(0.5).next_to(l8, direction=DOWN, aligned_edge=LEFT)
        l10 = Tex(r'On définit C'' comme C sauf que z.freq=x.freq+y.freq').scale(0.5).next_to(l9, direction=DOWN, aligned_edge=LEFT)
        l11 = Tex(r'Soit T'' un arbre  représentant un code préfixe optimal pour l''alphabet C''').scale(0.5).next_to(l10, direction=DOWN, aligned_edge=LEFT)
        l12 = Tex(r'Alors, l''arbre  T, obtenu ä partir de T'' en remplaçant le noeud feuille associé à z par un noued interne ayant x et y comme enfants, représente un code optimal pour l''alphabet C').scale(0.5).next_to(l11, direction=DOWN, aligned_edge=LEFT)
        
        self.play(Write(l0))
        self.wait(1)
        self.play(Write(l1))
        self.wait(2)
        self.play(Write(l2),Write(l6))
        self.wait(2)
        self.play(Write(l3),Write(l4), Write(l5))
        self.wait(5)
        self.play(Write(l7),Write(l8), Write(l9))
        self.wait(2)
        self.play(Write(l10),Write(l11), Write(l12))
        self.wait(10)

class Complexite(Scene):
    def construct(self):
        
        ech = .5 # pour régler l'échelle
        l0 = Tex(r'Complexité').scale(2).move_to(np.array([-4,3.5 ,0]))
        l1 = Tex(r'L\' algorithme de Huffman est glouton').scale(1).next_to(l0, direction=DOWN, aligned_edge=LEFT)
        l2 = Tex(r'tout noeud construit est définitif').scale(0.7).next_to(l1, direction=DOWN, aligned_edge=LEFT)
        l3 = Tex(r'sous arbre - arbre optimal').scale(0.7).next_to(l2, direction=DOWN, aligned_edge=LEFT)
        l4 = Tex(r'Coûts pour un alphabet de k symboles ').scale(1).next_to(l3, direction=DOWN, aligned_edge=LEFT)
        l5 = Tex(r'k-1 itérations sur E').scale(0.7).next_to(l4, direction=DOWN, aligned_edge=LEFT)
        l6 = Tex(r'Coûts d\' intégration et d\' extraction sont en theta(log(k))').scale(0.7).next_to(l5, direction=DOWN, aligned_edge=LEFT)
        l7 = Tex(r'l\' algorithme est donc en theta(klog(k))').scale(1.0).next_to(l6, direction=DOWN, aligned_edge=LEFT)
        
        
        self.play(Write(l0))
        self.wait(1)
        self.play(Write(l1))
        self.wait(1)
        self.play(Write(l2),Write(l3))
        self.wait(3)  
        self.play(Write(l4))
        self.wait(1)
        self.play(Write(l5))
        self.wait(1)
        self.play(Write(l6))
        self.wait(3)
        self.play(Write(l7))
        self.wait(10)


##############################
#
# I M P L É M E N T A T I O N 
#
##############################

class Implementation(Scene):
    def construct(self):
        
        ech = .5 # pour régler l'échelle
        l0 = Tex(r'Implémentation').scale(2).move_to(np.array([-2,3.5 ,0]))
        l1 = Tex(r"(ici l'implémentation)").scale(ech).next_to(l0, direction=DOWN, aligned_edge=LEFT)
        l2 = Tex(r"(ne pas oublier l'évaluation de la performance)").scale(ech).next_to(l1, direction=DOWN, aligned_edge=LEFT)
                
        self.add(l0,l1,l2)
        self.wait(10)

##############################
#
# C R É D I T 
#
##############################

class Credit(Scene):
    def construct(self):
        
        ech = .5 # pour régler l'échelle
        l0 = Tex(r'Crédit').scale(1.2).move_to(np.array([-2,3.5 ,0]))
        l1 = Tex(r"Une vidéo réalisée à l'aide de Python et de la bibliothèque Manim").scale(ech).next_to(l0, direction=DOWN, aligned_edge=LEFT)
        l2 = Tex(r"Murièle Jacquier \& Simon Verdan  (GymInf 2021)").scale(ech).next_to(l1, direction=DOWN, aligned_edge=LEFT)
        
                
        self.add(l0,l1,l2)
        self.wait(10)

