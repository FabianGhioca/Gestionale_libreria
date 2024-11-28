lista_libri = ["libro1", "libro3", "libro5"]
libri_prestito = ["libro2", "libro4"]
from Libro import AggiuntaLibro, PrestitoLibro , RiportaLibro, DisponibilitaLibro, LibriLibreria, LibriPrestito


funzione = 0

while funzione <= 6:
    print("1 - Aggiunta libro")
    print("2 - Prestito libro")
    print("3 - Riporta libro")
    print("4 - Disponibilità libro")
    print("5 - Libri disponibili nella libreria")
    print("6 - libri dati in prestito")
    print("7 - Esci dal programma")
    funzione = int(input("Inserisci il numero della funzione desiderata: "))

    if funzione == 1:                                          # Aggiunta libro
        libro_aggiunta = input("Inserisci il titolo del nuovo libro: ")
        AggiuntaLibro(libro_aggiunta, lista_libri)

    elif funzione == 2:                                        # Prestito libro
        for item in lista_libri:
            print(item)
        prestito = input("Seleziona il libro che vuoi prendere in prestito: ")
        PrestitoLibro(prestito, lista_libri, libri_prestito)
    
    elif funzione == 3:                                        # Riporta libro
        for item in libri_prestito:
            print(item)
        libro_riportato = input("Inserisci il libro riportato: ")
        RiportaLibro(libro_riportato, lista_libri, libri_prestito)
        
    elif funzione == 4:                                        # Disponibilita libro
        titolo = input("Inserisci il titolo che vuoi cercare: ")
        DisponibilitaLibro(titolo, lista_libri)

    elif funzione == 5:                                        # Libri disponibili nella libreria
        LibriLibreria(lista_libri)

    elif funzione == 6:                                        # Libri dati in prestito
        LibriPrestito(libri_prestito)

    else:                                                      # Fine programma
        print("Hai chiuso il programma")
        break