# Chapter 14: Scoring - Complete Study Guide

## Chapter Overview
This chapter completes the Alien Invasion game by adding:
- A Play button for game control
- Progressive difficulty (speed increases per level)
- Comprehensive scoring system
- Visual feedback (high scores, levels, ship count)

---

## Part 1: Adding the Play Button

### 1.1 Concept: Game State Management
**Purpose**: Control when the game is active vs inactive, allowing players to start/restart games on demand.

**Key Changes to GameStats**:
```python
def __init__(self, ai_game):
    """Initialize statistics."""
    self.settings = ai_game.settings
    self.reset_stats()
    # Start game in an inactive state.
    self.game_active = False
```

**Why This Works**: 
- Game starts paused instead of immediately active
- Provides clear separation between menu and gameplay states
- Allows for proper game initialization before play begins

### 1.2 Creating the Button Class

**Complete Button Implementation** (`button.py`):

```python
import pygame.font

class Button:
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)  # Bright green
        self.text_color = (255, 255, 255)  # White text
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # The button message needs to be prepped only once.
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                        self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
```

**Key Concepts Explained**:

1. **Font Rendering**: `font.render()` converts text to images
   - `True` parameter enables antialiasing (smoother text edges)
   - Background color makes text stand out against button

2. **Rect Positioning**: Using `center` attribute for automatic positioning
   - `self.rect.center = self.screen_rect.center` centers button on screen
   - `self.msg_image_rect.center = self.rect.center` centers text on button

3. **Drawing Process**: Two-step drawing (background then text)
   - `screen.fill()` draws the colored rectangle
   - `screen.blit()` overlays the text image

### 1.3 Integrating the Button

**In AlienInvasion.__init__()**:
```python
# Make the Play button.
self.play_button = Button(self, "Play")
```

**In AlienInvasion._update_screen()**:
```python
# Draw the play button if the game is inactive.
if not self.stats.game_active:
    self.play_button.draw_button()
```

**Why Conditional Drawing**: Button only appears when game is inactive, preventing visual clutter during gameplay.

### 1.4 Mouse Event Handling

**Mouse Click Detection**:
```python
def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # existing code...
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            self._check_play_button(mouse_pos)
```

**Button Click Processing**:
```python
def _check_play_button(self, mouse_pos):
    """Start a new game when the player clicks Play."""
    if self.play_button.rect.collidepoint(mouse_pos):
        self.stats.game_active = True
```

**Concept Explanation**:
- `pygame.mouse.get_pos()` returns (x, y) coordinates of click
- `collidepoint()` checks if click coordinates are within button rectangle
- Only activates game if click is specifically on the button

### 1.5 Game Reset Functionality

**Complete Reset Implementation**:
```python
def _check_play_button(self, mouse_pos):
    """Start a new game when the player clicks Play."""
    button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not self.stats.game_active:
        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True
        
        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()
        
        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()
        
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
```

**Why Each Step is Necessary**:
1. **Statistics Reset**: Restores player lives, score, etc.
2. **Sprite Cleanup**: Removes old game objects that could interfere
3. **Fresh Start**: Creates new fleet and centers ship
4. **UI Enhancement**: Hides cursor for better gameplay experience

### 1.6 Advanced Button Behavior

**Preventing Accidental Clicks**:
```python
button_clicked = self.play_button.rect.collidepoint(mouse_pos)
if button_clicked and not self.stats.game_active:
    # Start game logic...
```

**Cursor Management**:
```python
# Hide cursor when game starts
pygame.mouse.set_visible(False)

# Show cursor when game ends (in _ship_hit method)
self.stats.game_active = False
pygame.mouse.set_visible(True)
```

---

## Exercises for Part 1

### Exercise 14-1: Press P to Play
**Objective**: Add keyboard alternative to mouse click.

**Implementation Strategy**:
1. Create `_start_game()` method containing game reset logic
2. Call `_start_game()` from both `_check_play_button()` and `_check_keydown_events()`
3. Add P key detection in `_check_keydown_events()`

**Sample Solution Structure**:
```python
def _start_game(self):
    """Start a new game."""
    self.stats.reset_stats()
    self.stats.game_active = True
    # ... rest of reset logic

def _check_keydown_events(self, event):
    # ... existing key handling
    elif event.key == pygame.K_p and not self.stats.game_active:
        self._start_game()
```

### Exercise 14-2: Target Practice
**Objective**: Create a simplified shooting game with moving target.

**Key Components Needed**:
1. **Moving Target**: Rectangle that moves up/down at screen edge
2. **Ship Control**: Player ship that moves vertically
3. **Collision Detection**: Bullet hits target
4. **Miss Counter**: Track missed shots, end game after 3 misses
5. **Play Button**: Restart functionality

**Implementation Outline**:
```python
class Target:
    def __init__(self):
        self.rect = pygame.Rect(screen_width-50, 0, 30, 50)
        self.direction = 1  # 1 for down, -1 for up
        self.speed = 2
    
    def update(self):
        self.rect.y += self.speed * self.direction
        if self.rect.top <= 0 or self.rect.bottom >= screen_height:
            self.direction *= -1
```

---

## Part 2: Leveling Up (Progressive Difficulty)

### 2.1 Concept: Dynamic Settings

**Problem**: Static difficulty makes games boring after initial challenge.

**Solution**: Separate static settings from dynamic ones that change during gameplay.

### 2.2 Reorganizing Settings Class

**Updated Settings Structure**:
```python
class Settings:
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # Alien settings
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
```

**Design Benefits**:
1. **Clear Separation**: Static vs dynamic settings are distinct
2. **Easy Reset**: `initialize_dynamic_settings()` resets speeds for new games
3. **Scalable Difficulty**: `speedup_scale` controls difficulty progression
4. **Maintainable**: Easy to add new dynamic settings

### 2.3 Implementing Speed Increases

**Triggering Speed Increase**:
```python
def _check_bullet_alien_collisions(self):
    # ... collision detection code ...
    
    if not self.aliens:
        # Destroy existing bullets and create new fleet.
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()
```

**Why This Location**: Speed increases when player clears entire fleet, marking level completion.

### 2.4 Resetting Speeds for New Games

**In Play Button Handler**:
```python
def _check_play_button(self, mouse_pos):
    button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not self.stats.game_active:
        # Reset the game settings.
        self.settings.initialize_dynamic_settings()
        # ... rest of reset logic
```

**Critical Concept**: Without this reset, new games would start at the previous game's difficulty level.

---

## Exercises for Part 2

### Exercise 14-3: Challenging Target Practice
**Enhancement**: Apply speed progression to target practice game.

**Implementation Ideas**:
```python
def increase_difficulty(self):
    """Make target move faster and bullets slower."""
    self.target_speed *= 1.2
    self.bullet_speed *= 0.95  # Make bullets slightly slower
```

### Exercise 14-4: Difficulty Levels
**Objective**: Add multiple difficulty buttons (Easy, Medium, Hard).

**Implementation Strategy**:
1. Create multiple buttons with different labels
2. Set different initial values for each difficulty
3. Store difficulty choice and apply appropriate settings

**Sample Difficulty Settings**:
```python
DIFFICULTIES = {
    'easy': {'alien_speed': 0.5, 'speedup_scale': 1.05},
    'medium': {'alien_speed': 1.0, 'speedup_scale': 1.1},
    'hard': {'alien_speed': 1.5, 'speedup_scale': 1.2}
}
```

---

## Part 3: Comprehensive Scoring System

### 3.1 Core Scoring Concepts

**Score as Game Statistic**:
```python
# In GameStats.reset_stats()
def reset_stats(self):
    """Initialize statistics that can change during the game."""
    self.ships_left = self.settings.ship_limit
    self.score = 0  # Initialize in reset_stats, not __init__
```

**Why reset_stats()**: Score should reset for each new game, unlike high score which persists.

### 3.2 Scoreboard Class Architecture

**Complete Scoreboard Implementation**:
```python
import pygame.font

class Scoreboard:
    """A class to report scoring information."""
    
    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image.
        self.prep_score()
    
    def prep_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True,
                                          self.text_color, self.settings.bg_color)
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
```

**Key Design Principles**:
1. **Separation of Concerns**: Scoreboard only handles display, not game logic
2. **Text Rendering**: Convert numbers to images for screen display
3. **Positioning Strategy**: Use rect attributes for consistent placement

### 3.3 Live Score Updates

**Scoring When Aliens Are Hit**:
```python
# In Settings.initialize_dynamic_settings()
self.alien_points = 50

# In AlienInvasion._check_bullet_alien_collisions()
if collisions:
    for aliens in collisions.values():
        self.stats.score += self.settings.alien_points * len(aliens)
    self.sb.prep_score()
```

**Advanced Collision Handling**:
The `collisions.values()` loop ensures all aliens hit by any bullet are scored:
- Each bullet becomes a key in the collisions dictionary
- Each value is a list of aliens hit by that bullet
- Wide bullets or multiple simultaneous hits are properly scored

### 3.4 Score Formatting and Display

**Professional Score Formatting**:
```python
def prep_score(self):
    """Turn the score into a rendered image."""
    rounded_score = round(self.stats.score, -1)  # Round to nearest 10
    score_str = "{:,}".format(rounded_score)     # Add comma separators
    self.score_image = self.font.render(score_str, True,
                                      self.text_color, self.settings.bg_color)
```

**Formatting Benefits**:
- `round(score, -1)`: Rounds to nearest 10 (arcade-style scoring)
- `"{:,}".format()`: Adds commas (1,000 instead of 1000)
- Professional appearance matches commercial games

### 3.5 High Score System

**Persistent High Score**:
```python
# In GameStats.__init__() - not reset_stats()!
def __init__(self, ai_game):
    # ... other initialization ...
    # High score should never be reset.
    self.high_score = 0

# In Scoreboard
def prep_high_score(self):
    """Turn the high score into a rendered image."""
    high_score = round(self.stats.high_score, -1)
    high_score_str = "{:,}".format(high_score)
    self.high_score_image = self.font.render(high_score_str, True,
                                           self.text_color, self.settings.bg_color)
    
    # Center the high score at the top of the screen.
    self.high_score_rect = self.high_score_image.get_rect()
    self.high_score_rect.centerx = self.screen_rect.centerx
    self.high_score_rect.top = self.score_rect.top

def check_high_score(self):
    """Check to see if there's a new high score."""
    if self.stats.score > self.stats.high_score:
        self.stats.high_score = self.stats.score
        self.prep_high_score()
```

**High Score Logic**:
1. **Persistence**: Stored in `__init__()`, not reset between games
2. **Positioning**: Centered at top of screen for prominence
3. **Live Updates**: Checked after every alien hit

### 3.6 Progressive Point Values

**Increasing Alien Values**:
```python
class Settings:
    def __init__(self):
        # ... other settings ...
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
    
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
```

**Balancing Considerations**:
- `speedup_scale = 1.1`: Modest speed increase maintains playability
- `score_scale = 1.5`: Larger point increase rewards higher difficulty
- `int()` conversion: Keeps point values as whole numbers

### 3.7 Level Display System

**Level Tracking and Display**:
```python
# In GameStats.reset_stats()
self.level = 1

# In Scoreboard.prep_level()
def prep_level(self):
    """Turn the level into a rendered image."""
    level_str = str(self.stats.level)
    self.level_image = self.font.render(level_str, True,
                                      self.text_color, self.settings.bg_color)
    
    # Position the level below the score.
    self.level_rect = self.level_image.get_rect()
    self.level_rect.right = self.score_rect.right
    self.level_rect.top = self.score_rect.bottom + 10
```

**Level Advancement**:
```python
# In _check_bullet_alien_collisions() when fleet is destroyed
self.stats.level += 1
self.sb.prep_level()
```

### 3.8 Visual Ship Counter

**Ship as Sprite**:
```python
# Modified Ship class
class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()  # Initialize Sprite
        # ... rest of ship initialization
```

**Ship Display Group**:
```python
def prep_ships(self):
    """Show how many ships are left."""
    self.ships = Group()
    for ship_number in range(self.stats.ships_left):
        ship = Ship(self.ai_game)
        ship.rect.x = 10 + ship_number * ship.rect.width
        ship.rect.y = 10
        self.ships.add(ship)
```

**Visual Benefits**:
- Intuitive representation (ship icons = ship lives)
- No need for text labels
- Matches classic arcade game conventions

---

## Exercises for Part 3

### Exercise 14-5: All-Time High Score
**Objective**: Persist high score to file.

**Implementation Strategy**:
```python
import json

def save_high_score(self):
    """Save high score to file."""
    with open('high_score.json', 'w') as f:
        json.dump({'high_score': self.high_score}, f)

def load_high_score(self):
    """Load high score from file."""
    try:
        with open('high_score.json', 'r') as f:
            data = json.load(f)
            return data['high_score']
    except FileNotFoundError:
        return 0
```

### Exercise 14-6: Refactoring
**Objective**: Improve code organization.

**Refactoring Opportunities**:
1. **Method Extraction**: Move level-up logic from `_check_bullet_alien_collisions()` to `_start_new_level()`
2. **Initialization Grouping**: Create `prep_images()` method in Scoreboard
3. **Common Functionality**: Extract game start logic to reusable method

**Benefits of Refactoring**:
- Improved readability
- Easier maintenance
- Better code reuse
- Clearer method responsibilities

### Exercise 14-7: Expanding the Game
**Enhancement Ideas**:

1. **Alien Bullets**:
   ```python
   class AlienBullet(Sprite):
       def __init__(self, alien):
           # Create downward-moving bullets
   ```

2. **Destructible Shields**:
   ```python
   class Shield(Sprite):
       def __init__(self, position):
           # Create shield blocks that can be destroyed
   ```

3. **Sound Effects**:
   ```python
   import pygame.mixer
   
   # Load sounds
   self.shoot_sound = pygame.mixer.Sound('shoot.wav')
   self.explosion_sound = pygame.mixer.Sound('explosion.wav')
   ```

### Exercise 14-8: Sideways Shooter Final Version
**Objective**: Apply all concepts to sideways-scrolling variant.

**Key Adaptations**:
- Horizontal alien movement
- Different bullet directions
- Modified collision detection
- Adapted scoring system

---

## Chapter Summary

### Key Concepts Mastered:

1. **Game State Management**: Controlling when games are active/inactive
2. **User Interface Design**: Creating interactive buttons and displays
3. **Event Handling**: Processing mouse clicks and keyboard input
4. **Progressive Difficulty**: Dynamically adjusting game parameters
5. **Comprehensive Scoring**: Points, levels, high scores, and visual feedback
6. **Code Organization**: Separating concerns and maintaining clean architecture

### Technical Skills Developed:

1. **Pygame Text Rendering**: Converting text to images for display
2. **Mouse Input Processing**: Detecting clicks and coordinate handling
3. **Sprite Groups**: Managing collections of game objects
4. **File I/O**: Saving and loading persistent data
5. **Mathematical Operations**: Scaling values and formatting numbers
6. **Class Design**: Creating cohesive, single-purpose classes

### Game Development Principles:

1. **User Experience**: Hiding cursors, clear visual feedback
2. **Professional Polish**: Formatted scores, proper positioning
3. **Accessibility**: Multiple input methods (mouse and keyboard)
4. **Engagement**: Progressive difficulty and scoring incentives
5. **Code Quality**: Refactoring and organizing for maintainability

This comprehensive scoring system transforms a simple game into a polished, engaging experience that encourages replayability and provides clear progression feedback to players.
