# XindeX
Indice Python para Terminal

quiero que el indice se genere  con streamlit (ejecuta_st.py y ejecutado_st.py)
y se recuperen los datos en un diccionario. y cuando cierre streamlit vuelva  al 
programa principal y pueda ejecutar el indice creado en streamlit.
veo estas opciones para hacer este proceso. quiero que las valides para ver si 
es viable lo que sugiero.
no quiero codigo aun, solo quiero analisis y orientación, eso si, analiza el codigo.
el streamlit que quiero ejecutar para configurar el indice es tal como ./identa/identa6.html 
y quiero que se ejecute y retorne comno ./ejecuta_st/ejecuta_st.py y ./ejecuta_st/ejecutado_st.py

las opciones que se me han ocurrido y que quiero que analices serían:

# opcion 1
Se abre Over_Main, este abre como subprocess streamlit que genera un diccionario qeu cuando se 
pulsa el boton se envía a Over_Main y se muestra el resultado con mystica. 
a partir de ahí se sigue en terminal.

■ problema: como se ejecutan las funciones?
■ problema: usuario CIERRA STREAMLIT A LAS BRAVAS

# opcion 2
Se abre Over_Main
if json and b_config=True ??    
    se lee json ► streamlit 
    if boton_st:
        recibe json + lee json
        mystica +     se sigue en terminal.
    else:   
        (CIERRA STREAMLIT A LAS BRAVAS)

    mystyca +    se sigue en terminal.

elif json and b_config=False:
    mystica +     se sigue en terminal.
elif not json and b_config=True:
    streamlit:
    if boton_st:
        recibe json + lee json
        mystica +     se sigue en terminal.
    else:   
        (CIERRA STREAMLIT A LAS BRAVAS)
elif not json and b_config=False:

# opcion 3
Abre streamlit y ejecuta las funciones del terminal en web.
Tengo que crear un mapa(diccionario nombre_funcion:funcion) en el programa principal


