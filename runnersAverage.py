# # nuestro código no puede vivir dentro de un libro de jupyter. Para poder compartirlo debemos encapsularlo dentro de una función para después crear un módulo con el que podamos organizar y compartir nuestro código.


# def data_runners(file_name: str) -> tuple:
#     # es bueno añadir un comentario al inicio de la función para indicar que hace.
#     """ Dado el nombre de un corredor, extrae los datos necesarios
#     y los devuelve como una tupla """
#     return 'media'


# copiamos nuestro código dentro de la función:

import statistics

FOLDER = '../registros/'


def data_runners(file_name: str) -> tuple:
    """ Dado el nombre de un corredor, extrae los datos necesarios
     y los devuelve como una tupla 
    """
    runner, meters, category = file_name.removesuffix(".csv").split("-")
    with open(FOLDER + file_name) as df:
        data = df.readlines()

    times = []
    for i in data:
        line = i.removesuffix("\n").split(";")[1]
        # print(line)
        if line != "Tiempo":
            times.append(line)
    list_converted_times = []

    for t in times:
        minutes, rest = t.split(":")
        seconds, hundredths = rest.split(".")
        hundredths_time = int(minutes)*60*100 + \
            int(seconds)*100 + int(hundredths)
        list_converted_times.append(hundredths_time)

    average_time = statistics.mean(list_converted_times)
    round(average_time / 100, 2)
    str(round(average_time / 100, 2)).split(".")
    seconds, hundredths = str(round(average_time / 100, 2)).split(".")
    seconds = int(seconds)
    # los pasamos a minutos
    minutes = seconds / 60
    minutes = seconds // 60
    # Ahora vamos a calcular el nº de segundos
    seconds = seconds - minutes*60
    average_time_str = str(minutes) + ":" + str(seconds) + "." + hundredths

    # la función retorna una tupla, solamente puede devolver un resultado
    # como en una ecuación matemática.
    return runner, meters, category, average_time, average_time_str, times

# ahora vamos a crear un nuevo libro de jupyter y vamos a importar nuestro nuevo modulo
