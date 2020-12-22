#DZ 9.3: Make string lowercase

print("""Dobrodošli! Upišite bilokoju riječ ili rečenicu, malim ili velikim slovima, a sustav će je izbaciti u malim slovima
Pokušajte!""")

while True:

    x = input("Vaš unos: ")

    print("U malim slovima Vaš je unos:")

    print(x.lower())

    ponovi = input("Želite li ponoviti radnju? (DA/NE): ")

    if ponovi.lower() != "da":
        print("Hvala na sudjelovanju i do skorog viđenja!")
        break

