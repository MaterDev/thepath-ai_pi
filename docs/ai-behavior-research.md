# AI Behavior Specification

## Decision Making System

### Core AI Structure
```python
class AIAgent:
    def __init__(self, difficulty: float, personality: str):
        self.difficulty = difficulty
        self.personality = personality
        self.strategy = self._load_strategy()
        self.model = self._initialize_model()

    def make_decision(self, game_state: dict) -> Action:
        valid_actions = self._get_valid_actions(game_state)
        action_scores = self._evaluate_actions(valid_actions, game_state)
        return self._select_action(action_scores)
```

### State Evaluation
```python
class StateEvaluator:
    def evaluate_state(self, state: dict) -> float:
        metrics = {
            'health_ratio': self._calculate_health_ratio(state),
            'position_score': self._evaluate_positions(state),
            'threat_level': self._assess_threats(state),
            'opportunity_score': self._identify_opportunities(state)
        }
        return self._combine_metrics(metrics)

    def _calculate_health_ratio(self, state: dict) -> float:
        team_health = sum(c['stats']['health'] for c in state['allies'])
        team_max_health = sum(c['stats']['maxHealth'] for c in state['allies'])
        return team_health / team_max_health

    def _assess_threats(self, state: dict) -> float:
        threat_scores = []
        for enemy in state['enemies']:
            damage_potential = enemy['stats']['attack'] * max(a['power'] for a in enemy['abilities'])
            threat_scores.append(damage_potential * (enemy['stats']['health'] / enemy['stats']['maxHealth']))
        return sum(threat_scores)
```

## Strategic Patterns

### Difficulty Levels
```python
DIFFICULTY_PROFILES = {
    'BEGINNER': {
        'randomness': 0.4,
        'optimization': 0.3,
        'aggression': 0.4,
        'defensive_threshold': 0.7
    },
    'NORMAL': {
        'randomness': 0.2,
        'optimization': 0.6,
        'aggression': 0.6,
        'defensive_threshold': 0.5
    },
    'HARD': {
        'randomness': 0.1,
        'optimization': 0.8,
        'aggression': 0.7,
        'defensive_threshold': 0.4
    },
    'EXPERT': {
        'randomness': 0.05,
        'optimization': 0.95,
        'aggression': 0.8,
        'defensive_threshold': 0.3
    }
}
```

### Personality Traits
```python
PERSONALITY_TRAITS = {
    'AGGRESSIVE': {
        'attack_weight': 1.5,
        'defense_weight': 0.7,
        'positioning_weight': 0.8,
        'risk_tolerance': 0.8
    },
    'DEFENSIVE': {
        'attack_weight': 0.7,
        'defense_weight': 1.5,
        'positioning_weight': 1.2,
        'risk_tolerance': 0.4
    },
    'BALANCED': {
        'attack_weight': 1.0,
        'defense_weight': 1.0,
        'positioning_weight': 1.0,
        'risk_tolerance': 0.6
    }
}
```

## Action Selection

### Priority System
```python
class ActionPrioritizer:
    def __init__(self, difficulty: float, personality: dict):
        self.difficulty = difficulty
        self.personality = personality
        
    def prioritize_actions(self, actions: list, state: dict) -> list:
        scored_actions = []
        for action in actions:
            base_score = self._calculate_base_score(action, state)
            personality_mod = self._apply_personality(base_score, action)
            difficulty_mod = self._apply_difficulty(personality_mod, action)
            scored_actions.append((action, difficulty_mod))
        return sorted(scored_actions, key=lambda x: x[1], reverse=True)

    def _calculate_base_score(self, action: dict, state: dict) -> float:
        if action['type'] == 'ABILITY':
            return self._score_ability(action, state)
        elif action['type'] == 'MOVE':
            return self._score_movement(action, state)
        return self._score_default_action(action, state)
```

### Target Selection
```python
class TargetSelector:
    def select_target(self, state: dict, action: dict) -> str:
        targets = self._get_valid_targets(state, action)
        scored_targets = []
        for target in targets:
            base_score = self._calculate_target_score(target, state)
            tactical_score = self._evaluate_tactical_value(target, state)
            final_score = base_score * tactical_score
            scored_targets.append((target['id'], final_score))
        return max(scored_targets, key=lambda x: x[1])[0]

    def _calculate_target_score(self, target: dict, state: dict) -> float:
        return {
            'health_ratio': target['stats']['health'] / target['stats']['maxHealth'],
            'threat_level': self._calculate_threat_level(target),
            'vulnerability': self._assess_vulnerability(target),
            'strategic_value': self._evaluate_strategic_value(target, state)
        }
```

## Model Integration

### State Representation
```python
def create_state_tensor(game_state: dict) -> torch.Tensor:
    # Character features
    char_features = []
    for char in game_state['characters'].values():
        features = [
            char['stats']['health'] / char['stats']['maxHealth'],
            char['stats']['attack'] / 100,
            char['stats']['defense'] / 100,
            char['stats']['speed'] / 100,
            len(char['status']['effects']) / 10
        ]
        char_features.extend(features)
    
    # Global state features
    global_features = [
        game_state['round'] / 100,
        len(game_state['timeline']) / 10,
        len(game_state['statusEffects']) / 10
    ]
    
    return torch.tensor(char_features + global_features)
```

### Action Encoding
```python
def encode_action(action: dict) -> torch.Tensor:
    action_type_encoding = {
        'ABILITY': [1, 0, 0, 0],
        'MOVE': [0, 1, 0, 0],
        'WAIT': [0, 0, 1, 0],
        'DEFEND': [0, 0, 0, 1]
    }
    
    encoding = action_type_encoding[action['type']]
    
    if action['type'] == 'ABILITY':
        ability_features = [
            action['ability']['power'] / 100,
            len(action['ability']['effects']) / 5
        ]
        encoding.extend(ability_features)
    
    return torch.tensor(encoding)
```

## Performance Monitoring

### Metrics Collection
```python
class AIPerformanceMonitor:
    def __init__(self):
        self.metrics = {
            'decision_times': [],
            'action_confidence': [],
            'state_evaluation_times': [],
            'prediction_accuracy': []
        }
    
    def record_decision(self, decision_time: float, confidence: float):
        self.metrics['decision_times'].append(decision_time)
        self.metrics['action_confidence'].append(confidence)
    
    def calculate_metrics(self) -> dict:
        return {
            'avg_decision_time': np.mean(self.metrics['decision_times']),
            'avg_confidence': np.mean(self.metrics['action_confidence']),
            'confidence_std': np.std(self.metrics['action_confidence']),
            'performance_consistency': self._calculate_consistency()
        }
```

## Implementation Notes

### Optimization Requirements
- Decision time < 500ms
- Model inference < 100ms
- State evaluation < 50ms

### Memory Management
- Cache frequently used state evaluations
- Limit decision tree depth based on difficulty
- Prune invalid actions early