# Pruebas de unidad a los modulos realizados por Roman en su Tesis

# Variables y Funciones utilizadas

__Variables__

start <- guada el tiempo actual de la ejecución

specs_file <- path para el archivo que contiene las especificaciones en SOFL
SOFL_specs <- cadena de caracteres con el contenido del archivo

__Examinando la especificación en SOFL siguiente__

```s
process mod(x,y:int)
r,q: int
pre y!=0
post (y>0 and x!=0 and x=q*y+r and |r|< y and y*r>=0) or 
(y<0 and x!=0 and x=q*y+r and |r|<-y and y*r>=0) or
(x=0 and q=0 and r=0)
end_process
```
operation_name <- 
    SOFL_specs[0:11].replace('process ', '') $\equiv$ 
        'mod'

vars_info <-
    SOFL_specs[0:33] $\equiv$ 
        'process mod(x:int,y:int)\nr,q: int\n'


input_Variables, output_Variables <-
    `divideVars(vars_info)`
//----------------------------------------------------------------------
vars_info.rsplit('\n') : es una lista de subcadenas
    ['process mod(x:y:int)', 'r,q:int', '']

[20] linewithInputs : es una cadena de caracteres que contiene las var. de entrada
linewithInputs <-
    'process mod(x,y:int)'

[21] linewithOutputs : es una cadena de caracteres que contine las var. de salida
    'r,q:int'

[23] lineiwith inputs<-
    'x,y:int'

[38] inputList <- 
    ['x,y:int']

listwithInputs <- ['x,y','int']
[43] input_Variable <- {'int':['x','y']}

[59] output_Variable <- {'int':['r','q']}

[60] input_Variables.key() <- ['int']

[67] input_Variable, output_Variable <- {'int':['x','y']}, {'int':['r','q']}
//----------------------------------------------------------------------

pre <- 
    'y!=0\n'.replace('\n','') <- 'y!=0'

post <-
    'post (y>0 and x!=0 and x=q*y+r and |r|< y and y*r>=0) or\n(y<0 and x!=0 and x=q*y+r and |r|<-y and y*r>=0) or\n(x=0 and q=0 and r=0)'.replace('\n','')
    <- 'post (y>0 and x!=0 and x=q*y+r and |r|< y and y*r>=0) or(y<0 and x!=0 andx=q*y+r and|r|<-y and y*r>=0) or(x=0 and q=0 and r=0)'

_dividir funcion de guarda y definicion de la post_

[73] post <-
    ' (y>0 and x!=0 and x=q*y+r and |r|< y and y*r>=0) or(y<0 and x!=0 andx=q*y+r and|r|<-y and y*r>=0) or(x=0 and q=0 and r=0)'

[75] clauses <-
    [' (y>0 and x!=0 and x=q*y+r and |r|< y and y*r>=0) ','(y<0 and x!=0 andx=q*y+r and|r|<-y and y*r>=0) ','(x=0 and q=0 and r=0)']
    


    




