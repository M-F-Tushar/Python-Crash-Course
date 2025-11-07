# Complete Guide to Building Alien Invasion Game with Pygame

## Chapter Overview: A Ship that Fires Bullets

This chapter introduces game development with Pygame by building the foundation of an Alien Invasion game. We'll create a controllable spaceship that can move and fire bullets, establishing the core mechanics for a complete game.

## Learning Objectives

By the end of this chapter, you will:
- Understand the basic structure of a Pygame application
- Create and manage game objects (ship, bullets)
- Handle user input for game control
- Implement continuous movement and collision detection
- Organize code into manageable classes and methods
- Use sprite groups for efficient object management

---

## 1. Project Planning and Setup

### 1.1 Game Description and Requirements

**Game Concept:**
- Player controls a rocket ship at the bottom center of the screen
- Ship moves left/right with arrow keys
- Ship fires bullets with spacebar
- Fleet of aliens moves across and down the screen
- Player destroys aliens by shooting them
- Game ends when player loses three ships
- New fleets move faster than previous ones

**Development Phases:**
1. **Phase 1 (This Chapter):** Create movable ship that fires bullets
2. **Phase 2:** Add aliens and collision detection
3. **Phase 3:** Add scoring and game states

### 1.2 Project Structure

```
alien_invasion/
├── alien_invasion.py    # Main game file
├── settings.py          # Game settings class
├── ship.py             # Ship class
├── bullet.py           # Bullet class
└── images/
    └── ship.bmp        # Ship sprite image
```

### 1.3 Installing Pygame

```bash
# Standard installation
python -m pip install --user pygame

# Alternative for Python 3
python3 -m pip install --user pygame

# macOS (if --user flag doesn't work)
python -m pip install pygame
```

---

## 2. Creating the Basic Game Window

### 2.1 Basic Pygame Window Structure

```python
# alien_invasion.py
import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()  # Initialize Pygame modules
        self.screen = pygame.display.set_mode((1200, 800))  # Create display window
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```

**Key Concepts Explained:**

1. **pygame.init():** Initializes all Pygame modules
2. **pygame.display.set_mode():** Creates the game window
   - Takes a tuple (width, height) for dimensions
   - Returns a Surface object representing the screen
3. **Event Loop:** Continuously checks for user input
4. **pygame.display.flip():** Updates the entire screen display
5. **Surface:** Pygame object representing a rectangular area where graphics can be drawn

### 2.2 Setting Background Color

```python
def __init__(self):
    # ... previous code ...
    # Set the background color (RGB values)
    self.bg_color = (230, 230, 230)  # Light gray

def run_game(self):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Fill screen with background color
        self.screen.fill(self.bg_color)
        pygame.display.flip()
```

**RGB Color System:**
- Each color component ranges from 0-255
- (255, 0, 0) = Red
- (0, 255, 0) = Green  
- (0, 0, 255) = Blue
- (230, 230, 230) = Light gray (equal mix of all colors)

---

## 3. Creating a Settings Management System

### 3.1 The Settings Class

```python
# settings.py
class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
```

### 3.2 Using Settings in Main Game

```python
# alien_invasion.py (updated)
import sys
import pygame
from settings import Settings

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
```

**Benefits of Settings Class:**
- Centralized configuration management
- Easy to modify game parameters
- Cleaner, more organized code
- Easier to maintain and debug

---

## 4. Creating and Managing the Ship

### 4.1 The Ship Class

```python
# ship.py
import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
```

**Key Concepts:**

1. **Rect Objects:** Pygame's way of handling rectangular areas
   - Contains position (x, y) and size (width, height)
   - Provides convenient positioning attributes:
     - `center`, `centerx`, `centery`
     - `top`, `bottom`, `left`, `right`
     - `midtop`, `midbottom`, `midleft`, `midright`

2. **Image Loading:** `pygame.image.load()` loads image files
3. **Blitting:** `screen.blit(source, destination)` draws one surface onto another

### 4.2 Coordinate System in Pygame

```
(0,0) -----> X-axis
  |
  |
  |
  v
Y-axis

Top-left corner is (0,0)
X increases going right
Y increases going down
```

### 4.3 Displaying the Ship

```python
# alien_invasion.py (updated)
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        # ... previous code ...
        self.ship = Ship(self)
    
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()  # Draw ship on screen
            pygame.display.flip()
```

---

## 5. Code Refactoring and Organization

### 5.1 Breaking Down the run_game() Method

**Before Refactoring:**
```python
def run_game(self):
    while True:
        # Event handling code
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # Screen updating code
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
```

**After Refactoring:**
```python
def run_game(self):
    """Start the main loop for the game."""
    while True:
        self._check_events()
        self._update_screen()

def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def _update_screen(self):
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    pygame.display.flip()
```

**Benefits of Refactoring:**
- Improved code readability
- Easier to maintain and extend
- Better separation of concerns
- Helper methods (prefixed with `_`) indicate internal use only

---

## 6. Implementing Ship Movement

### 6.1 Basic Keypress Detection

```python
def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                self.ship.rect.x += 1
```

**Key Event Types:**
- `pygame.KEYDOWN`: Key is pressed
- `pygame.KEYUP`: Key is released
- Common key constants: `pygame.K_RIGHT`, `pygame.K_LEFT`, `pygame.K_SPACE`, `pygame.K_q`

### 6.2 Continuous Movement Implementation

**Problem with Basic Method:**
- Ship only moves when key is pressed
- Not smooth or responsive for games

**Solution: Movement Flags**

```python
# ship.py (updated)
class Ship:
    def __init__(self, ai_game):
        # ... previous code ...
        # Movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1
```

```python
# alien_invasion.py (updated)
def _check_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

def run_game(self):
    while True:
        self._check_events()
        self.ship.update()  # Update ship position
        self._update_screen()
```

### 6.3 Adjustable Ship Speed

```python
# settings.py (updated)
def __init__(self):
    # ... previous settings ...
    # Ship settings
    self.ship_speed = 1.5
```

```python
# ship.py (updated for decimal positioning)
def __init__(self, ai_game):
    # ... previous code ...
    self.settings = ai_game.settings
    # Store a decimal value for the ship's horizontal position
    self.x = float(self.rect.x)

def update(self):
    """Update the ship's position based on movement flags."""
    # Update the ship's x value, not the rect
    if self.moving_right:
        self.x += self.settings.ship_speed
    if self.moving_left:
        self.x -= self.settings.ship_speed
    
    # Update rect object from self.x
    self.rect.x = self.x
```

**Why Use Decimal Values:**
- Allows for fractional movement speeds
- More precise control over game tempo
- `rect` attributes only store integers, so we need separate tracking

### 6.4 Boundary Detection

```python
def update(self):
    """Update the ship's position based on movement flags."""
    # Check boundaries before moving
    if self.moving_right and self.rect.right < self.screen_rect.right:
        self.x += self.settings.ship_speed
    if self.moving_left and self.rect.left > 0:
        self.x -= self.settings.ship_speed
    
    self.rect.x = self.x
```

**Boundary Logic:**
- `self.rect.right < self.screen_rect.right`: Ship hasn't reached right edge
- `self.rect.left > 0`: Ship hasn't reached left edge

### 6.5 Advanced Event Handling

```python
def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)

def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()  # Quit shortcut

def _check_keyup_events(self, event):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False
```

### 6.6 Fullscreen Mode

```python
def __init__(self):
    pygame.init()
    self.settings = Settings()
    
    # Fullscreen mode
    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    self.settings.screen_width = self.screen.get_rect().width
    self.settings.screen_height = self.screen.get_rect().height
    
    pygame.display.set_caption("Alien Invasion")
    self.ship = Ship(self)
```

**Important:** Always ensure you can quit (Q key) before using fullscreen mode.

---

## 7. Implementing Bullet System

### 7.1 Bullet Settings

```python
# settings.py (updated)
def __init__(self):
    # ... previous settings ...
    # Bullet settings
    self.bullet_speed = 1.0
    self.bullet_width = 3
    self.bullet_height = 15
    self.bullet_color = (60, 60, 60)  # Dark gray
    self.bullets_allowed = 3  # Maximum bullets on screen
```

### 7.2 The Bullet Class

```python
# bullet.py
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                               self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
```

**Key Concepts:**

1. **Sprite Inheritance:** Bullets inherit from `pygame.sprite.Sprite`
   - Enables group management
   - Automatic `update()` calling

2. **pygame.Rect():** Creates rectangle without an image
   - Parameters: x, y, width, height

3. **pygame.draw.rect():** Draws filled rectangle
   - Parameters: surface, color, rect

### 7.3 Managing Bullets with Groups

```python
# alien_invasion.py (updated)
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        # ... previous code ...
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()  # Updates all bullets automatically
            self._update_screen()
```

**Benefits of Sprite Groups:**
- Automatic `update()` calling for all sprites
- Efficient collision detection
- Easy add/remove operations
- List-like behavior with gaming-specific methods

### 7.4 Firing Bullets

```python
def _check_keydown_events(self, event):
    # ... previous code ...
    elif event.key == pygame.K_SPACE:
        self._fire_bullet()

def _fire_bullet(self):
    """Create a new bullet and add it to the bullets group."""
    if len(self.bullets) < self.settings.bullets_allowed:
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

def _update_screen(self):
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()
    
    # Draw all bullets
    for bullet in self.bullets.sprites():
        bullet.draw_bullet()
    
    pygame.display.flip()
```

### 7.5 Removing Old Bullets

```python
def _update_bullets(self):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions
    self.bullets.update()
    
    # Get rid of bullets that have disappeared
    for bullet in self.bullets.copy():  # Use copy() to avoid modification during iteration
        if bullet.rect.bottom <= 0:
            self.bullets.remove(bullet)

def run_game(self):
    while True:
        self._check_events()
        self.ship.update()
        self._update_bullets()  # Refactored bullet management
        self._update_screen()
```

**Important Notes:**
- Use `bullets.copy()` to iterate safely while modifying
- Remove bullets when `rect.bottom <= 0` (off-screen)
- This prevents memory leaks and performance issues

---

## 8. Complete File Structure

### 8.1 Final alien_invasion.py

```python
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()
        
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
```

### 8.2 Final settings.py

```python
class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed = 1.5
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
```

### 8.3 Final ship.py

```python
import pygame

class Ship:
    """A class to manage the ship."""
    
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        
        # Movement flags
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x
    
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
```

### 8.4 Final bullet.py

```python
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""
    
    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                               self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
    
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
```

---

## 9. Try It Yourself Exercises

### Exercise 12-1: Blue Sky
**Objective:** Create a Pygame window with blue background

**Solution:**
```python
import sys
import pygame

class BlueSky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Blue Sky")
        self.bg_color = (135, 206, 235)  # Sky blue
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    blue_sky = BlueSky()
    blue_sky.run()
```

### Exercise 12-2: Game Character
**Objective:** Display a character at screen center with matching background

**Detailed Steps:**
1. Find/create a bitmap image of a game character
2. Create a Character class similar to Ship class
3. Position character at screen center using `rect.center`
4. Match background colors

**Solution:**
```python
# character.py
import pygame

class Character:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        
        # Load character image
        self.image = pygame.image.load('images/character.bmp')
        self.rect = self.image.get_rect()
        
        # Center the character
        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

# main.py
import sys
import pygame
from character import Character

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Game Character")
        self.bg_color = (255, 255, 255)  # Match your image background
        self.character = Character(self)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.bg_color)
            self.character.blitme()
            pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()
```

### Exercise 12-3: Pygame Documentation
**Objective:** Explore Pygame documentation

**Key Areas to Explore:**
- **pygame.display:** Window management functions
- **pygame.event:** Event handling system
- **pygame.sprite:** Sprite and group management
- **pygame.image:** Image loading and manipulation
- **pygame.draw:** Drawing geometric shapes
- **pygame.font:** Text rendering capabilities

**Recommended Documentation Sections:**
1. Tutorials for beginners
2. Reference documentation for specific modules
3. Examples and code snippets
4. Performance tips and best practices

### Exercise 12-4: Rocket
**Objective:** Create a rocket that moves in all four directions

**Solution:**
```python
# rocket.py
import pygame

class Rocket:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        
        # Load rocket image
        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        
        # Start at center
        self.rect.center = self.screen_rect.center
        
        # Store position as floats
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False
    
    def update(self):
        """Update rocket position based on movement flags."""
        # Vertical movement
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        
        # Horizontal movement
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        
        # Update rect position
        self.rect.x = self.x
        self.rect.y = self.y
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

# settings.py (addition)
class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.rocket_speed = 1.5

# main game file
import sys
import pygame
from settings import Settings
from rocket import Rocket

class RocketGame:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket Game")
        
        self.rocket = Rocket(self)
    
    def run_game(self):
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        pygame.display.flip()

if __name__ == '__main__':
    game = RocketGame()
    game.run_game()
```

### Exercise 12-5: Keys
**Objective:** Display key event information to understand Pygame's key detection

**Solution:**
```python
import sys
import pygame

class KeyDetector:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Key Detector")
        self.bg_color = (255, 255, 255)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    print(f"Key pressed: {event.key}")
                    print(f"Key name: {pygame.key.name(event.key)}")
                    print(f"Unicode: {event.unicode}")
                    print("---")
            
            self.screen.fill(self.bg_color)
            pygame.display.flip()

if __name__ == '__main__':
    detector = KeyDetector()
    detector.run()
```

**Key Information Displayed:**
- `event.key`: Numeric key code
- `pygame.key.name()`: Human-readable key name
- `event.unicode`: Unicode character representation

### Exercise 12-6: Sideways Shooter
**Objective:** Create a horizontal shooting game

**Detailed Implementation:**
```python
# sideways_settings.py
class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_speed = 1.5
        
        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

# sideways_ship.py
import pygame

class SidewaysShip:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        
        # Load ship image (or create a simple rect)
        self.image = pygame.Surface((50, 30))
        self.image.fill((0, 100, 255))  # Blue ship
        self.rect = self.image.get_rect()
        
        # Position on left side, vertically centered
        self.rect.midleft = self.screen_rect.midleft
        
        # Store vertical position as float
        self.y = float(self.rect.y)
        
        # Movement flags
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update ship position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        
        self.rect.y = self.y
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

# sideways_bullet.py
import pygame
from pygame.sprite import Sprite

class SidewaysBullet(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        
        # Create bullet rect
        self.rect = pygame.Rect(0, 0, 
                               self.settings.bullet_width,
                               self.settings.bullet_height)
        self.rect.midright = game.ship.rect.midright
        
        # Store position as float
        self.x = float(self.rect.x)
    
    def update(self):
        """Move bullet to the right."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

# sideways_shooter.py (main game)
import sys
import pygame
from sideways_settings import Settings
from sideways_ship import SidewaysShip
from sideways_bullet import SidewaysBullet

class SidewaysShooter:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")
        
        self.ship = SidewaysShip(self)
        self.bullets = pygame.sprite.Group()
    
    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = SidewaysBullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        self.bullets.update()
        
        # Remove bullets that have left the screen
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen.get_rect().right:
                self.bullets.remove(bullet)
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        pygame.display.flip()

if __name__ == '__main__':
    game = SidewaysShooter()
    game.run_game()
```

---

## 10. Advanced Concepts and Best Practices

### 10.1 Game Development Patterns

**1. Game Loop Pattern:**
```python
while game_running:
    handle_input()      # Process user input
    update_game_state() # Update positions, physics, AI
    render_screen()     # Draw everything
    control_framerate() # Maintain consistent speed
```

**2. Entity-Component System:**
```python
# Instead of large monolithic classes, break into components
class Position:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Velocity:
    def __init__(self, dx, dy):
        self.dx, self.dy = dx, dy

class Renderable:
    def __init__(self, image):
        self.image = image
```

### 10.2 Performance Optimization Tips

**1. Sprite Groups for Efficiency:**
```python
# Efficient collision detection
hits = pygame.sprite.spritecollide(player, enemies, False)

# Efficient group operations
all_sprites = pygame.sprite.Group()
all_sprites.update()  # Updates all sprites at once
all_sprites.draw(screen)  # Draws all sprites efficiently
```

**2. Dirty Rectangle Updates:**
```python
# Only update changed screen areas
dirty_rects = []
for sprite in moving_sprites:
    dirty_rects.append(sprite.rect)
pygame.display.update(dirty_rects)  # More efficient than flip()
```

**3. Image Management:**
```python
# Convert images for better performance
image = pygame.image.load('sprite.png').convert_alpha()
# Use convert() for images without transparency
image = pygame.image.load('background.jpg').convert()
```

### 10.3 Code Organization Principles

**1. Single Responsibility Principle:**
- Each class should have one clear purpose
- Ship class handles ship behavior only
- Bullet class handles bullet behavior only
- Game class coordinates overall game flow

**2. Dependency Injection:**
```python
# Pass dependencies rather than creating them
class Ship:
    def __init__(self, game):  # Receive game instance
        self.screen = game.screen
        self.settings = game.settings
```

**3. Configuration Management:**
```python
# Centralize all game settings
class Settings:
    def __init__(self):
        self._load_screen_settings()
        self._load_ship_settings()
        self._load_bullet_settings()
    
    def _load_screen_settings(self):
        self.screen_width = 1200
        # etc.
```

### 10.4 Debugging Techniques

**1. Visual Debugging:**
```python
# Draw collision rectangles for debugging
if DEBUG_MODE:
    pygame.draw.rect(screen, (255, 0, 0), sprite.rect, 2)
```

**2. State Monitoring:**
```python
# Print game state information
def debug_print(self):
    print(f"Ship position: {self.ship.rect.x}, {self.ship.rect.y}")
    print(f"Bullets active: {len(self.bullets)}")
    print(f"Moving flags: R:{self.ship.moving_right} L:{self.ship.moving_left}")
```

**3. Performance Monitoring:**
```python
# Track frame rate
clock = pygame.time.Clock()
fps = 60

while running:
    dt = clock.tick(fps)  # Delta time in milliseconds
    # Use dt for frame-independent movement
    sprite.x += sprite.velocity * dt
```

### 10.5 Error Handling

**1. Image Loading:**
```python
def load_image(filename):
    try:
        image = pygame.image.load(filename).convert_alpha()
        return image
    except pygame.error as e:
        print(f"Cannot load image: {filename}")
        raise SystemExit(e)
```

**2. Sound Loading:**
```python
def load_sound(filename):
    try:
        sound = pygame.mixer.Sound(filename)
        return sound
    except pygame.error as e:
        print(f"Cannot load sound: {filename}")
        return None  # Return None for silent fallback
```

---

## 11. Common Challenges and Solutions

### 11.1 Movement Issues

**Problem:** Jerky or inconsistent movement
**Solution:** Use decimal positions and consistent time steps
```python
# Store position as float for smooth movement
self.x = float(self.rect.x)
self.x += self.speed * dt  # Use delta time
self.rect.x = int(self.x)  # Convert to integer for display
```

**Problem:** Movement tied to frame rate
**Solution:** Frame-independent movement
```python
clock = pygame.time.Clock()
dt = clock.tick(60) / 1000.0  # Delta time in seconds
position += velocity * dt
```

### 11.2 Collision Detection Problems

**Problem:** Bullets passing through fast-moving objects
**Solution:** Use swept collision detection or smaller time steps

**Problem:** Inconsistent collision boundaries
**Solution:** Adjust collision rectangles
```python
# Create smaller collision rect for more precise hits
self.collision_rect = self.rect.inflate(-10, -10)
```

### 11.3 Memory Management

**Problem:** Growing memory usage
**Solution:** Proper cleanup of unused sprites
```python
# Remove sprites that are off-screen
for sprite in group.copy():
    if sprite.rect.right < 0 or sprite.rect.left > screen_width:
        group.remove(sprite)
```

### 11.4 Input Responsiveness

**Problem:** Delayed or missed input
**Solution:** Separate input handling from game logic
```python
# Handle all events before updating game state
def handle_events(self):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            self.keys_pressed.add(event.key)
        elif event.type == pygame.KEYUP:
            self.keys_pressed.discard(event.key)

# Check key states during update
def update(self):
    if pygame.K_LEFT in self.keys_pressed:
        self.move_left()
```

---

## 12. Summary and Next Steps

### 12.1 What We've Accomplished

In this chapter, we've built the foundation of a complete game:

1. **Project Structure:** Organized code into logical modules
2. **Game Window:** Created a responsive Pygame window
3. **Settings Management:** Centralized configuration system
4. **Ship Control:** Smooth, responsive player movement
5. **Bullet System:** Projectile creation and management
6. **Code Organization:** Clean, maintainable code structure

### 12.2 Key Programming Concepts Learned

1. **Object-Oriented Design:** Classes for game entities
2. **Event-Driven Programming:** Responding to user input
3. **Game Loop:** Continuous update-render cycle
4. **Sprite Management:** Efficient group operations
5. **Collision Detection:** Boundary checking
6. **Memory Management:** Resource cleanup

### 12.3 Pygame-Specific Knowledge

1. **Surface Operations:** Blitting and drawing
2. **Event System:** Keyboard and mouse handling
3. **Coordinate System:** Screen positioning
4. **Sprite Groups:** Batch operations
5. **Rectangle Mathematics:** Position and collision
6. **Display Management:** Screen updates

### 12.4 Next Chapter Preview

In Chapter 13, we'll add:
- **Alien Fleet Creation:** Procedural enemy generation
- **Collision Detection:** Bullet-alien interactions
- **Game States:** Different phases of gameplay
- **Difficulty Progression:** Increasing challenge
- **Advanced Movement:** AI-controlled entities

### 12.5 Recommended Practice Exercises

1. **Customization:** Modify ship speed, bullet properties, colors
2. **New Features:** Add diagonal movement, multiple bullet types
3. **Visual Improvements:** Better graphics, animations, effects
4. **Sound Integration:** Add sound effects using pygame.mixer
5. **Different Game Modes:** Time trial, survival mode, etc.

### 12.6 Resources for Further Learning

1. **Official Pygame Documentation:** https://www.pygame.org/docs/
2. **Pygame Tutorials:** https://www.pygame.org/wiki/tutorials
3. **Game Development Patterns:** Research common game programming patterns
4. **Performance Optimization:** Study advanced Pygame optimization techniques
5. **Graphics and Animation:** Learn about sprite sheets and animation systems

This foundation provides everything needed to create more complex games. The modular structure makes it easy to add new features, and the patterns established here scale well to larger projects.
    
