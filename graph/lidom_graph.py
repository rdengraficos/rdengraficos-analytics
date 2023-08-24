
from models.lidom_model import LidomModel
import plotly.express as px
from dash import dcc
   


class LidomGraph():

    @staticmethod
    def build_position_table_line(ganados): 
        fig = px.line(ganados, x='Temporada', y='G', 
              color='Equipo',
              title='Evolución de Victorias por Equipo a lo Largo de los Años')
        
        return dcc.Graph(figure=fig)
