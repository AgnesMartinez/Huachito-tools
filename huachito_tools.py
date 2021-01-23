import random
import re
import math as white

def slots():
    """Ahora si es todo un casino"""

    emojis = ['👻','🐷','🐧','🦝','🍮', '💣','👾','👽','🦖','🥓','🤖']

    huachito = [random.choice(emojis) for i in range(5)]

    conteo = [huachito.count(emoji) for emoji in emojis if huachito.count(emoji) != 0 and emoji != '🥓']

    if '🥓' in huachito:
        maximo = max(conteo)

        tocinos = huachito.count('🥓')

        conteo.append(maximo + tocinos)

    if huachito.count('💣') > 1:
        #Enviar mensaje de perdida en caso de 2 bombas
        respuestas_bomba = ["Como en buscaminas, te explotaron las bombas, perdiste!","2 bombas werito, perdiste","DOBLE BOMBA! mala suerte :'(","Te salio el negrito y el prietito del arroz, perdistes."]

        return f"{random.choice(respuestas_bomba)}"
                
    else:
        #Dar dinero en caso de 2 pares iguales
        if conteo.count(2) == 2:

            if '💣' in huachito:
                cantidad = 5
            else:
                cantidad = 10

            return f"Ganaste {cantidad} huachis (2 pares iguales)"
                
        elif conteo.count(2) == 3:

            cantidad = 100

            return f"Ganaste {cantidad} huachis (3 pares iguales)"
                
        else:

            for numero in sorted(conteo,reverse=True):
                #Entregar premios

                if numero == 3:
                  
                    if huachito.count('👻') == 3:
                        cantidad = 300
                            
                    elif huachito.count('🐷') == 3:
                        cantidad = 70

                    elif huachito.count('🍮') == 3:
                        cantidad = 80

                    elif huachito.count('🦝') == 3:
                        cantidad = 150

                    elif huachito.count('👾') == 3:
                        cantidad = 90

                    elif huachito.count('👽') == 3:
                        cantidad = 100

                    elif huachito.count('🦖') == 3:
                        cantidad = 200

                    elif huachito.count('🐧') == 3:
                        cantidad = 60

                    elif huachito.count('🤖') == 3:
                        cantidad = 50

                    else:
                        cantidad = 30
                            
                    if '💣' in huachito:
                        cantidad = round(cantidad / 2)

                    if '🥓' in huachito:

                        return f"#Rasca y gana con Huachito - Loteria Mujicana\n\n>!{' '.join(huachito)}!<\n\n>!Ganaste {cantidad:,} huachis (3 iguales usando comodin 🥓)!<"
                    
                    else:

                        return f"#Rasca y gana con Huachito - Loteria Mujicana\n\n>!{' '.join(huachito)}!<\n\n>!Ganaste {cantidad:,} huachis (3 iguales)!<"


                elif numero == 4:

                
                    if huachito.count('👻') == 4:
                        cantidad = 4000
                            
                    elif huachito.count('🐷') == 4:
                        cantidad = 800

                    elif huachito.count('🍮') == 4:
                        cantidad = 900

                    elif huachito.count('🦝') == 4:
                        cantidad = 2000

                    elif huachito.count('👾') == 4:
                        cantidad = 1000

                    elif huachito.count('👽') == 4:
                        cantidad = 1500

                    elif huachito.count('🦖') == 4:
                        cantidad = 3000

                    elif huachito.count('🐧') == 4:
                        cantidad = 700

                    elif huachito.count('🤖') == 4:
                        cantidad = 600

                    else:
                        cantidad = 500
                            
                    if '💣' in huachito:
                        cantidad = round(cantidad / 2)

                    if '🥓' in huachito:

                           return f"#Rasca y gana con Huachito - Loteria Mujicana\n\n>!{' '.join(huachito)}!<\n\n>!Ganaste {cantidad:,} huachis (4 iguales usando comodin 🥓)!<"
                    
                    else:

                            return f"#Rasca y gana con Huachito - Loteria Mujicana\n\n>!{' '.join(huachito)}!<\n\n>!Ganaste {cantidad:,} huachis (4 iguales)!<"


                elif numero == 5:

                      
                    if huachito.count('👻') == 5:
                        cantidad = 10000
                            
                    elif huachito.count('🐷') == 5:
                        cantidad = 4000

                    elif huachito.count('🍮') == 5:
                        cantidad = 5000

                    elif huachito.count('🦝') == 5:
                        cantidad = 8000

                    elif huachito.count('👾') == 5:
                        cantidad = 6000

                    elif huachito.count('👽') == 5:
                        cantidad = 7000

                    elif huachito.count('🦖') == 5:
                        cantidad = 9000

                    elif huachito.count('🐧') == 5:
                        cantidad = 3000

                    elif huachito.count('🤖') == 5:
                        cantidad = 2000

                    else:
                        cantidad = 1000
                            
                    if '💣' in huachito:
                        cantidad = round(cantidad / 2)


                    if '🥓' in huachito:

                        return f"#Rasca y gana con Huachito - Loteria Mujicana\n\n>!{' '.join(huachito)}!<\n\n>!Ganaste {cantidad:,} huachis (5 iguales usando comodin 🥓)!<"
                    
                    else:

                        return f"#Rasca y gana con Huachito - Loteria Mujicana\n\n>!{' '.join(huachito)}!<\n\n>!Ganaste {cantidad:,} huachis (5 iguales)!<"  
                    
            respuestas_perdida = ["Sigue participando","Suerte para la proxima","Asi es este negocio de rascar boletitos, llevate un dulce del mostrador"]

            return f"{random.choice(respuestas_perdida)}"

def resultados():

    victorias = 0

    derrotas = 0

    total_ganado = 0

    tres_iguales = 0

    cuatro_iguales = 0

    cinco_iguales = 0

    tocino_3 = 0

    tocino_4 = 0

    tocino_5 = 0

    pares_2 = 0

    pares_3 = 0

    for i in range(10000):

        resultado  = slots()

        if "Ganaste" in resultado:
            victorias += 1

            if "🥓" in resultado and "3 iguales" in resultado:
                tocino_3 += 1

            elif "🥓" in resultado and "4 iguales" in resultado:
                tocino_4 += 1

            elif "🥓" in resultado and "5 iguales" in resultado:
                tocino_5 += 1    

            elif "2 pares iguales" in resultado:
                pares_2 += 1

            elif "3 pares iguales" in resultado:
                pares_3 += 1

            elif "3 iguales" in resultado:
                tres_iguales += 1

            elif "4 iguales" in resultado:
                cuatro_iguales += 1

            elif "5 iguales" in resultado:
                cinco_iguales += 1

            pattern = 'Ganaste\ *(\d+)'

            cantidad = re.findall(pattern, resultado)

            total_ganado += int(cantidad[0])
        
        else:
            derrotas += 1

    print(f"""
    Huachitos = 10000
    Victorias = {victorias} (mujicanos ganan {total_ganado} huachis)
    Derrotas = {derrotas}
    ----------
    Premios pares e iguales:
    ----------
    2 pares iguales = {pares_2}
    3 pares iguales = {pares_3}
    3 iguales = {tres_iguales}
    4 iguales = {cuatro_iguales}
    5 iguales = {cinco_iguales}
    ----------
    Premios con tocino:
    ----------
    3 iguales = {tocino_3}
    4 iguales = {tocino_4}
    5 iguales = {tocino_5}
    """)
    
if __name__ == "__main__":
    resultados()

  
    