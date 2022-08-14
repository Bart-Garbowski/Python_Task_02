TOTAL_PACKAGE_WEIGHT = 20 # maksymalna waga paczki
elements_total_weight = 0 # waga wszystkich elementów
initial_package_weight = 0 # poczatkowa waga paczki
packages_number = 0 # ilosc paczek wyslanych
total_empty_weight = 0

package_num_empty = 0 # numer paczki z pustymi kg
package_weight_empty = 0 # ilosc pustych kilogramow

number_of_elements = input("Liczba elementów do wysłania: ")
number_of_elements = int(number_of_elements)

for element_number in range(1, number_of_elements + 1):
    print(f"## Element numer {element_number} ##")

    element_weight = input(f"Waga elementu numer {element_number}[kg]: ")
    element_weight = int(element_weight)

    if element_weight == 0:
        print("KONIEC PROGRAMU!")
        break

    if element_weight > 10 or element_weight < 1:
        print(f"Waga {element_weight} kg poza zakresem!")
        packages_number += 1
        if (TOTAL_PACKAGE_WEIGHT - element_weight) >= package_weight_empty:
                # print(f"{element_weight=}")
                # print(f"{package_weight_empty=}")
                # print(f"{last_element_weight=}")
                package_num_empty = packages_number
                package_weight_empty = TOTAL_PACKAGE_WEIGHT - last_element_weight
        break

    initial_package_weight += element_weight

    if initial_package_weight == TOTAL_PACKAGE_WEIGHT:
        packages_number += 1
        initial_package_weight = 0
    if initial_package_weight > TOTAL_PACKAGE_WEIGHT:
        packages_number += 1
        initial_package_weight = element_weight

        package_num_empty = packages_number
        package_weight_empty = TOTAL_PACKAGE_WEIGHT - element_weight

    elements_total_weight += element_weight

    if element_number == number_of_elements:
        if element_weight > 0:
            packages_number += 1

            if (TOTAL_PACKAGE_WEIGHT - element_weight) >= package_weight_empty:
                package_num_empty = packages_number
                package_weight_empty = TOTAL_PACKAGE_WEIGHT - element_weight

    last_element_weight = elements_total_weight

total_empty_weight = (packages_number * TOTAL_PACKAGE_WEIGHT) - elements_total_weight

print("#### PODSUMOWANIE ####")
print(f"Suma kilogramów wysłanych: {elements_total_weight}")
print(f"Liczba wysłanych paczek: {packages_number}")
print(f"Suma pustych kilogramów: {total_empty_weight}")

print(f"Paczka numer {package_num_empty} z najwieksza liczba pustych kg: {package_weight_empty}")
