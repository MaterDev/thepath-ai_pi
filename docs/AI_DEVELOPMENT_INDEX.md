# AI Development Index

## Purpose

This document serves as a master reference for AI agents (like Windsurf) during development of The Path (AI-Pi). It provides:
1. Quick access to critical specifications
2. Documentation update guidelines
3. Implementation priorities
4. Cross-reference validation

IMPORTANT: This document should be kept in context during all development sessions.

## Development Guidelines

### AI Agent Directives
```yaml
Context_Management:
  - Keep this entire document in context during all sessions
  - Reference related documents when making changes
  - Update development log after EACH session
  - Maintain documentation alignment

Development_Log:
  location: "docs/meta/development-log.md"
  update_frequency: "After each session"
  required_sections:
    - Key Activities
    - Files Modified
    - Key Decisions
    - Insights
    - Next Steps

Documentation_Updates:
  - Cross-reference all changes
  - Maintain version alignment
  - Update related documents
  - Verify performance requirements

Quality_Standards:
  - Test coverage >80%
  - Documentation alignment
  - Performance validation
  - Code review process
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

## Implementation Priorities

### 1. Core Systems
```yaml
Priority: HIGHEST
Components:
  - Game state management
  - WebSocket communication
  - Basic AI integration
  - State serialization
Dependencies:
  - Go server
  - TypeScript client
  - Python AI system
References:
  - system-architecture.md
  - game-state.md
  - endpoints.md
```

### 2. AI Integration
```yaml
Priority: HIGH
Components:
  - Transformer model
  - Hardware acceleration
  - Difficulty system
  - State processing
Dependencies:
  - AI HAT+ setup
  - Python environment
  - Model optimization
References:
  - ai-models.md
  - behavior-model.md
  - hardware/configuration.md
```

### 3. User Interface
```yaml
Priority: HIGH
Components:
  - React components
  - Redux state
  - WebSocket client
  - Game visualization
Dependencies:
  - Node.js setup
  - TypeScript config
  - Asset pipeline
References:
  - client/architecture.md
  - api/endpoints.md
```

## Development Timeline Reference

### Phase 1 (Weeks 1-2)
```yaml
Critical_Tasks:
  setup:
    days: "1-2"
    priority: HIGHEST
    dependencies: []
  
  architecture:
    days: "3-5"
    priority: HIGHEST
    dependencies: ["setup"]
  
  game_loop:
    days: "6-8"
    priority: HIGHEST
    dependencies: ["architecture"]
  
  ai_integration:
    days: "9-10"
    priority: HIGHEST
    dependencies: ["game_loop"]

Validation_Points:
  - Repository structure
  - Development environment
  - Basic server functionality
  - WebSocket communication
  - Game state management
  - Initial AI response time
```

### Phase 2 (Weeks 3-4)
```yaml
Critical_Tasks:
  combat:
    days: "11-13"
    priority: HIGH
    dependencies: ["game_loop"]
  
  characters:
    days: "14-16"
    priority: HIGH
    dependencies: ["combat"]
  
  ai_enhancement:
    days: "17-19"
    priority: HIGH
    dependencies: ["characters"]
  
  client:
    days: "20"
    priority: HIGH
    dependencies: ["combat", "characters"]

Validation_Points:
  - Combat mechanics
  - Character system
  - AI personality system
  - Client responsiveness
```

### Phase 3 (Weeks 5-6)
```yaml
Critical_Tasks:
  enhanced_combat:
    days: "21-23"
    priority: MEDIUM
    dependencies: ["combat", "ai_enhancement"]
  
  ai_refinement:
    days: "24-26"
    priority: MEDIUM
    dependencies: ["ai_enhancement"]
  
  polish:
    days: "27-28"
    priority: MEDIUM
    dependencies: ["enhanced_combat", "ai_refinement"]
  
  launch:
    days: "29-30"
    priority: MEDIUM
    dependencies: ["polish"]

Validation_Points:
  - Advanced features
  - AI performance
  - System optimization
  - Launch readiness
```

## Task Dependencies

### Core Systems
```yaml
Dependencies:
  state_management:
    requires: ["server_setup"]
    blocks: ["game_loop"]
  
  websocket:
    requires: ["server_setup"]
    blocks: ["client_development"]
  
  ai_system:
    requires: ["hardware_setup"]
    blocks: ["combat_system"]
```

### Game Features
```yaml
Dependencies:
  combat:
    requires: ["state_management", "ai_system"]
    blocks: ["advanced_features"]
  
  characters:
    requires: ["combat"]
    blocks: ["ai_personality"]
  
  client:
    requires: ["websocket", "combat"]
    blocks: ["polish"]
```

### AI Features
```yaml
Dependencies:
  basic_ai:
    requires: ["hardware_setup", "state_management"]
    blocks: ["personality_system"]
  
  personality:
    requires: ["basic_ai", "characters"]
    blocks: ["ai_refinement"]
  
  refinement:
    requires: ["personality", "combat"]
    blocks: ["launch"]
```

## Validation Rules

### 1. Performance Checks
```yaml
Validate:
  - AI response times <= 100ms
  - Server updates <= 50ms
  - Client frames <= 16ms
  - Memory usage <= 512MB
Location: "docs/technical/hardware/monitoring.md"
```

### 2. API Consistency
```yaml
Validate:
  - WebSocket event schemas
  - REST endpoint formats
  - Error handling patterns
  - Data type definitions
Location: "docs/technical/api/endpoints.md"
```

### 3. State Management
```yaml
Validate:
  - Game state structure
  - Action validation
  - State transitions
  - Serialization
Location: "docs/technical/data-schemas/game-state.md"
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

## Project State

### Current Phase
```yaml
Phase: "Initial Setup"
Week: 1
Status: "In Progress"
Focus: "Documentation and Architecture"

Current_Priorities:
  - Establish development environment
  - Complete documentation structure
  - Define core systems
  - Plan AI integration

Recent_Changes:
  - Created AI Development Index
  - Established project scope
  - Set up documentation structure
  - Created development log
```

### Development Progress
```yaml
Documentation:
  status: "In Progress"
  completion: 80%
  next_steps:
    - Complete API specifications
    - Finalize data schemas
    - Detail hardware configuration

Implementation:
  status: "Planning"
  completion: 0%
  next_steps:
    - Set up development environment
    - Initialize core repositories
    - Configure hardware
    - Begin server implementation
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
