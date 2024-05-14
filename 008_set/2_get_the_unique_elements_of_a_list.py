'''
Digamos que tienes una lista de restaurantes; tal vez la leas de un archivo. Te importan los restaurantes únicos en
la lista. La mejor manera de obtener los elementos únicos de una lista es convertirla en un conjunto.
'''
from enum import Enum


def function_get_the_unique_elements_of_a_list():
    restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
    unique_restaurants = set(restaurants)
    print(unique_restaurants)

    '''
    Tenga en cuenta que el conjunto no está en el mismo orden que la lista original; eso se debe a que los conjuntos 
    están desordenados, al igual que los dict s. Esto se puede transformar fácilmente nuevamente en una Lista 
    con la función de lista incorporada de Python, dando otra lista que es la Misma lista que el 
    original pero sin duplicados:
    '''

    print(  list(unique_restaurants)        )

    # También es común ver esto como una sola línea:
    print(  list(set(restaurants))      )

    # Now any operations that could be performed on the original list can be done again.

    







    # Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("Este código se ejecuta solo si el script se ejecuta directamente.")
    function_get_the_unique_elements_of_a_list()