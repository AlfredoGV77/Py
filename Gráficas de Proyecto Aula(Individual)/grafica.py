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


#PARA EL SEGUNDO CSV-----------------------------------------------------------------------------------------------------------------
datos2 = pd.read_csv("AdiccionesDatos.csv")
df1 = pd.DataFrame(datos2)
script2 = ""
i2=0
while i2<13:
        script2 = script2+"{x:'"+str(datos2['Ano'].loc[i2])+"', y:"+str(datos2['Alcohol'].loc[i2])+", z:"+str(i2+1)+"},\n"
        i2+=1
print (script2)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#PARA EL 3ER CSV----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
datos3=pd.read_csv("AbusoSustancias.csv")
df2 = pd.DataFrame(datos3)
script3 = ""
i3=0
while i3<5:
        script3 = script3+"{value:'"+str((datos3['Pacientes'].loc[i3]))+"', label:"+str(datos3['Enfermedad'].loc[i3])+"},\n"
        i3+=1
print (script3)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


datos4=pd.read_csv("Adolescentes_PrevencionAdicciones.csv")
df3 = pd.DataFrame(datos4)
script4 = ""
i4=0
while i4<33:
        script4 = script4+"{HOMBRES:'"+str(datos4['MASCULINO'].loc[i4])+"', MUJERES:"+str(datos4['FEMENINO'].loc[i4])+"},\n"
        i4+=1
print (script4)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

datos5=pd.read_csv("TasaMortalidadEPOC.csv")
df4 = pd.DataFrame(datos4)
script5 = ""
i5=0
while i5<792:
        script5 = script5+"{x:'"+str(datos5['Año'].loc[i5])+"', y:"+str(datos5['Muertes por EPOC'].loc[i5])+", z:"+str(datos5['Tasa Mortalidad'].loc[i5])+"},\n"
        i5+=1
print(script5)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


datos6=pd.read_csv("TasaMortalidadDiabetes.csv")
df6 = pd.DataFrame(datos6)
script6 = ""
i6=0
while i6<528:
        script6 = script6+"{elapsed:'"+str(datos6['Año'].loc[i6])+"', y:"+str(datos6['Muertes por Diabetes'].loc[i6])+"},\n"
        i6+=1
print(script6)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------

datos7=pd.read_csv("Pruebas_Tamizaje.csv")
df7 = pd.DataFrame(datos7)
script7 = ""
i7=0
while i7<33:
        script7 = script7+"{value:'"+str(datos7['TOTAL DE TAMIZAJES '].loc[i7])+"', label:"+str(datos7['ENTIDAD'].loc[i7])+"},\n"
        i7+=1
print(script7)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------


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

function grafica2(){
  new Morris.Area({
  element: 'graph',
  data: ["""+script2+"""
          ],
  xkey: 'x',
  ykeys: ['y','z'],
  axes:false,
  labels: ['Y','Z'],
  resize:true,
  lineColors:['#2CB4AC']
  });   
}


function grafica3(){
  new Morris.Area({
    element: 'graph',
    data: ["""+script3+"""
          ],
          backgroundColor: '#ccc',
          labelColor: '#060',
          colors: [
            '#0BA462',
            '#39B580',
            '#67C69D',
            '#95D7BB'
          ],
          formatter: function (x) { return x + "%"}
    });   
}


function grafica4(){
  new Morris.Donut({
    element: 'graph',
    data: ["""+script4+"""
          ],
          backgroundColor: '#ccc',
          labelColor: '#060',
          colors: [
            '#0BA462',
            '#39B580',
            '#67C69D',
            '#95D7BB'
          ],
          formatter: function (x) { return x + "%"}
    });   
}



function grafica5(){

    var day_data = ["""+script5+"""
  ];
  Morris.Line({
    element: 'graph5',
    data: day_data,
    xkey: 'elapsed',
    ykeys: ['value'],
    labels: ['Muertes por diabetes'],
    parseTime: false
  });


}



function grafica6(){

  new Morris.Donut({
    element: 'graph6',
    data: ["""+script6+"""
          ],
          backgroundColor: '#ccc',
          labelColor: '#060',
          colors: [
            '#74d2e7',
            '#009f4d',
            '#efdf00',
            '#fe5000',
            '#e4002b',
          ],
          formatter: function (x) { return x + ""}
    });

}












</script>
</head>
<body>
<div id='graph'></div>
<p id=texto1>hola que hace xd</p>
<input type='button' value='grafica' onclick='grafica1()'>
<input type='button' value='grafica' onclick='grafica2()'>
<input type='button' value='grafica' onclick='grafica3()'>
<input type='button' value='grafica' onclick='grafica4()'>
<input type='button' value='grafica' onclick='grafica5()'>
<input type='button' value='grafica' onclick='grafica6()'>
</body>
</html>"""
f.write(mensaje)
f.close()

webbrowser.open_new_tab('Adicciones.html')

#print(datos.to_excel("CreditCards.xls",sheet_name="datos"))