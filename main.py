import pandas as pd
from fuzzy_system import evaluar_paciente_difuso
from patient_input import procesar_fila


csv_data_path = 'csv_data/'
csv_result_path = 'csv_result/'
csv_name = 'test'


# Cargamos CSV
df = pd.read_csv(csv_data_path + csv_name + '.csv', delimiter=';')

# Evaluamos cada paciente y añadimos una COLUMNA DE RIESGO ESTIMADO
riesgos_estimados = []
i = 0

for _, row in df.iterrows():
    i += 1
    print(i)
    entrada = procesar_fila(row)
    riesgo = evaluar_paciente_difuso(entrada)
    riesgos_estimados.append(riesgo)

df['RIESGO_ESTIMADO'] = riesgos_estimados

# Mostrar resultados
print(df[['AGE', 'AP_HIGH', 'CHOLESTEROL', 'GLUCOSE', 'RIESGO_ESTIMADO']].head())

# Guardar resultado 
df.to_csv(csv_result_path + csv_name + '.csv', index=False)


