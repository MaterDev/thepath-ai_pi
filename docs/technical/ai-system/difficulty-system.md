# Difficulty System

## Overview

The difficulty system provides basic adjustment of AI behavior using a simple scaling factor from 0.2 to 0.95.

## Core Components

### Difficulty Levels

```python
class DifficultyLevel:
    """Basic difficulty settings"""
    BEGINNER = 0.2    # Very easy, mostly random actions

    EASY = 0.4       # Basic strategy

    NORMAL = 0.6     # Balanced decisions

    HARD = 0.8      # Strong strategy

    EXPERT = 0.95    # Near-optimal play

def apply_difficulty(predictions: np.ndarray, difficulty: float) -> np.ndarray:

    """Apply difficulty scaling to model predictions"""
    # Scale predictions using temperature scaling

    # Lower difficulty = higher temperature = more random

    temperature = 1.0 / max(0.2, min(0.95, difficulty))
    scaled = predictions ** temperature

    return scaled / scaled.sum()

```

### Action Selection

```python
class ActionSelector:
    """Selects actions based on model predictions and difficulty"""
    def __init__(self, difficulty: float):
        self.difficulty = difficulty

    def select_action(self, predictions: np.ndarray) -> int:

        """Select action using scaled predictions"""
        scaled_probs = apply_difficulty(predictions, self.difficulty)
        return np.random.choice(len(scaled_probs), p=scaled_probs)

    def get_top_actions(self, predictions: np.ndarray, n: int = 3) -> List[int]:

        """Get top n actions for UI feedback"""
        scaled_probs = apply_difficulty(predictions, self.difficulty)
        return np.argsort(scaled_probs)[-n:][::-1]

```

### Basic Adaptation

```python
class DifficultyAdjuster:
    """Simple difficulty adjustment based on win/loss"""
    def __init__(self, initial_difficulty: float = 0.6):
        self.current_difficulty = initial_difficulty
        self.adjustment_rate = 0.1
        self.min_difficulty = 0.2
        self.max_difficulty = 0.95

    def adjust_after_battle(self, player_won: bool):
        """Adjust difficulty after battle"""
        if player_won:
            # Increase difficulty

            self.current_difficulty = min(
                self.max_difficulty,
                self.current_difficulty + self.adjustment_rate
            )
        else:
            # Decrease difficulty

            self.current_difficulty = max(
                self.min_difficulty,
                self.current_difficulty - self.adjustment_rate

            )

```

## Integration

```python
class BattleAI:
    """Main AI class for battles"""
    def __init__(self, model_path: str, difficulty: float = 0.6):
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.action_selector = ActionSelector(difficulty)
        self.difficulty_adjuster = DifficultyAdjuster(difficulty)

    def get_action(self, state: GameState) -> Action:

        """Get next action for battle"""
        # Get model predictions

        features = extract_features(state)
        predictions = run_inference(self.interpreter, features)

        # Select action using difficulty scaling

        action_idx = self.action_selector.select_action(predictions)
        return ACTIONS[action_idx]

    def update_difficulty(self, battle_result: bool):
        """Update difficulty after battle"""
        self.difficulty_adjuster.adjust_after_battle(battle_result)
        self.action_selector.difficulty = self.difficulty_adjuster.current_difficulty
```
