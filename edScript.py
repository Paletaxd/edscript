# Script hecho para el aprendizaje básico de la programación en Python.
# Lo propuesto en este código está basado en el conocimiento principal del desarrollador de éste.
# Código principalmente hecho para la ayuda del aprendizaje de este lenguaje para los estudiantes del Colegio de las Américas de grado 9°.
# Codificado por el estudiante de grado 10°: Andrés Felipe Rodríguez Arias.
# A lo largo del código pueden aparecer comentarios como éste para explicar qué significa cada operador.

def main():                                                 # Aquí se está definiendo la función principal o "main" del código.
    input("\n¡Hola! Este es un script hecho en Python3 con el fin del aprendizaje básico del lenguaje Python.");
    input("\nPara comenzar con este tema, quisiera saber si tiene algún conocimiento previo acerca de lo que es este lenguaje.");

    userKnowledgement = '0'                                   # El conocimiento del usuario debe ser 0 para iniciar con el aprendizaje, este valor es asignado a la variable que se puede ver.
    found = False

    while not found:                                        # Mientras el conocimiento ingresado siga siendo opuesto al necesario, se repetirá la petición de ingresar.
        userInput = input("\n¿Conoce usted algo sobre programación en Python? (0 = No, 1 = Sí): ")

        if userInput == userKnowledgement:
            print("\n¡Ok! Vamos a comenzar.")
            found = True
        elif str(userInput) > str(userKnowledgement):
            input("\n0 = No, 1 = Sí: ")

def sBeg():
      print('''\n                       _ _ _ _ _ _   _ _        _ _   _ _ _ _ _ _ _ _ _    _ _ _       _ _ _    _ _ _ _ _ _ _ _ _    _ _       _ _ 
                      |    _ _    \  \   \     /   / |                 |  |     |     |     |  |                 |  |    \    |   |
                      |   |   |    |  \   \   /   /  |_ _ _       _ _ _|  |     |     |     |  |      _ _ _      |  |     \   |   |
                      |   |_ _|    |   \   \_/   /         |     |        |     |     |     |  |     |     |     |  |      \  |   |
                      |            |    \       /          |     |        |     |_ _ _|     |  |     |     |     |  |       \ |   |
                      |      _ _ _/      |     |           |     |        |                 |  |     |     |     |  |        \|   |
                      |     /            |     |           |     |        |      _ _ _      |  |     |     |     |  |    |\       |
                      |    |             |     |           |     |        |     |     |     |  |     |     |     |  |    | \      |
                      |    |             |     |           |     |        |     |     |     |  |     |_ _ _|     |  |    |  \     |
                      |    |             |     |           |     |        |     |     |     |  |                 |  |    |   \    |
                      |    |             |     |           |     |        |     |     |     |  |                 |  |    |    \   |
                      |_ _ |             |_ _ _|           |_ _ _|        |_ _ _|     |_ _ _|  |_ _ _ _ _ _ _ _ _|  |_ _ |     \ _|
        \n                                                    / / / Codificado por Andrés Rodríguez :) \ \ \                                             ''')




if __name__ == '__main__':
    main()
    sBeg()
