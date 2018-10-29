# Reverse enginerng Markov Chain
#

import re 
import random
from collections import defaultdict, deque




class Markov:

	def __init__(self, num_key_words=3): # < od razu w inicie ustala zmienna/ num_key_words to dlugosc sekcji slow, 
	#ogniwo lancucha np 3- pan tadeusz poszedl, np pan. mniejsza liczba wieksza randomizacja i chaos
    self.num_key_words = num_key_words
    
    

    self.lookup_dict = defaultdict(list) # < defaultdict, defaultdict(list) , tworzy slownik z okreslonym typem klucza- kazdy klucz bedzie lista / 
    #my_dictionary = {'key1' : [a,b,c], 'key2' : [g,b,d], 'key3' : [3,5,6]


     
    


    self._punctuation_regex = re.compile('[,.!;\?\:\-\[\]\n]+') # < zapisuje ktore symbole maja zostac usuniete z tekstu
    
    self._seeded = False # <- bool - domyslnie falsz
    self.__seed_me() # <- f uzywa funkcji




# sprawdza czy zostala wybrana opcja seeded, jesli tak przypisuje seed, jesli nie wyw


    def __seed_me(self, rand_seed=None): # <  ustanawia zmienna, nie okresla jednak typ ani wartosci
    
    if self._seeded is not True: # < bedzie non true, w inicie ustawiony na false przed wezwaniem funkcji
      try: 							# < try ?
        if rand_seed is not None: # < domyslnie nie zostanie aktywowane ( w wewnatrz funkcji okreslone na None)
          random.seed(rand_seed) # < otrzyma seed gdy fukcja zostanie uzyta, przypisze dany seed dla losowych czynnikow
        else:						# < domyslnie przeskoczy tutaj - 
          random.seed()				# < jesli nie dostanie sprecyzowanego seeda, wybierze losowy
        self._seeded = True 			# < zmieni zmienna z inita self.seeded na True
      except NotImplementedError: 	# < wywali error i ustawi zmienna do poczatkowej z inita jesli nie seeded nie bedzie true  przy odpaleniu funkcji
        self._seeded = False



    # uzywa funkcji add source data na tekscie z pliku
 	def add_file(self, file_path):
    

    	content = ''
    	with open(file_path, 'r') as fh:
      		self.__add_source_data(fh.read())

    

    # uzywa funkcji add source dta na podanym stringu
	def add_string(self, str):
    	
    	self.__add_source_data(str) # < uzycie wewnetrznej funkci klasy

  	


  	def __add_source_data(self, str):
    	
    	clean_str = self._punctuation_regex.sub(' ', str).lower() #< stosuje fukcje sub na zmiennej z inita, - czysci stringa ze znakow, unifikuje wielkosc liter
    	
    	tuples = self.__generate_tuple_keys(clean_str.split()) #< tworzy ZMIENNA tuple uzywajac funkcji na splitowanym, oczyszczonym stringu , ['Litwo,' 'ojczyzno', 'moja',]
    	

    	for t in tuples:      # < dla kazdego elementu w liscie ( nazwanej tuple)
      		
      		self.lookup_dict[t[0]].append(t[1]) # < dodaje element z indeksem 1 do elementu z indeksem 0  np. ' [ litwo ojczyzno moja  - klucz' dodaj wpis ' tys'

      lookup_dict = { 'litwo ojczyzno moja : 'tys') '





  	def __generate_tuple_keys(self, data): #< data- ['Litwo,' 'ojczyzno', 'moja',] - lista wytworzona w add_source_data
    	if len(data) < self.num_key_words: # sprawdza czy lista ma tyle slow co powinna - np 3 ( data < 2) - indeksy zaczynaja sie od 0, wiec <
      		return  # jesli wyczyszczony, splitowany do listy string jest mniejszy niz dlugosc ogniwa lancucha - zakoncz dzialanie funkcji

    for i in xrange(len(data) - self.num_key_words): # < dla kazdego elementu, dlugosc listy ( ilosc slow) - dlugosc pojedynczego ogniwa w lancuchu
      
      yield [ tuple(data[i:i+self.num_key_words]), data[i+self.num_key_words] ] # < ~ tworzy generator object



data:

['Litwo,' 'ojczyzno', 'moja', 'tys', 'jest', 'jak', 'zdrowie' 'tyle']

    0          1       2       3       4       5       6        7


    yield [x, y] - lista 

    tuple (lista data (od obecnego do 3+ - tworzy ogniwo z 3 slow))


x:


    i0  ['Litwo ojczyzno moja' ,'tys']
    i1  


    ('ojczyzno moja tys ')
    i2  ('moja tys jest')
    i3  ('tys jest jak')
    i4  (' jest jak zdrowie')
    i5  ('jak zdrowie tyle')


y:

    i0  ('tys')
    i1  ('jest')
    i2  ('jak')
    i3  ('zdrowie')
    i4  ('tyle')


def generate_text(self, max_length=20): #< funkcja wzywana zewnetrznie, max lenght dlugosc tekstu do wygenerowania 
    
    context = deque() #< tworzy deck - zoptymalizowana lista oparta o first in first out, mozna dodawac i usuwac z obu stron
    
    output = [] #< tworzy pusta liste -zwraca text w postaci listy
    
   
    if len(self.lookup_dict) > 0: #< jesli zostal dodany jakis tekst ..
      
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