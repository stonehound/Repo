MacBook-Air:python devin$ ls
__pycache__	bar.py		drumseq		fractest.py	midi		pycairo.py	supriyatest.py
anim.py		cairo.py	example.svg	graph.py	projnote.md	scamptest.py	venv
MacBook-Air:python devin$ clear

































MacBook-Air:python devin$ python3 bar.py
/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/pygame/pkgdata.py:25: UserWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html. The pkg_resources package is slated for removal as early as 2025-11-30. Refrain from using this package or pin to Setuptools<81.
  from pkg_resources import resource_stream, resource_exists
pygame 2.6.1 (SDL 2.28.4, Python 3.13.6)
Hello from the pygame community. https://www.pygame.org/contribute.html
2025-09-15 18:08:20.561 Python[10435:272448] WARNING: Secure coding is automatically enabled for restorable state! However, not on all supported macOS versions of this application. Opt-in to secure coding explicitly by implementing NSApplicationDelegate.applicationSupportsSecureRestorableState:.
MacBook-Air:python devin$ vim bar.py
MacBook-Air:python devin$ vim bar.py

























import pygame

pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Grow Shape from Bottom")

# Initial rectangle properties
# Start with a height of 0 at the bottom of the screen
rect_x = SCREEN_WIDTH // 2 - 25
rect_y = SCREEN_HEIGHT
rect_width = 50
rect_height = 0

# Create the rect object
growing_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Animation properties
grow_speed = 2
max_height = 360

running = True
clock = pygame.time.Clock()

grow = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
"bar.py" 63L, 1517B

