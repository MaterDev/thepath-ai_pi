# AI Development Index

## Purpose

This document serves as a master reference for AI agents during development of The Path (AI-Pi). It indexes essential resources and documentation across the project.

## Project Resources

### Repository Structure
```yaml
Root_Directories:
  docs: "Documentation and specifications"
  server: "Go server implementation"
  client: "TypeScript/React client"
  ai: "Python AI components"
  scripts: "Build and utility scripts"

Documentation_Structure:
  overview: "High-level project documentation"
  technical: "Technical specifications and APIs"
  implementation: "Implementation details and planning"
  meta: "Development logs and metadata"
  character_classes: "Game character specifications"
```

### Core Documentation
```yaml
Architecture:
  system_overview: "docs/overview/system-architecture.md"
  server_design: "docs/implementation/server/architecture.md"
  client_design: "docs/implementation/client/architecture.md"
  ai_design: "docs/implementation/ai/architecture.md"

Technical_Specs:
  api_endpoints: "docs/technical/api/endpoints.md"
  game_state: "docs/technical/game/state.md"
  turn_system: "docs/technical/game/turns.md"
  ai_interface: "docs/technical/ai/interface.md"
```

### System Components
```yaml
Game_State:
  components:
    - Character state management
    - Turn system
    - Combat actions
    - State synchronization
  key_docs: "docs/technical/game/state.md"

Communication:
  protocols:
    - WebSocket events
    - REST endpoints
    - State synchronization
  key_docs: "docs/technical/api/endpoints.md"

AI_System:
  components:
    - Model inference
    - Decision making
    - Hardware acceleration
    - Performance monitoring
  key_docs: "docs/technical/ai/core.md"

Game_Systems:
  components:
    - Turn management
    - Combat mechanics
    - Character classes
    - Status effects
  key_docs: "docs/technical/game/systems.md"
```

### Technical Requirements
```yaml
Performance:
  ai_response_time_max: 100ms
  server_update_time_max: 50ms
  client_frame_time_max: 16ms

Hardware:
  platform: "Raspberry Pi 5"
  ram: "8GB"
  accelerator: "AI HAT+"
  cooling: "Active"

Dependencies:
  server: "Go 1.21+"
  client: "Node.js 18+"
  ai: "Python 3.11+"
  database: "MongoDB 6+"
```

### Development Resources
```yaml
Test_Suites:
  locations:
    server: "server/tests/"
    client: "client/tests/"
    ai: "ai/tests/"
  requirements:
    coverage_minimum: 80%
    critical_coverage: 90%

Documentation_Standards:
  required_sections:
    - Purpose
    - Technical Requirements
    - Implementation Details
    - Test Coverage
    - Performance Metrics

Quality_Standards:
  code:
    - Automated linting
    - Type safety
    - Error handling
    - Performance monitoring
  testing:
    - Unit test coverage
    - Integration tests
    - Performance validation
  documentation:
    - Technical accuracy
    - Implementation alignment
    - Cross-reference validation
```

## Core Specifications

### Performance Requirements
```yaml
AI:
  response_time_max: 100ms
  memory_limit: 512MB
  difficulty_range: [0.2, 0.95]

Server:
  update_time_max: 50ms
  concurrent_games: 4
  websocket_protocol: true

Client:
  frame_time_max: 16ms
  react_redux: true
  typescript: true

Hardware:
  platform: "Raspberry Pi 5"
  ram: "8GB"
  accelerator: "AI HAT+"
  cooling: "Active"
```

### Critical Paths
```yaml
Documentation:
  overview: "docs/overview/"
  technical: "docs/technical/"
  implementation: "docs/implementation/"
  meta: "docs/meta/"

Source:
  server: "server/"
  client: "client/"
  ai: "ai/"
  scripts: "scripts/"
```

## Documentation Map

### Key Documents
```yaml
Architecture:
  system: "docs/overview/system-architecture.md"
  server: "docs/implementation/server/architecture.md"
  client: "docs/implementation/client/architecture.md"
  ai: "docs/implementation/ai/architecture.md"

APIs:
  endpoints: "docs/technical/api/endpoints.md"
  websocket: "docs/technical/api/endpoints.md#websocket-events"
  rest: "docs/technical/api/endpoints.md#rest-endpoints"

Data:
  schemas: "docs/technical/data-schemas/"
  game_state: "docs/technical/data-schemas/game-state.md"
  ai_models: "docs/technical/data-schemas/ai-models.md"

Setup:
  project: "docs/implementation/setup/project-setup.md"
  dependencies: "docs/technical/dependencies.md"
```

## Game Mechanics Reference

### Combat System
```yaml
Turn_Based:
  order: "Speed-based probability"
  actions_per_turn: 1
  reaction_system: true

Actions:
  attack:
    targeting: "Single/AOE"
    damage_types: ["Physical", "Magical", "True"]
  defend:
    duration: "Until next turn"
    bonus: "50% damage reduction"
  ability:
    cooldown: true
    resource_cost: true
    targeting: "Varied"
  item:
    inventory_limit: 6
    use_time: "1 action"

Status_Effects:
  duration: "1-5 turns"
  stacking: "Some effects"
  cleansing: "Specific abilities"
```

### Character System
```yaml
Classes:
  warrior:
    focus: "Physical damage/Tank"
    difficulty: 0.3
  mage:
    focus: "Magical damage/Control"
    difficulty: 0.7
  rogue:
    focus: "Speed/Critical hits"
    difficulty: 0.8
  support:
    focus: "Healing/Buffs"
    difficulty: 0.6

Stats:
  primary:
    - health
    - attack
    - defense
    - speed
  secondary:
    - critical_chance
    - dodge
    - resistance
    - accuracy
```

### Character Classes
```yaml
Classes:
  Conjuror:
    doc: "docs/character_classes/conjuror_bio.yml"
    role: "Damage/Control"
    theme: "Arcane manipulation and energy control"
    combat_style: "Mid-range spell weaver"
    difficulty: "Medium"

  Crystal_Vanguard:
    doc: "docs/character_classes/crystal_vanguard_bio.yml"
    role: "Tank/Support"
    theme: "Crystal-based defense and protection"
    combat_style: "Frontline protector"
    difficulty: "Low"

  Zealot:
    doc: "docs/character_classes/zealot_bio.yml"
    role: "Damage/Mobility"
    theme: "Fanatical combat prowess"
    combat_style: "Aggressive skirmisher"
    difficulty: "High"

  Wraithwood_Seer:
    doc: "docs/character_classes/wraithwood_seer_bio.yml"
    role: "Support/Control"
    theme: "Natural magic and foresight"
    combat_style: "Tactical support"
    difficulty: "Medium"

  Primal_Shifter:
    doc: "docs/character_classes/primal_shifter_bio.yml"
    role: "Tank/Damage"
    theme: "Bestial transformation"
    combat_style: "Adaptable warrior"
    difficulty: "High"

  The_Blessed:
    doc: "docs/character_classes/the_blessed_bio.yml"
    role: "Support/Utility"
    theme: "Divine blessings and protection"
    combat_style: "Strategic enabler"
    difficulty: "Medium"

Class_System:
  doc_root: "docs/character_classes/"
  balance_considerations:
    - Each class must have clear strengths and weaknesses
    - Roles should complement each other in team composition
    - Difficulty ratings affect AI behavior adaptation
    - Combat styles should enable diverse strategies

  class_relationships:
    strong_against:
      Conjuror: ["The_Blessed", "Wraithwood_Seer"]
      Crystal_Vanguard: ["Conjuror", "Zealot"]
      Zealot: ["The_Blessed", "Primal_Shifter"]
      Wraithwood_Seer: ["Primal_Shifter", "Crystal_Vanguard"]
      Primal_Shifter: ["Conjuror", "The_Blessed"]
      The_Blessed: ["Crystal_Vanguard", "Wraithwood_Seer"]
```

### AI Behavior Patterns

### Personality Types
```yaml
Aggressive:
  attack_priority: 0.8
  defense_priority: 0.2
  risk_taking: 0.7

Defensive:
  attack_priority: 0.3
  defense_priority: 0.8
  risk_taking: 0.2

Balanced:
  attack_priority: 0.5
  defense_priority: 0.5
  risk_taking: 0.5

Strategic:
  attack_priority: 0.6
  defense_priority: 0.6
  risk_taking: 0.4
```

### Learning Parameters
```yaml
Adaptation:
  rate: 0.1
  window_size: 10
  metrics:
    - player_health
    - damage_dealt
    - survival_time
    - objective_completion

Pattern_Recognition:
  features:
    - action_sequences
    - resource_management
    - positioning
    - target_selection
  
Response_Adjustment:
  confidence_threshold: 0.7
  exploration_rate: 0.2
  memory_length: 50
```

## Testing Requirements

### Unit Tests
```yaml
Coverage:
  server: ">= 80%"
  client: ">= 75%"
  ai: ">= 85%"

Critical_Paths:
  - State management
  - Action validation
  - AI decisions
  - Network handling
```

### Integration Tests
```yaml
Scenarios:
  - Full game flow
  - AI adaptation
  - Network resilience
  - State synchronization

Performance_Tests:
  - Response times
  - Memory usage
  - Concurrent games
  - Hardware utilization
```

### User Acceptance
```yaml
Criteria:
  - Response time feels instant
  - AI behavior feels natural
  - UI is intuitive
  - Game is engaging

Metrics:
  - User session length
  - Return rate
  - Completion rate
  - Difficulty satisfaction
```

## Development Workflow

### Feature Implementation
```yaml
Steps:
  1: Review specifications
  2: Update documentation
  3: Implement tests
  4: Develop feature
  5: Validate performance
  6: Update AI index

Validation:
  - Performance requirements
  - API consistency
  - Documentation alignment
  - Test coverage
```

### Code Review Process
```yaml
Checklist:
  - Documentation updated
  - Tests added
  - Performance validated
  - API consistency
  - Error handling
  - Security checks

Priority:
  critical:
    - State management
    - AI behavior
    - Network code
  high:
    - UI components
    - Game logic
    - Data handling
```

## Security Considerations

### Data Protection
```yaml
Sensitive_Data:
  - Player credentials
  - Game statistics
  - AI training data
  - Performance metrics

Encryption:
  websocket: "TLS 1.3"
  storage: "AES-256"
  api: "HTTPS only"
```

### Access Control
```yaml
Authentication:
  method: "JWT"
  expiry: "24h"
  refresh: true

Authorization:
  roles:
    - player
    - admin
    - system
  scope_based: true
```

## Error Recovery

### Failure Modes
```yaml
Network:
  - Connection loss
  - High latency
  - Packet loss
  - State desync

Hardware:
  - Memory exhaustion
  - CPU throttling
  - Storage limits
  - Temperature limits

Recovery:
  - State restoration
  - Graceful degradation
  - Auto-reconnect
  - Data consistency
```

### Monitoring
```yaml
Metrics:
  - Response times
  - Error rates
  - Resource usage
  - User engagement

Alerts:
  performance:
    ai_response: "> 100ms"
    server_update: "> 50ms"
    client_frame: "> 16ms"
  hardware:
    memory: "> 80%"
    cpu: "> 80%"
    temperature: "> 80°C"
```

## Quick Reference

### Critical Limits
```yaml
AI:
  response: 100ms
  memory: 512MB
  difficulty: [0.2, 0.95]

Server:
  updates: 50ms
  memory: 512MB
  concurrent: 4

Client:
  frames: 16ms
  memory: 256MB
```

### Key Paths
```yaml
Docs: "docs/"
Server: "server/"
Client: "client/"
AI: "ai/"
```

### Main APIs
```yaml
WebSocket: "/game"
REST: "/api/v1"
AI: "/ai/v1"
```

## Related Documentation
- [Project Scope](docs/overview/project-scope.md)
- [System Architecture](docs/overview/system-architecture.md)
- [API Endpoints](docs/technical/api/endpoints.md)
- [Setup Guide](docs/implementation/setup/project-setup.md)
