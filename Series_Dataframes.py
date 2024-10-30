# importamos la biblioteca pandas y la llamamos pd
import pandas as pd

# creamos una serie de pandas que es como una lista con etiquetas
# los valores son nombres de jugadores de psg
# el indice especifica los numeros de camisetas de esos jugadores

psg_players=pd.Series (
    ['Navas', 'Mbappe', 'Neymar', 'Messi'],  # lista de jugadores
    index=[1,7,10,30] 
)

print (psg_players)


