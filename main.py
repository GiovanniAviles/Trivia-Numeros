def trivia_fetch(num):
    # Diccionario con trivia sobre algunos números
    trivia_dict = {
        1: "El número uno es el primer número natural.",
        2: "El número dos es el único número par que es primo.",
        3: "El número tres es el primer número impar.",
        4: "El número cuatro es el primer número compuesto.",
        5: "El número cinco es el primer número que es la suma de dos números primos (2 + 3).",
        10: "El número diez es la base del sistema decimal.",
        7: "El número siete es considerado un número de la suerte en muchas culturas.",
        13: "El número trece es a menudo considerado un número de mala suerte.",
        21: "El número veintiuno es el número de puntos necesarios para ganar en el blackjack.",
        42: "El número 42 es conocido como la respuesta a la vida, el universo y todo lo demás.",
        100: "El número cien es el primer número que tiene tres dígitos.",
        1000: "El número mil es el primer número que tiene cuatro dígitos y es un hito en la numeración."
    }
    
    trivia = trivia_dict.get(num, "No hay trivia disponible para este número.")
    
    return {"number": num, "trivia": trivia}

def main():
  print("¡Bienvenido a la Trivia Quizz!")

  while True:
        try:
            num = int(input("Introduce un número para obtener trivia (o -1 para salir): "))
            if num == -1:
                print("¡Gracias por jugar!")
                break
            
            trivia = trivia_fetch(num)
            print(trivia)
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__=="__main__":
  main()