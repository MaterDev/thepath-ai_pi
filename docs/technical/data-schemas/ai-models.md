# AI Model Schemas

## Overview

This document defines the data structures used for AI model training and inference. The system uses TensorFlow Lite for deployment on Raspberry Pi, with training done on Mac Mini M1.

## Model Input

```python
@dataclass
class BattleFeatures:
    """Features extracted from battle state"""
    # Player features
    player_health: float      # Normalized (0-1)
    player_energy: float      # Normalized (0-1)
    player_statuses: List[int] # One-hot encoded
    
    # AI features
    ai_health: float         # Normalized (0-1)
    ai_energy: float        # Normalized (0-1)
    ai_statuses: List[int]  # One-hot encoded
    
    # Battle context
    round: int             # Current round
    turns_taken: int       # Turns in current round
    
    def to_array(self) -> np.ndarray:
        """Convert to model input array"""
        return np.array([
            self.player_health,
            self.player_energy,
            *self.player_statuses,
            self.ai_health,
            self.ai_energy,
            *self.ai_statuses,
            self.round / 20.0,  # Normalize round
            self.turns_taken / 2.0  # Normalize turns
        ])
```

## Model Output

```python
@dataclass
class ActionPrediction:
    """Model prediction for next action"""
    action_probs: np.ndarray  # Probability per action
    
    def get_action(self, difficulty: float) -> int:
        """Get action index using difficulty scaling"""
        # Apply temperature scaling
        temperature = 1.0 / max(0.2, min(0.95, difficulty))
        scaled = self.action_probs ** temperature
        scaled /= scaled.sum()
        
        # Sample action
        return np.random.choice(len(scaled), p=scaled)
    
    def get_top_k(self, k: int = 3) -> List[Tuple[int, float]]:
        """Get top k actions and probabilities"""
        indices = np.argsort(self.action_probs)[-k:][::-1]
        return [(i, self.action_probs[i]) for i in indices]
```

## Training Data

```python
@dataclass
class TrainingExample:
    """Single training example"""
    features: np.ndarray     # Input features
    action: int             # Chosen action
    reward: float          # Battle outcome
    
    def to_tf_data(self) -> Tuple[np.ndarray, np.ndarray]:
        """Convert to TensorFlow training data"""
        return self.features, np.array([self.action])

class TrainingDataset:
    """Collection of training examples"""
    def __init__(self, max_size: int = 10000):
        self.examples: List[TrainingExample] = []
        self.max_size = max_size
    
    def add(self, example: TrainingExample):
        """Add example to dataset"""
        self.examples.append(example)
        if len(self.examples) > self.max_size:
            self.examples.pop(0)
    
    def to_tf_dataset(self) -> tf.data.Dataset:
        """Convert to TensorFlow dataset"""
        features = np.array([ex.features for ex in self.examples])
        actions = np.array([ex.action for ex in self.examples])
        return tf.data.Dataset.from_tensor_slices((features, actions))
```

## Model Configuration

```python
@dataclass
class ModelConfig:
    """TensorFlow Lite model configuration"""
    input_size: int = 16     # Feature vector size
    hidden_size: int = 64    # Hidden layer size
    output_size: int = 3     # Number of actions
    
    def create_model(self) -> tf.keras.Model:
        """Create TensorFlow model"""
        return tf.keras.Sequential([
            tf.keras.layers.Dense(self.hidden_size, activation='relu'),
            tf.keras.layers.Dense(self.output_size, activation='softmax')
        ])

@dataclass
class TrainingConfig:
    """Training configuration"""
    batch_size: int = 32
    epochs: int = 10
    learning_rate: float = 0.001
    validation_split: float = 0.2
    
    def get_optimizer(self) -> tf.keras.optimizers.Optimizer:
        """Get TensorFlow optimizer"""
        return tf.keras.optimizers.Adam(learning_rate=self.learning_rate)
```

## Model Export

```python
def export_for_pi(model: tf.keras.Model, path: str):
    """Export model for Raspberry Pi"""
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    converter.target_spec.supported_types = [tf.float32]
    
    tflite_model = converter.convert()
    with open(path, 'wb') as f:
        f.write(tflite_model)

class ModelDeployer:
    """Deploy and run model on Raspberry Pi"""
    def __init__(self, model_path: str):
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
    
    def predict(self, features: np.ndarray) -> ActionPrediction:
        """Run inference on Pi"""
        self.interpreter.set_tensor(
            self.input_details[0]['index'],
            features.reshape(1, -1)
        )
        
        self.interpreter.invoke()
        
        probs = self.interpreter.get_tensor(
            self.output_details[0]['index']
        )[0]
        
        return ActionPrediction(probs)
