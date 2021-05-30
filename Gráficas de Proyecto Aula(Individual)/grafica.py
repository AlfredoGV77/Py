import pandas as pd
import webbrowser
datos = pd.read_csv("PrevalenciaC.csv")
df = pd.DataFrame(datos)
i=0
script = ""
while i<11:
        script = script+"{x:'"+str(datos['Estado'].loc[i])+"', y:"+str(datos['Prevalencia consumo de cigarro en 30 dias'].loc[i])+", z:"+str(i+1)+"},\n"
        i+=1
print (script)
df.groupby('Estado')['Prevalencia consumo de cigarro en 30 dias'].sum().plot(kind='bar',legend='Reverse',title='Cigarros Fumados por Dia ',color='cyan')
#df.groupby('Estado')['Prevalencia consumo de cigarro en 30 dias'].sum().plot(kind='bar',legend='Reverse')
#df.groupby('Estado')['Prevalencia consumo de cigarro en 30 dias'].sum().plot(kind='barh',legend='Reverse')
#df.groupby('Estado')['Prevalencia consumo de cigarro en 30 dias'].sum().plot(kind='hist',legend='Reverse')
#df.groupby('Estado')['Prevalencia consumo de cigarro en 30 dias'].sum().plot(kind='kde',legend='Reverse')
#df.groupby('Estado')['Prevalencia consumo de cigarro en 30 dias'].sum().plot(kind='density',legend='Reverse')
#df.groupby('Estado')['Prevalencia consumo de cigarro en 30 dias'].sum().plot(kind='pie',legend='Reverse')


f = open('camaras.html','w')

"""

{x:'CDMX', y:28, z:1},
{x:'Puebla', y:27, z:2},
{x:'Edo.Mexico', y:27, z:3},
{x:'Guanajuato', y:23, z:4},
{x:'Durango', y:24, z:5},
{x:'Morelos', y:22, z:6},
{x:'Zacatecas', y:22, z:7},
{x:'San Luis Potosi', y:20, z:8},
{x:'Sonora', y:20, z:9},
{x:'Guerrero', y:20, z:10},
{x:'Hidalgo', y:19, z:11},


"""







f = open('Adicciones.html','w')

mensaje = """<html>
<head>
<title>Gráficas de Adicciones</title>
<meta charset='utf-8'>
<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>
<link rel='stylesheet' type='text/css' href='morris.css'>  
<script src='http://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js'></script>
<script src='http://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js'></script>
<script src='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js' integrity='sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM' crossorigin='anonymous'></script> 
<script src='morris.min.js'></script>
<script>    
function grafica1(){
  new Morris.Bar({
  element: 'graph',
  data: ["""+script+"""
          ],
  xkey: 'x',
  ykeys: ['y'],
  axes:false,
  labels: ['Prevalencia:'],
  resize:true,
  lineColors:['#2CB4AC']
  });
}
</script>
</head>
<body>
<div id='graph'></div>
<input type='button' value='grafica' onclick='grafica1()'>
</body>
</html>"""
f.write(mensaje)
f.close()

webbrowser.open_new_tab('Adicciones.html')