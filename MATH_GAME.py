#we import the modules that we are going to use in the development
import time
import random
#say hi to players
print("Bienvenidos a nuestro juego matematico,el jugador con mayor puntaje sera el ganador")
print ("Responde lo mas rapido posible")
#flag variable for while loop
jugar='si'
while jugar=='si':
    inicio=time.time()#We store the start time in the "inicio" variable
    numazar1=random.randint(1,9)
    numazar2=random.randint(1,9)#in these two lines we pick two random numbers
    respuesta2=numazar1*numazar2#here we keep the correct answer
    respuesta=int(input("cuanto es "+str(numazar1)+str("*")+str(numazar2)))#player answer
    final=time.time()#final time
    tiempo=round(final-inicio,0)#time it took for the player to respond
    if respuesta == respuesta2:
        print("Felicidades, resultado correcto")
        if tiempo < 5 :
            puntaje=tiempo*50#score if he answer in 5 seconds
            print("tu tiempo fue de :",tiempo,"segundos,y tu puntaje de: ",puntaje,"puntos\nEXCELENTE")
        if tiempo >= 5:
            puntaje=tiempo*1#score if he answer after 5 seconds
            print("tu tiempo fue de :",tiempo,"segundos,y tu puntaje de : ",puntaje,"puedes ,mejorar")
        jugar=input("quieres jugar otra vez")#we update flag variable
        if jugar == 'no':#the loop will break 
            break
    else:
        print("Respuesta incoreccta,Suerte para la proxima")#wrong answer
        jugar=input("quieres jugar otra vez")
        if jugar == 'no':
            break
        
    
         
        
        
            
       
               
            
         
            
            
        
