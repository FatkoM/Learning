import pygame
import random
import webbrowser

sauce = random.randint(0,474960)
#user_horny = input("SAUCE OR TAG?").upper()

##if user_horny == "TAG":
    #user_tag = input("Please input the tags that you would like.")
    #webbrowser.open(f"https://nhentai.net/search/?q=[{user_tag} english]")

#elif user_horny == "SAUCE":
    #user_sauce = input("Please input your sauce")
    #webbrowser.open(f"https://nhentai.net/g/{user_sauce}")

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("The nhentai helper!")
clock = pygame.time.Clock()
text = pygame.font.Font("images\VCR_OSD_MONO_1.001.ttf", 50)
background = pygame.image.load("images\what.jpg")

text_surface = text.render("N-HELPER!", False, "Red")
tag_surface = text.render("Tag?", False, "Yellow")
sauce_surface= text.render("Sauce?", False, "Green")
question_surface = text.render("Enter the tags please!", False, "Red")

user_text= ""

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            print(user_text)
            exit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER:
            print("underscore")
            screen.blit(question_surface,(200,200))
            screen.blit(input_field,(300,300))
            webbrowser.open(f"https://nhentai.net/search/?q=[{user_text}]")
        elif event.type == pygame.KEYDOWN:
            print("key_down")
            user_text+=event.unicode
        
        input_field =  text.render(user_text, False, "Red")


            #if event.type == pygame.K_BACKSPACE:
                #user_text.repace(user_text[-1],"") 

    

        


    screen.blit(background,(-100,-100))
    screen.blit(input_field,(300,300))
    screen.blit(tag_surface,(100,100))
    screen.blit(sauce_surface,(600,100))
    screen.blit(text_surface,(300,0))
    

    
    pygame.display.update()
    clock.tick(60)