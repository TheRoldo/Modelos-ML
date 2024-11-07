#¿Qué programas académicos están alineados con las tendencias
# del mercado laboral y cuáles tienen más potencial para la empleabilidad de los egresados?
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 


data = pd.read_excel(r"Data set estudiantes matriculados 2023.xlsx")
data.head()
data.info()

#Eliminar datos faltantes 
data.dropna(inplace=True)
data.info()

#Conteo de subniveles de las diferentes columnas categoricas 
cols_cat =['CÓDIGO DE LA INSTITUCIÓN','INSTITUCIÓN DE EDUCACIÓN SUPERIOR (IES)','TIPO IES','SECTOR IES',
           'CARÁCTER IES','DEPARTAMENTO DE DOMICILIO DE LA IES','IES ACREDITADA','PROGRAMA ACADÉMICO','PROGRAMA ACREDITADO',
           'NIVEL ACADÉMICO','NIVEL DE FORMACIÓN','MODALIDAD','ÁREA DE CONOCIMIENTO','NÚCLEO BÁSICO DEL CONOCIMIENTO (NBC)',
           'DESC CINE CAMPO AMPLIO','DESC CINE CAMPO ESPECIFICO','DESC CINE CAMPO DETALLADO','DEPARTAMENTO DE OFERTA DEL PROGRAMA']

for col in cols_cat:
     print(f'Columna {col}: {data[col].nunique()}subniveles')


print(data.describe())
#Se elimina la columna año porque tiene un unico valor el año 2023 
data= data.drop(columns=['AÑO'])

#Filas repetidas
print(f'Tamaño del set de datos Con filas repetidas:{data.shape}' )
data.drop_duplicates(inplace=True)
print(f'Tamaño del set de datos SIN filas repetidas:{data.shape}' )
#Concluimos que no tiene filas repetidas

#Revisamos si hay valores extremos o Outhliers en las variables numericas
#Generar Graficas individuales para las variables numericas


# Definir las columnas numéricas para los gráficos
cols_num = ['IES PADRE', 'ID SECTOR IES', 'ID CARÁCTER IES', 'CÓDIGO DEL DEPARTAMENTO (IES)', 
            'CÓDIGO DEL MUNICIPIO IES', 'CÓDIGO SNIES DEL PROGRAMA', 'ID NIVEL ACADÉMICO', 
            'ID NIVEL DE FORMACIÓN', 'ID MODALIDAD', 'ID ÁREA', 'ID NÚCLEO', 
            'ID CINE CAMPO AMPLIO', 'ID CINE CAMPO ESPECIFICO', 'ID CINE CAMPO DETALLADO', 
            'CÓDIGO DEL DEPARTAMENTO (PROGRAMA)', 'DEPARTAMENTO DE OFERTA DEL PROGRAMA', 
            'CÓDIGO DEL MUNICIPIO (PROGRAMA)', 'ID SEXO', 'SEMESTRE', 'MATRICULADOS']

# Iterar sobre las columnas numéricas y generar un gráfico por cada una
for col in cols_num:
    # Crear una nueva figura para cada gráfico
    plt.figure(figsize=(8, 6))  # Ajusta el tamaño de la figura si es necesario
    sns.boxenplot(x=col, data=data)
    plt.title(f'Boxenplot de {col}')  # Título del gráfico
    plt.xlabel(col)  # Etiqueta en el eje x
    plt.ylabel('Valores')  # Etiqueta en el eje y
    plt.show()  # Mostrar el gráfico
#Errores tipograficos
#Graficar subniveles de cada variable categorica 
    # Crear una nueva figura para cada gráfico
   # plt.figure(figsize=(8, 6))  # Ajusta el tamaño de la figura si es necesario
   # sns.boxenplot(x=col, data=data)
    #plt.title(f'Boxenplot de {col}')  # Título del gráfico
   # plt.xlabel(col)  # Etiqueta en el eje x
   # plt.ylabel('Valores')  # Etiqueta en el eje y
    #plt.show()  # Mostrar el gráfico