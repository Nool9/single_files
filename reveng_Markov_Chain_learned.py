# Markov Chain


# Paczka regex, manipulacja stringami

import re 

# Paczka random, losowosc

import random



# RE



# re.compile tworzy klucz sre (specjalny obiekt) - pattern w stringu, np slowo, symbole. Do wykorzystania w funkcjach z re

example = re.compile('kurwa')

# funkcja dla obiektu sre - zastepuje zdefiniowany w re.compile pattern podanym stringiem (lub innymp patternem). 

example.sub('*****', string)



# RANDOM



# tworzy randomowy seed dla funkcji z modulu random

random.seed()


# tworzy seed o danym kluczu. predefiniuje lososc - np. uzycie tego samego seedu w innym programie da te same 'losowe' liczby

random.seed(36472)

# losuje liczbe z przedzialu

randint(0,10)




# EXCEPTIONS



# (try) sprobuj tego- jesli spotka error, nie wywali programu tylko przejdzie do except

try:

	something		

except:

	something else



# NONE



# tworzy zmianna i nie przypisuje wartosci ani typu zmiennej

variable = None


#SPLIT

string1 = 'dont go gently into that dark night'
list_from_string1 = string1.split()





1. init 

	- ile slow bedzie mial czlon? co bedzie ogniwoem
	- jak potraktowac losowosc? dac uzytkownikowi mozliwosc wpisania seeda, jesli nie wybierze wybrac za niego
	- z jakich zrodel bedzie korzystac program? co jest inputem? jak bedzie nalezalo go przetworzyc? jak bedzie wygladal output?

2. input
	
	- funkcje pobierajace dane, string lub plik tekstowy
	- funkcja przetwarzajaca input

3. finalne przetworzenie tekstu i wygenerowanie nowego tekstu

	- PRZETWORZENIE :

	1. Stworz pusty slownik skladajacy sie z list, okreslenie dlugosc ogniwa lancucha ( na czym bedziemy operowac? jaka przestrzen bedzie najlepsza do przetworzenia tego?)
	2. Pobierz tekst ze zrodla i go przygotuj - wyczysc za pomoca funkcji z re i otrzymaj czysty tekst w formie stringa
	3. Stworz ogniwa lancucha :


	Rozbij wyczyszczonego stringa na liste

	['slowo1', 'slowo2', 'slowo3']

	Stworz trzy slowowe ogniwo dla kazdego slowa w lancuchu ( dlugosc - jedna dlugosc lancucha, zostanie zapewniony pozniej), 
	dolacz do pustego slownika z wartoscia rowna nastepnemu slowu po tej sekwencji

	{('slowo1' ,'slowo2' ,'slowo3') : [slowo4]}

	Uzywajac deque i zmiennej context, dodawaj do zmiennej output 

	f len(self.lookup_dict) > 0: #< jesli zostal dodany jakis tekst ..
      
      self.__seed_me(rand_seed=len(self.lookup_dict)) # < wykorzystuje dlugosc slownika jako randomowy seed dla funkcji seed_me

      idx = random.randint(0, len(self.lookup_dict)-1) # < losuje liczbe z przedzialu 0 do dlugosc slownika ( ilosc 3 slowowych ogniw)
      chain_head = list(self.lookup_dict.keys()[idx]) # tworzy liste o jednym argumencie - funkcja .keys()wywoluje wszystkie klucze ( ogniwa), idx wybiera jedno z nich ( indeks klucza z listy)
      context.extend(chain_head) #< dodaje pierwsze ogniwo do deku

      while len(output) < (max_length - self.num_key_words): # < dodawaj elementy do listy output dopoki nie osiagniemy max_lenght ( -3 , pierwsze ogniwo juz jest)
        next_choices = self.lookup_dict[tuple(context)] # < tworzy zmienna przechowujaca nastepna pozycje dla slownika, zamienia klucze z deku na tuple
        if len(next_choices) > 0:
          next_word = random.choice(next_choices) # < wybiera randomowe slowo z listy
          context.append(next_word) # M dodaje slowo d listy next choices
          output.append(context.popleft()) # dodaje slowo do listy output, wyrzuca poprzednie z deku context
        else:
          break
      output.extend(list(context))
    return output


# DEQUE & DEFAULTDICT

from collections import defaultdict, deque


# tworzy pusty slownik skladajacy sie z list ( lub innego typu danych)

my_dictionary = defaultdict(list)

# deque - typ listy ktory mozna dynamicznie zmieniac- dokladac cos z lewej lub prawej, okreslic maksymalna dlugosc ( po dodaniu nastepnego elementu pierwszy odpada)
# zasada fifo - first in first out


context = deque() # tworzy obiekt
context.extend(chain_head) # dodaje element/y
output.append(context.popleft()) # dodaje elementy, pop, popleft wyrzuca skrajny element i zwraca jego wartosc




# TUPLES

# podobne do listy ale nie zmienne, zapisywane z () zamiast []

a = (a,b,c)


# YIELD

# generator, wykorzystywany przy iterowaniu przez elementy - znacznie wydajniejszy od append - nie trzyma w pamieci wszystkich danych, tylko iteruje po jednym elemencie


for x in z:

	yield [ tuple(data[i:i+self.num_key_words]), data[i+self.num_key_words] ]