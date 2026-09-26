import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar dimensiones de la ventana
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi primer juego en vivo")

# Control de los fotogramas por segundo (FPS)
reloj = pygame.time.Clock()

# Color de fondo (RGB)
COLOR_FONDO = (30, 30, 30)

# --- PROPIEDADES DEL PERSONAJE ---
# Posición inicial (X, Y) en el centro de la pantalla
jugador_x = 350
jugador_y = 250
# Tamaño del cuadrado (Ancho, Alto)
jugador_ancho = 50
jugador_alto = 50
# Velocidad de movimiento (píxeles por fotograma)
velocidad = 5

# Bucle principal del juego
while True:
    # 1. Capturar eventos del sistema
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Capturar teclas presionadas en tiempo real (Movimiento en vivo)
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:
        jugador_x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador_x += velocidad
    if teclas[pygame.K_UP]:
        jugador_y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador_y += velocidad

    # 3. Dibujar elementos en pantalla
    pantalla.fill(COLOR_FONDO)
    
    # Dibujar al personaje usando las variables de posición actualizadas
    pygame.draw.rect(pantalla, (255, 0, 0), (jugador_x, jugador_y, jugador_ancho, jugador_alto))

    # 4. Refrescar la pantalla
    pygame.display.flip()
    
    # Mantener a 60 fotogramas por segundo
    reloj.tick(60)
