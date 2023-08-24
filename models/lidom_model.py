import pandas as pd



class LidomModel():

    @staticmethod
    def get_position_table()->pd.DataFrame:
        df = pd.read_csv('static/file/lidom_tabla_posiciones_equipos_2012_2022.csv')
        ganados=df[['Equipo','Temporada','G']].groupby(['Equipo','Temporada']).sum('G').reset_index()
        return ganados

