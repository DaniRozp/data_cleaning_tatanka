import pandas as pd
def mergeData():
    reacciones = pd.read_csv("../Directory")
    emociones = pd.read_csv("../Directory")
    emociones_agrupadas = emociones.groupby(['Post ID', 'Category_list_label'])['Category_list_label'].count()
    emociones_agrupadas_df = pd.DataFrame(data = emociones_agrupadas)
    emociones_agrupadas_df=emociones_agrupadas_df.rename({"Category_list_label":"Count"},axis=1).reset_index()
    emociones_agrupadas_df=emociones_agrupadas_df.pivot(index='Post ID', columns='Category_list_label', values='Count').fillna(0)
    result = pd.merge(emociones_agrupadas_df, reacciones, on='Post ID')

    return emociones_agrupadas_df

print(mergeData())
