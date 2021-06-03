import pandas as pd
import webbrowser



#PARA EL PRIMER CSV------------------------------------------------------------------------------------------------------------------------------
datos = pd.read_csv("PrevalenciaC.csv")
df = pd.DataFrame(datos)
script = ""
i=0
while i<31:
        script = script+"{x:'"+datos['Estado'].loc[i]+"', y:"+str(datos['Prevalencia consumo de cigarro en 30 dias'].loc[i])+", z:"+str(i+1)+"},\n"
        i+=1
print (script)
df.groupby('Estado')['Prevalencia consumo de cigarro en 30 dias'].sum().plot(kind='line',title='Prevalencia consumo de cigarro en 30 dias por entidad',color='red')


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------




#GRAFICAS XD----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#df1.groupby('Ano')['Alcohol'].sum().plot(kind='bar',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='barh',legend='Reverse')
#df.groupby('Model')['Price'].sum().plot(kind='hist',legend='Reverse')
#df1.groupby('Ano')['Alcohol'].sum().plot(kind='box',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='kde',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='density',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='area',legend='Reverse')
#df.groupby('Model')['Price'].sum().plot(kind='pie',legend='Reverse')
#df.groupby('Model')['Price'].sum().plot(kind='scatter',legend='Reverse')
#df1.groupby('Name')['Transaction'].sum().plot(kind='hexbin',legend='Reverse')
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


f = open('Adicciones2.html','w')

mensaje = """<html>
<head>
<title>Gráficas con JavaScript</title>
<meta charset='utf-8'>
<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>
<link rel='stylesheet' type='text/css' href='morris.css'>  
<link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.css">
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.min.js"></script>
<script src='Morris.js'></script>
<script>    
function grafica1(){
  new Morris.Line({
  element: 'graph',
  data: ["""+script+"""
          ],
  xkey: 'x',
  ykeys: ['y','z'],
  axes:false,
  labels: ['Y','Z'],
  resize:true,
  lineColors:['#2CB4AC']
  });
}

</script>
</head>
<body>
<div id='graph'></div>
<p id=texto1>hola que hace xd</p>
<input type='button' value='grafica' onclick='grafica1()'>

</body>
</html>"""
f.write(mensaje)
f.close()

webbrowser.open_new_tab('Adicciones.html')

#print(datos.to_excel("CreditCards.xls",sheet_name="datos"))