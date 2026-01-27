import pygame

def unde(x):
    return (x[0]//300,x[1]//300)
def ial(x,piesa):
    if piesa:     
        puse[f'col{x[0]}'].append('x')
        puse[f'lin{x[1]}'].append('x')
        if x[0]+x[1]==2:
            puse['diagpos'].append('x')
        if x[0]==x[1]:
            puse['diagneg'].append('x')
    else:
        puse[f'col{x[0]}'].append('o')
        puse[f'lin{x[1]}'].append('o')
        if x[0]+x[1]==2:
            puse['diagpos'].append('o')
        if x[0]==x[1]:
            puse['diagneg'].append('o')
def winner():
    for j,i in puse.items():
        if len(i)==3 and i[0]==i[1]==i[2]:
            return j


pozitii={
            (0,0):(-100,-100), 
            (0,1):(-100,200),
            (0,2):(-100,500),
            (1,0):(200,-100), 
            (1,1):(200,200),
            (1,2):(200,500),
            (2,0):(500,-100),
            (2,1):(500,200), 
            (2,2):(500,500)   
}
linii={
    'col0':[(150,0),(150,900)],
    'col1':[(450,0),(450,900)],
    'col2':[(750,0),(750,900)],
    'lin0':[(0,150),(900,150)],
    'lin1':[(0,450),(900,450)],
    'lin2':[(0,750),(900,750)],
    'diagpos':[(900,0),(0,900)],
    'diagneg':[(0,0),(900,900)]
}
puse={
    'col0':[],
    'col1':[],
    'col2':[],
    'lin0':[],
    'lin1':[],
    'lin2':[],
    'diagpos':[],
    'diagneg':[]
}
pygame.init()
pygame.event.set_blocked(None)
pygame.event.set_allowed(pygame.QUIT)
pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)

screen = pygame.display.set_mode((900, 900))
pygame.display.set_caption("x si o")
ximg=pygame.image.load('x.png')
o=pygame.image.load('o.png')
screen.fill((255,255,255))
negru=(0,0,0)

for row in range(3):
    for col in range(3):
        x = col * 300
        y = row * 300
        pygame.draw.rect(
            screen,
            negru,
            pygame.Rect(x, y, 300, 300),
            width=1,
            border_radius=1
        )


c=None
running = True
x=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if unde(event.pos) in pozitii:
                if x:
                    screen.blit(ximg,pozitii[unde(event.pos)])
                    ial(unde(event.pos),x)
                    x=False
                else:
                    screen.blit(o,pozitii[unde(event.pos)])
                    ial(unde(event.pos),x)
                    x=True
                pozitii.pop(unde(event.pos))
                c=winner()
                if c:
                    pygame.draw.line(screen,(0,0,255),linii[c][0],linii[c][1],10)
                    pozitii.clear()
    pygame.display.flip()
pygame.quit()