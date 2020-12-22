#DZ 9.2: FizzBuzz

print("""Dobrodošlli u FizzBuzz igru! Pravila su jednostavna:

Navedite broj, a sustav će zatim brojati do toga broja.
Ako je broj djeljiv sa 3, sustav će ispisati \'fizz\' umjesto broja.
Ako je broj djeljiv sa 5, sustav će ispisati \'buzz\' umjesto broja.
A ako je broj djeljiv i sa 3 i sa 5, sustav će ispisati \'fizzbuzz\'.

Pokušajte!
""")

while True:

    x = int(input("Do kojeg broja želite da sustav broji? "))

    for x in range (1, x+1):
        if x % 5 == 0 and x % 3 == 0:
            print("fizzbuzz")
        elif x % 3 == 0:
            print("fizz")
        elif x % 5 == 0:
            print("buzz")

        else:
            print(x)

    print("Gotovo! Nadam se da Vam se sviđala igra!")

    pitanje = input("Želite li pokušati ponovo? (Da/Ne): ")

    if pitanje.lower() == "ne":
        print("Hvala na igranju i do skorog viđenja!")
        break