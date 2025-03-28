from main import trivia_fetch

# Test 1
def test_trivia_42():
    assert trivia_fetch(42)["number"] == 42
    assert trivia_fetch(42)["trivia"] == "El número 42 es conocido como la respuesta a la vida, el universo y todo lo demás, según 'La guía del autoestopista galáctico' de Douglas Adams."

# Test 2
def test_trivia_1000():
    assert trivia_fetch(1000)["number"] == 1000
    assert trivia_fetch(1000)["trivia"] == "El número mil es el primer número que tiene cuatro dígitos y es un hito en la numeración."

# Ejecutar las pruebas
if __name__ == "__main__":
    test_trivia_42()
    test_trivia_1000()
    print("Todas las pruebas pasaron.")



if __name__ == "__main__":
    test_trivia_42()
    test_trivia_1000()
print("Todas las pruebas pasaron.")

