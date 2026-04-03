"""Poprawka zadań z poprzednich lekcji."""

for i in range(4):
    for j in range(2):
        print("**" * (i + 1))



CHEESE_1 = "roquefort"
PRICE_1 = 12.50
AMOUNT_1 = 2

CHEESE_2 = "stilton"
PRICE_2 = 11.24
AMOUNT_2 = 1

CHEESE_3 = "brie"
PRICE_3 = 9.30
AMOUNT_3 = 1

CHEESE_4 = "gouda"
PRICE_4 = 8.55
AMOUNT_4 = 1

CHEESE_5 = "edam"
PRICE_5 = 11.00
AMOUNT_5 = 1

CHEESE_6 = "parmezan"
PRICE_6 = 16.50
AMOUNT_6 = 3.5

CHEESE_7 = "mozzarella"
PRICE_7 = 14.00
AMOUNT_7 = 1.3

CHEESE_8 = "czechosłowacki ser z owczego mleka"
PRICE_8 = 122.32
AMOUNT_8 = 2.2

LISTEK_MIETOWY = "listki mięty"
PRICE_MIETOWY = 20.00
AMOUNT_MIETOWY = 0.2

LIST_OF_CHEESES = (
    f"Raport z zakupów:\n"
    f".................................\n"
    f"{CHEESE_1}, {AMOUNT_1} kg, {PRICE_1:.2f} zł/kg,\n"
    f"{CHEESE_2}, {AMOUNT_2} kg, {PRICE_2:.2f} zł/kg,\n"
    f"{CHEESE_3}, {AMOUNT_3} kg, {PRICE_3:.2f} zł/kg,\n"
    f"{CHEESE_4}, {AMOUNT_4} kg, {PRICE_4:.2f} zł/kg,\n"
    f"{CHEESE_5}, {AMOUNT_5} kg, {PRICE_5:.2f} zł/kg,\n"
    f"{CHEESE_6}, {AMOUNT_6} kg, {PRICE_6:.2f} zł/kg,\n"
    f"{CHEESE_7}, {AMOUNT_7} kg, {PRICE_7:.2f} zł/kg,\n"
    f"{CHEESE_8}, {AMOUNT_8} kg, {PRICE_8:.2f} zł/kg,\n"
    f"{LISTEK_MIETOWY}, {AMOUNT_MIETOWY} kg, {PRICE_MIETOWY:.2f} zł.\n"
    f".................................\n"
    f"Suma zł: {
        (AMOUNT_1 * PRICE_1)
        + (AMOUNT_2 * PRICE_2)
        + (AMOUNT_3 * PRICE_3)
        + (AMOUNT_4 * PRICE_4)
        + (AMOUNT_5 * PRICE_5)
        + (AMOUNT_6 * PRICE_6)
        + (AMOUNT_7 * PRICE_7)
        + (AMOUNT_8 * PRICE_8)
        + (PRICE_MIETOWY):.2f}"
)


print(LIST_OF_CHEESES)
