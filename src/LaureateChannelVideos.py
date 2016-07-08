
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import json
import requests


COMODINES = "part=id%2CcontentDetails"
PARAMETROS = "&forUsername=LaureateChannel&key="
API_KEY = "AIzaSyDp_2064ipFwhPEU2McAue9L3GZ90Pwz_w"
URLGET = "https://www.googleapis.com/youtube/v3/channels?"
global UPLOAD_ID
global CHANNEL_ID
global TITLE
global nextPageToken
lista=[]
VideoList=[]
#global VideoList #estructura ['VideoID','VideoTitulo','VideoDescripcion']
#obteniendo el id del canal de youtube
FULL_URL = URLGET + COMODINES + PARAMETROS + API_KEY
response = requests.get(FULL_URL)
if response.status_code == 200:
    results = response.json()
    items = results['items']
    for item in items:
        UPLOAD_ID = item['contentDetails']['relatedPlaylists']['uploads']
        CHANNEL_ID = item['id']
else:
    print "Error code %s" % response.status_code
#print CHANNEL_ID  
#print UPLOAD_ID  
#con el id del cana obtenemos todos los videos
URLGET = "https://www.googleapis.com/youtube/v3/playlistItems?"
COMODINES = "part=snippet"
PARAMETROS = "&playlistId=" +UPLOAD_ID +"&maxResults=50"+"&key=" + API_KEY
FULL_URL = URLGET + COMODINES + PARAMETROS
response = requests.get(FULL_URL)
contador=1
if response.status_code == 200:
    results = response.json()
    items = results['items']
    nextPageToken = results['nextPageToken']
    while (nextPageToken!=""):
        for item in items:
           print contador,"-", (item['snippet']['title']).encode("utf-8")
           videoID=(item['snippet']['resourceId']['videoId']).encode("utf-8") 
           videoTi=(item['snippet']['title']).encode("utf-8")
           videoDes=(item['snippet']['description']).encode("utf-8")
           lista=[videoID,videoTi,videoDes]
           VideoList.append(lista)
#           VideoList=[videoID,videoTi,videoDes]
#           List.append(VideoList)
           contador=contador+1
        if(nextPageToken!="last"):
            PARAMETROS="&playlistId="+UPLOAD_ID+"&maxResults=50"+"&pageToken="+nextPageToken+"&key="+API_KEY
            FULL_URL=URLGET+COMODINES+PARAMETROS
            requests.get(FULL_URL)
            response=requests.get(FULL_URL)
            results=response.json()
            items=results['items']
            try:
               nextPageToken = results['nextPageToken']
            except KeyError as e: #si se encuentral al final de la lista
                nextPageToken="last"
        else:
               nextPageToken=""
    print "------------------------------------------------------------------------------------"  
    print "Fin lista"   
else:
    print "Error code %s" % response.status_code
  
        
#busqueda del video dentro de la lista de videos de LaureateChannel
option=0
Watchlink="https://www.youtube.com/watch?v="
while option!=-1:
    print "-----------------------------------------------------------------------------"
    print "Menu"
    print "1-para buscar un video en la lista en relacion al <Titulo> del video"
    print "2-para buscar un video en la lista en relacion a la <descripcion> del video"
    print "3-implimir lista de videos"
    print "4-salir"
    option=input()
    print "-----------------------------------------------------------------------------"
    if(option==1):
        print "Busqueda por Titulo"
        text=raw_input("Ingrese un titulo :")
        conteo=1
        for item in VideoList:
            contiene=item[1].find(text)
            if(contiene!=-1):
                print conteo,"-",item[1]," Link:",Watchlink+item[0]
                conteo=conteo+1
    else:
       if(option==2):          
        print "Busqueda por Descripcion"
        text=raw_input("Ingrese una descripcion :")
        conteo=1
        for item in VideoList:
            contiene=item[2].find(text)
            if(contiene!=-1):
                print conteo,"-",item[2]," Link:"," Link:",Watchlink+item[0]
                conteo=conteo+1
       else:
         if(option==3):
              print"lista de canales"
              for video in VideoList:
                  print video
                  
         else:
             print "Salir"
             option=-1

print "Fin del programa"
    