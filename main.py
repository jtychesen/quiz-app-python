  
# Start bolding with \033[1m and reset it with \033[0m
print("\033[1mThis line of text will be bold inside VS Code terminal!\033[0m")
print("This line will be back to normal.")


print()
print("Quiz - Versjon 0.1")
print()
print("Her er en quiz!")
print("Prinsippet her er ikke at selve quizen er så spennende,")
print("- men at ting virker.")

print()
print("Etterhvert som nye versjoner kommer blir ting både mer lekkert -")
print("men da også mer avansert i utviklings delen fra min side..!")
print()
print()
print("Spørsmål 1:")
print("Hva er hovedstaten i Tyrkia? (Skriv A, B, C eller D)")
print("A) Istanbul")
print("B) Ankara")
print("C) Kairo")
print("D) Har ingen hovedstat")

answer = input("Your answer: ")

if answer.upper() == "B":
    print("Korrekt! Mange tror Istanbul her!")
else:
    print("Feil altså :( Er faktisk B) Ankara")