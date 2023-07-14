import pygame
import time
import random

pygame.init()
gray=(60,60,60)
black=(255,0,0)

display=pygame.display.set_mode((830,600))

pygame.display.set_caption("Racing game")

#load car image
carimg=pygame.image.load("car1.png")
#load background image for the left side
backgroundleft=pygame.image.load("left.png")
#load background image for the right side
backgroundright=pygame.image.load("right.png")
#Defined car width
car_width=23

#define car functions that are coming from the opposite side.#(we are naming car that are coming from the opposite side policecar)
def policecar(police_startx,police_starty,police):
    if police==0:
        #for police car no 2
        police_come=pygame.image.load("car2.png")
    if police==1:
        #for police car no 3
        police_come=pygame.image.load("car3.png")
    if police==2:
        #for police car no 1
        police_come=pygame.image.load("car1.png")
    #display the police car
    display.blit(police_come,(police_startx,police_starty))

def background():
    #defining the position of background image for left side in x axis & y axis
    display.blit(backgroundleft,(0,0))
    #defining the position of background image for right side in x axis & y axis
    display.blit(backgroundright,(700,0))

#creating the function that will display the game over message
def crash():
    message_display("Game Over")

#create function for customizing the game over message
def message_display(text):
    #set font style and size of the message
    large_text=pygame.font.Font("freesansbold.ttf",80)
    #set function to edit the message
    textsurf,textrect=text_object(text,large_text)
    #set the position of the message on the screen
    textrect.center=((400),(300))
    #display the message
    display.blit(textsurf,textrect)
    pygame.display.update()
    #After the car has crashed, wait 3 seconds.
    time.sleep(3)
    #call the loop function to restart the game
    loop()

#This function will display the message after the car has crashed.
def text_object(text,font):
    #set color of the message
    text_surface=font.render(text,True,black)
    #after that restart the game & ready to give some input
    return text_surface,text_surface.get_rect()
