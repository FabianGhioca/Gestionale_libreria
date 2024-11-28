def AggiuntaLibro(libro_aggiunta, lista_libri):                     # 1

    lista_libri.insert(0, libro_aggiunta)
    print("Hai aggiunto questo libro: " +libro_aggiunta)
    print("Ecco la lista aggiornata:")
    for item in lista_libri:
        print(item)


def PrestitoLibro(prestito, lista_libri, libri_prestito):           # 2
    
    lista_libri.remove(prestito)
    libri_prestito.insert(0, prestito)
    print("Hai preso in prestito questo libro: " +prestito)


def RiportaLibro(libro_riportato, lista_libri, libri_prestito):     # 3
    libri_prestito.remove(libro_riportato)
    lista_libri.insert(0, libro_riportato)
    print("Hai riporato questo libro: " +libro_riportato)


def DisponibilitaLibro(titolo, lista_libri):                                # 4
    if titolo in lista_libri:
        print("il libro è disponibile")
    else:
        print("il titolo non è disponibile")


def LibriLibreria(lista_libri):                                  # 5
    for item in lista_libri:
        print(item)


def LibriPrestito(libri_prestito):                                  # 6
    for item in libri_prestito:
        print(item)