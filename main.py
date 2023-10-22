# Ignorare le righe fino alla 31
from os import terminal_size
from typing import Any, Callable, DefaultDict, List, OrderedDict
import string

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Esegue un test e controlla il risultato
def check_test(func: Callable, expected: Any, *args: List[Any]):
    func_str = func.__name__
    args_str = ', '.join(repr(arg) for arg in args)
    try:
        result = func(*args)
        result_str = repr(result)
        expected_str = repr(expected)
        test_outcome = "succeeded" if (result==expected) else "failed"
        color = bcolors.OKGREEN if (result==expected) else bcolors.FAIL
        print(f'{color}Test on {func_str} on input {args_str} {test_outcome}. Output: {result_str} Expected: {expected_str}')
    except BaseException as error:
        error_str = repr(error)
        print(f'{bcolors.FAIL}ERROR: {func_str}({args_str}) => {error_str}')

# Scrivere una funzione che controlla la validita' di una password.
# La password deve avere:
# - Almeno una lettera fra [a-z] e una lettera fra [A-Z]
# - Almeno un numero fra [0-9]
# - Almeno un carattere fra [$#@]
# - Essere lunga almeno 6 caratteri
# - Essere lunga non piu' di 16 caratteri
# - La password non è valida se contiene caratteri diversi da quelli specificati sopra
#   o se viola una delle regole specificate.
# La funzione restituisce true/false a seconda se la password sia valida o meno.
def check_pwd(pwd: str) -> bool:
    if len(pwd) < 6 or len(pwd) > 16:
        return False

    # Carichiamo i nostri caratteri
    lower_case_ascii = string.ascii_lowercase
    upper_case_ascii = string.ascii_uppercase
    digits = string.digits
    special_chars = "$#@"
    
    upper_char = False
    lower_char = False
    digit_char = False
    special_char = False

    # Soluzione adatta alle strutture che ci sono state fornite finora 
    for char in pwd:
        # Controlliamo se siamo già certi che una password sia corretta   
        if char in lower_case_ascii:
            lower_char = True
        elif char in upper_case_ascii:
            upper_char = True
        elif char in digits:
            digit_char = True
        elif char in special_chars:
            special_char = True      
        else:
            return False
    
    if lower_char and upper_char and digit_char and special_char:
        return True
    else:
        return False


# Scrivere una funzione che data una tupla (x, y, z)
# restituisca la tupla (z+1, x-1, y+2)
def tuple_ex(t: tuple) -> tuple:
    return t[2]+1, t[0]-1, t[1]+2

# Scrivere una funzione che calcola l'intersezione fra due liste.
# Date due liste, deve restituire una nuova lista contenente solo gli
# elementi presenti in entrambe le liste.
def intersect(a: list, b: list) -> list:
    # Qui abbiamo due soluzioni
    # Una elegante e una brutta
    
    # La soluzione elegante sarebbe convertire
    # a e b in insiemi e utilizzare le funzioni built-in di Python per fare l'intersezione
    # return list(set(a) & set(b))

    # Soluzione Tamarra
    output = []
    for char in a:
        if char in b:
            output.append(char)
    return output

# Scrivere una funzione che data una lista contenente valori >= 0, 
# crei una nuova lista contentente soltanto gli elementi della lista 
# originale tali che soddisfano la seguente proprietà:
#    lista[i] > 2*media(lista[0:i])
# (Il primo elemento non viene quindi mai inserito)
# Ad esempio, si consideri la lista [5, 3, 10, 0]
#  Il primo elemento è 5. Non viene inserito
#  Il secondo elemento è 3, e la media degli elementi nel range [0, 0] è 5. Poichè 3 < 5*2, l'elemento non viene inserito nella nuova lista
#  Il terzo elemento è 10, e la media degli elementi nel range [0, 1] è 4. Poichè 10 > 4*2, l'elemento viene inserito nella nuova lista
#  Il quarto elemento è 0, e la media degli elementi nel range [0, 2] è 6. Poichè 0 < 6*2, l'elemento non viene inserito nella nuova lista
def remove_avg(a: list) -> list:
    risultato = []

    # Calcoliamo dinamicamente la media degli elementi
    for i in range(1, len(a)):
        # Calcolo della media dall'inizio fino all'indice i-esimo
        media = sum(a[:i]) / i

        # Verifichiamo se l'elemento è maggiore della media attuale
        if a[i] >= media:
            risultato.append(a[i])

    return risultato

# Data una lista di interi (ciascun intero è compreso fra 0 e 99), scrivere una
# funzione che restituisca una lista di tuple (x, y),
# dove x è un intero, e y è il numero di volte che questo
# intero appare nella lista originale.
# La lista di tuple deve essere ordinata in base al primo elemento.
# Ad esempio, per l'input [5, 4, 1, 4], restituisce la lista [(1, 1), (4, 2), (5, 1)]
# (ordinata in base al primo elemento perché 1 < 4 < 5)
def frequency(a: list) -> list:
    # Creiamo dinamicamente liste delle dimensioni appropriate per ospitare l'elemento massimo
    output = [0] * (max(a) + 1)
    frequency = [0] * (max(a) + 1)

    # Iteriamo sulla lista
    for index in a:
        # Abbiamo una lista i cui indici sono la frequenza con cui abbiamo trovato un elemento
        frequency[index] += 1
        # Esempio input: 3 2 3
        # La frequenza avrà questa struttura
        # [0: 0, 1: 0, 2: 1, 3: 2]

        # Abbiamo quindi un'altra lista,
        # dove all'indice del numero corrente
        # memorizziamo in una tupla, il valore corrente e la sua frequenza
        output[index] = (index, frequency[index])

    # Filtriamo gli elementi non tuple dalla lista di output
    output = [item for item in output if isinstance(item, tuple)]

    return output




# Scrivere una funzione che restituisce True
# se la lista è palindroma, o False altrimenti
def is_palindrome(a: list) -> bool:

    # Verifica se la lunghezza della lista è dispari o pari
    # Facciamo l'operazione AND con il primo bit del numero
    if len(a) & 0x1:
        first_half = a[:len(a)//2 + 1]  
        second_half = a[len(a)//2:]    
    else:
        first_half = a[:len(a)//2]      
        second_half = a[len(a)//2:]    

    # Confronta la prima metà con la seconda metà invertita
    if first_half == second_half[::-1]:
        return True  
    return False     
    

# Scrivere una funzione che prende in input una lista, e 
# restituisce True se la lista è ordinata in ordine
# crescente o decrescente, e False altrimenti.
# Suggerimento: fare attenzione ai valori duplicati
# Utilizzare un solo ciclo e non utilizzare sorted/sort.
def is_sorted(a: list) -> bool:
    # Gestione dei casi speciali:
    if len(a) == 1:
        return True

    # Risoluzione
    reverse = None 
    # La prima cosa da determinare è se l'array è ordinato in modo crescente/decrescente 
    # Affrontiamo questo problema restituendo False se il valore previsto non è presente
    # Poiché il problema non lo specifica, supponiamo che per ogni n possa non esistere un elemento n+1
    # Es. [1,3,100,10000] è effettivamente ordinato :)

    lenght = len(a) - 1

    for index in range(lenght):
        # Verifichiamo se è necessario controllare il valore, o possiamo skippare un'iterazione.
        if a[index] == a[index + 1]:
            continue

        # Supponiamo che l'ordine predefinito non sia invertito
        if reverse is None:
            if a[index] > a[index + 1]:
                reverse = True
            else:
                reverse = False

        if not reverse:
            # se l'ordine non è invertito e il nostro valore è maggiore del successivo
            # c'è qualcosa che non va
            if a[index] > a[index + 1]:
                return False
        else:
            # se l'ordine è invertito e il nostro valore è minore del successivo
            # c'è qualcosa che non va
            if a[index] < a[index + 1]:
                return False

    # Se siamo arrivati fino a qui, l'array è ordinato correttamente
    return True




# Scrivere una funzione che restituisce True se una lista di interi
# è composta da una prima parte ordinata in modo crescente, seguita
# da una seconda parte ordinata in modo decrescente (o viceversa).
# Le due parti non devono avere necessariamente la stessa lunghezza.
# Utilizzare un solo ciclo e non utilizzare sorted/sort, ne la funzione
# is_sorted implementata precedentemente.
# Si assuma che la lista abbia almeno sempre 3 elementi.
def is_sorted_half(a: list) -> bool:
    # Dato che siamo certi che la lista contiene almeno 3 elementi,
    # possiamo effettuare un controllo diretto sui primi 2 elementi e decidere se la lista inizia in ordine crescente o decrescente.
    increasing = bool 

    if a[0] < a[1]: 
        increasing = True
    else: 
        increasing = False

    # Utilizziamo un'altra variabile per assicurarci che la lista poi decresca/cresca.
    order_changed = False
    lenght = len(a) -1
    for index in range(0, lenght):
        if not order_changed:
            # Caso 1
            # Ci aspettiamo che il valore sia crescente,
            # ma incontriamo un valore successivo che è inferiore a quello su cui stiamo iterando.
            if increasing and (a[index] > a[index+1]):
                order_changed = True

            # Ci aspettiamo che il valore sia decrescente,
            # ma incontriamo un valore è superiore a quello su cui stiamo iterando.
            elif not increasing and (a[index] < a[index+1]):
                order_changed = True
        # Abbiamo già cambiato l'ordine in precedenza.
        else:
            # Ci aspettavamo che il valore sia decrescente,
            # ma scopriamo che la lista è invece crescente.
            # Notare che da crescente abbiamo cambiato ordine.
            if increasing and (a[index] < a[index+1]):
                return False
            # Ci aspettavamo che il valore sia crescente,
            # ma scopriamo che la lista è invece decrescente.
            elif not increasing and (a[index] > a[index +1]):
                return False

    # Se l'ordine non è stato cambiato, allora dobbiamo ritornare False
    if not order_changed:
        return False
    # In tutti gli altri casi, se non abbiamo incontrato anomalie ritorniamo True
    return True 

            




# Test funzioni
check_test(check_pwd, False, "a")
check_test(check_pwd, False, "000000000000000000")
check_test(check_pwd, False, "almeno6")
check_test(check_pwd, False, "Aa@09asng2/")
check_test(check_pwd, True, "Aa@09asng2")
check_test(tuple_ex, (3, -2, 1), (-1, -1, 2))
check_test(intersect, [2, 3], [1, 2, 3], [2, 3, 4])
check_test(intersect, [], [1, 2, 3], [10, 11, 12])
check_test(intersect, [], [1, 2, 3], [])
check_test(intersect, [], [], [1, 2, 3])
check_test(remove_avg, [10], [5, 3, 10, 0])
check_test(remove_avg, [20, 1000], [5, 20, 10, 1000])
check_test(remove_avg, [], [])
check_test(frequency, [(1, 1), (4, 2), (5, 1)], [5, 4, 1, 4])
check_test(frequency, [(0, 1), (23, 3), (99, 1)], [23, 99, 0, 23, 23])
check_test(is_palindrome, True, [])
check_test(is_palindrome, True, [1])
check_test(is_palindrome, True, [1, 2, 8, 2, 1])
check_test(is_palindrome, True, [1, 2, 8, 8, 2, 1])
check_test(is_palindrome, False, [1, 3, 8, 8, 2, 1])
check_test(is_sorted, True, [1])
check_test(is_sorted, True, [1, 1, 1])
check_test(is_sorted, True, [1, 2, 3, 4])
check_test(is_sorted, True, [4, 3, 2, 1])
check_test(is_sorted, True, [1, 1, 2, 3, 3, 4])
check_test(is_sorted, True, [4, 4, 3, 2, 2, 1])
check_test(is_sorted, False, [1, 1, 3, 3, 2])
check_test(is_sorted, False, [4, 4, 3, 3, 5])
check_test(is_sorted_half, False, [1, 2, 3])
check_test(is_sorted_half, False, [3, 2, 1])
check_test(is_sorted_half, True, [1, 3, 2])
check_test(is_sorted_half, True, [3, 1, 2])
check_test(is_sorted_half, True, [1, 2, 5, 6, 8, 9, 3])
check_test(is_sorted_half, True, [1, 2, 5, 6, 8, 9, 3][::-1]) # Custom Test Case
check_test(is_sorted_half, False, [1, 2, 5, 6, 8, 9, 3, 4]) # Custom Test Case
