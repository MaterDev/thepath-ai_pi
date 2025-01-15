# Testing Guide

## Overview

This guide covers testing practices for The Path (AI-Pi) project:
- Unit testing
- Integration testing
- Performance testing
- AI behavior testing

## Testing Structure

```
tests/
├── unit/
│   ├── server/
│   ├── client/
│   └── ai/
├── integration/
│   ├── game_flow/
│   ├── networking/
│   └── ai_interaction/
└── performance/
    ├── load_tests/
    ├── stress_tests/
    └── ai_benchmarks/
```

## Testing Components

### 1. Unit Testing

```python
# Example test suite for AI behavior
class TestAIBehavior(unittest.TestCase):
    def setUp(self):
        """Set up test environment"""
        self.ai = AIAgent(difficulty=0.5)
        self.game_state = GameState()
    
    def test_action_selection(self):
        """Test AI action selection"""
        # Arrange
        state = self.game_state.create_test_state()
        
        # Act
        action = self.ai.select_action(state)
        
        # Assert
        self.assertIsNotNone(action)
        self.assertTrue(self.is_valid_action(action, state))
    
    def test_difficulty_scaling(self):
        """Test difficulty adjustment"""
        # Arrange
        easy_ai = AIAgent(difficulty=0.2)
        hard_ai = AIAgent(difficulty=0.8)
        state = self.game_state.create_test_state()
        
        # Act
        easy_action = easy_ai.select_action(state)
        hard_action = hard_ai.select_action(state)
        
        # Assert
        self.assertNotEqual(easy_action, hard_action)
        self.assertGreater(
            hard_ai.evaluate_action(hard_action),
            easy_ai.evaluate_action(easy_action)
        )
```

### 2. Integration Testing

```python
class TestGameFlow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.server = GameServer()
        cls.client = GameClient()
        cls.ai = AIAgent()
    
    async def test_complete_game(self):
        """Test complete game flow"""
        # Start game
        game_id = await self.server.create_game()
        await self.client.join_game(game_id)
        
        # Play through game
        while not self.server.is_game_complete(game_id):
            # Player turn
            player_action = await self.client.get_action()
            await self.server.process_action(player_action)
            
            # AI turn
            ai_action = await self.ai.get_action()
            await self.server.process_action(ai_action)
        
        # Verify game completion
        game_result = await self.server.get_game_result(game_id)
        self.assertIsNotNone(game_result.winner)
```

### 3. Performance Testing

```python
class PerformanceTester:
    """Test system performance"""
    def __init__(self):
        self.metrics = PerformanceMetrics()
    
    async def run_load_test(self,
                           num_clients: int,
                           duration: int) -> TestResults:
        """Run load test"""
        start_time = time.time()
        clients = []
        
        # Create clients
        for _ in range(num_clients):
            client = GameClient()
            await client.connect()
            clients.append(client)
        
        # Run test
        while time.time() - start_time < duration:
            for client in clients:
                action = random.choice(client.valid_actions)
                await client.send_action(action)
            
            await asyncio.sleep(0.1)
        
        # Collect results
        return self.metrics.get_results()
```

## Implementation Guidelines

For AI-assisted development:

1. **Test Case Design**
   ```python
   class TestCaseGenerator:
       """Generate test cases"""
       def generate_state_tests(self) -> List[TestCase]:
           """Generate game state test cases"""
           test_cases = []
           
           # Basic states
           test_cases.extend(self.generate_basic_states())
           
           # Edge cases
           test_cases.extend(self.generate_edge_cases())
           
           # Error cases
           test_cases.extend(self.generate_error_cases())
           
           return test_cases
       
       def generate_basic_states(self) -> List[TestCase]:
           """Generate basic test states"""
           return [
               TestCase(
                   name="new_game",
                   state=GameState.new_game(),
                   expected_valid=True
               ),
               TestCase(
                   name="mid_game",
                   state=GameState.with_history(10),
                   expected_valid=True
               ),
               TestCase(
                   name="game_over",
                   state=GameState.game_over(),
                   expected_valid=True
               )
           ]
   ```

2. **Performance Testing**
   ```python
   class PerformanceTest:
       """Test performance metrics"""
       def __init__(self):
           self.metrics = []
       
       @contextmanager
       def measure(self, name: str):
           """Measure operation performance"""
           start = time.perf_counter()
           yield
           duration = time.perf_counter() - start
           
           self.metrics.append({
               'name': name,
               'duration': duration,
               'timestamp': time.time()
           })
       
       def analyze_results(self) -> Dict[str, float]:
           """Analyze test results"""
           results = {}
           for metric in self.metrics:
               name = metric['name']
               if name not in results:
                   results[name] = []
               results[name].append(metric['duration'])
           
           return {
               name: {
                   'avg': statistics.mean(durations),
                   'max': max(durations),
                   'min': min(durations),
                   'p95': numpy.percentile(durations, 95)
               }
               for name, durations in results.items()
           }
   ```

3. **AI Testing**
   ```python
   class AITester:
       """Test AI behavior"""
       def __init__(self):
           self.ai = AIAgent()
           self.test_cases = TestCaseGenerator()
       
       def test_decision_making(self) -> TestResults:
           """Test AI decision making"""
           results = []
           
           for case in self.test_cases.generate():
               # Get AI decision
               decision = self.ai.make_decision(case.state)
               
               # Validate decision
               valid = self.validate_decision(
                   decision, case.state)
               
               # Record result
               results.append({
                   'case': case.name,
                   'decision': decision,
                   'valid': valid,
                   'expected': case.expected
               })
           
           return TestResults(results)
   ```

## Testing Best Practices

1. **Test Organization**
   ```python
   # Group related tests
   class TestAISystem(unittest.TestCase):
       """Test AI system components"""
       
       class TestBehavior(unittest.TestCase):
           """Test AI behavior"""
           pass
       
       class TestLearning(unittest.TestCase):
           """Test AI learning"""
           pass
       
       class TestPerformance(unittest.TestCase):
           """Test AI performance"""
           pass
   ```

2. **Test Utilities**
   ```python
   class TestUtils:
       """Test utilities"""
       @staticmethod
       def create_test_state(**kwargs) -> GameState:
           """Create test game state"""
           return GameState(
               round=kwargs.get('round', 1),
               players=kwargs.get('players', []),
               status=kwargs.get('status', GameStatus.ACTIVE)
           )
       
       @staticmethod
       def create_test_action(**kwargs) -> Action:
           """Create test action"""
           return Action(
               type=kwargs.get('type', ActionType.ATTACK),
               target=kwargs.get('target', None),
               parameters=kwargs.get('parameters', {})
           )
   ```

## Related Documentation
- [Server Implementation](../server/architecture.md)
- [Client Implementation](../client/architecture.md)
- [AI System](../../technical/ai-system/behavior-model.md)

## Version History
- v1.0: Initial testing guide
- v1.1: Added AI testing
- v1.2: Enhanced performance testing
