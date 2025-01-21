# AI Behavior Model

## Overview

The AI system uses TensorFlow Lite for efficient inference on the Raspberry Pi 5 with AI HAT+ acceleration. Training is performed on Mac Mini M1, with the trained models deployed to the Raspberry Pi.

## Core Components

1. **Model Architecture**
   - Input: Game state features
   - Output: Action probabilities
   - Format: TensorFlow Lite
   - Size: Optimized for edge deployment

2. **Decision Making**
   ```python
   class BattleAI:
       def __init__(self, model_path: str):
           self.interpreter = tf.lite.Interpreter(model_path=model_path)
           self.interpreter.allocate_tensors()
   
       def decide_action(self, state: GameState, difficulty: float) -> Action:
           """Process game state and return next action"""
           features = self.extract_features(state)
           predictions = self.run_inference(features)
           return self.select_action(predictions, difficulty)
   ```

3. **Difficulty Scaling**
   ```python
   def scale_difficulty(predictions: np.ndarray, difficulty: float) -> np.ndarray:
       """Adjust action selection based on difficulty level (0.2-0.95)"""
       # Simple temperature scaling
       return predictions ** (1.0 / difficulty)
   ```

## Training Pipeline

1. **Data Collection**
   - Battle records
   - Action outcomes
   - Win/loss statistics

2. **Training Environment**
   - Platform: Mac Mini M1
   - Framework: TensorFlow
   - Output: TFLite model

3. **Model Deployment**
   ```python
   def deploy_model(model_path: str):
       """Deploy model to Raspberry Pi"""
       interpreter = tf.lite.Interpreter(model_path=model_path)
       interpreter.allocate_tensors()
       
       # Verify model
       input_details = interpreter.get_input_details()
       output_details = interpreter.get_output_details()
       return interpreter
   ```

## State Management

1. **Feature Extraction**
   ```python
   def extract_features(state: GameState) -> np.ndarray:
       """Extract relevant features from game state"""
       features = [
           state.player.health / 100.0,
           state.opponent.health / 100.0,
           state.player.energy / 100.0,
           *encode_status_effects(state.player.status),
           *encode_status_effects(state.opponent.status)
       ]
       return np.array(features, dtype=np.float32)
   ```

2. **Action Selection**
   ```python
   def select_action(predictions: np.ndarray, difficulty: float) -> Action:
       """Select action based on model predictions and difficulty"""
       scaled = scale_difficulty(predictions, difficulty)
       action_idx = np.random.choice(len(scaled), p=scaled)
       return ACTIONS[action_idx]
   ```

## Integration

1. **WebSocket Handler**
   ```python
   class AIHandler:
       def __init__(self, model_path: str):
           self.ai = BattleAI(model_path)
           
       async def handle_turn(self, state: dict, difficulty: float):
           """Handle turn request from game server"""
           action = self.ai.decide_action(state, difficulty)
           return {'action': action.to_dict()}
   ```

2. **Performance Monitoring**
   ```python
   class AIMonitor:
       def __init__(self):
           self.inference_times = []
           
       def log_inference(self, duration: float):
           """Log inference time"""
           self.inference_times.append(duration)
   ```

### Monitoring
* Model performance metrics
* Decision confidence scores
* Response time tracking
* Resource utilization
