import gradio as gr
import pandas as pd
import sqlite3

def fetch_teams():

    conn = sqlite3.connect('playoffs.db')
    cursor = conn.cursor()

    query = '''
    SELECT*
    from teams;
    '''

    cursor.execute(query)
    output = cursor.fetchall()
    conn.close()

    outputDF = pd.DataFrame(output, columns=['id', 'City', 'Name'])
    return outputDF

iFace = gr.Interface(fetch_teams, inputs = [], outputs = gr.Dataframe(headers = ['id', 'City', 'Name']))
iFace.launch()

