# Combat System Balance and Meta

## Overview

This document outlines the core principles and considerations for balancing The Path's combat system, drawing from game balance theory by Ian Schreiber and Brenda Romero. It covers character design, combat mechanics, testing methodologies, and meta-game considerations.

## Character Class Design

### Core Design Principles

#### Unique Mechanics
* Each class must have distinctive mechanics that define their playstyle
* Mechanics can include:
    * Unique resource management
    * Special ability interactions
    * Modified combat rules
* Mechanics should feel natural to the class theme

#### Role Versatility
* Classes should have primary roles with multiple specializations
* Example specializations for tank role:
    * Crowd control focus
    * Damage mitigation
    * Self-healing capabilities
* Versatility prevents one-dimensional gameplay

#### Synergies and Counters
* Design natural synergies between classes
* Implement soft counters, not hard shutdowns
* Base interactions on:
    * Damage types
    * Buff/debuff systems
    * Resource management
* Maintain strategic options even in unfavorable matchups

#### Ability Cost Curves
* Base costs for standard effects (damage/healing)
* Additional costs for:
    * Special effects
    * Range increases
    * Area of effect
* Cost-to-benefit ratio should scale appropriately

## Combat System Mechanics

### Fundamental Pillars

#### Core Elements
* Genre: Turn-based tactical combat
* Time: Strategic planning between turns
* Pacing: Balanced action economy
* Feel: Impactful abilities with clear feedback
* Participants: Solo and team scenarios
* Progression: Character growth and mastery
* Volume: Encounter frequency and duration

#### Combat Feel vs Mathematical Balance
* Subjective feel must align with objective balance
* Consider:
    * Visual impact
    * Sound design
    * Animation timing
    * Numerical feedback

#### Combat Constraints
* Frequency of encounters
* Length of battles
* Number of actions per turn
* Hit frequency and impact

### Advanced Mechanics

#### Situational Balance
* Ability effectiveness varies with context
* Environmental factors affect strategy
* Different damage types for different scenarios
* Encourage strategic adaptation

#### Transitivity and Intransitivity
* Transitive relationships (A > B > C)
* Intransitive elements (rock-paper-scissors)
* Balance between predictable and dynamic interactions
* Prevent dominant strategies

#### Feedback Loops
* Positive feedback:
    * Momentum building
    * Power scaling
    * Victory reinforcement
* Negative feedback:
    * Comeback mechanics
    * Power limiting
    * Balance preservation
* Careful management of loop intensity

### Examples from The Path

#### Class Mechanics Examples

* **Unique Resource Systems**
    * Conjuror: Echo mechanic for spell repetition
    * Zealot: Emotional intensity stacking
    * Crystal Vanguard: Damage-to-defense conversion
    * The Blessed: Divine grace enhancement

* **Role Specialization Examples**
    * Crystal Vanguard Tank Variants:
        * Shield Focus: Maximum damage mitigation
        * Golem Master: Crowd control through summons
        * Crystal Core: Self-sustain through mineral absorption

* **Synergy Examples**
    * Conjuror + The Blessed: Enhanced healing through echo effects
    * Crystal Vanguard + Zealot: Protected mobility for emotional buildup
    * The Blessed + Zealot: Divine protection during emotional peaks

* **Soft Counter Examples**
    * Zealot vs Conjuror: High mobility to pressure low health
    * Crystal Vanguard vs Zealot: Damage absorption reduces emotional gain
    * Conjuror vs Crystal Vanguard: Spiritual damage bypasses physical defense

#### Combat System Examples

* **Situational Effectiveness**
    * Conjuror's echo spells in narrow corridors
    * Crystal Vanguard's mineral absorption near crystal formations
    * Zealot's mobility advantage in open spaces
    * The Blessed's divine protection in team formations

* **Feedback Loop Management**
    * Positive: Zealot's emotional intensity building momentum
    * Negative: Crystal Vanguard's defense scaling with damage taken
    * Balanced: Conjuror's echo timing requiring strategic planning

* **Resource Economy**
    * Energy costs scale with ability impact:
        * Basic attack: 1 energy
        * Special ability: 2-3 energy
        * Ultimate ability: 4-5 energy
    * Cooldown balance:
        * Quick abilities: 1-2 turns
        * Major abilities: 3-4 turns
        * Ultimate abilities: 5+ turns

## Testing and Analysis

### Data Collection

#### Granular Analysis
* Win rates by class and matchup
* Individual ability usage stats
* Damage output metrics
* Resource efficiency tracking
* Player behavior patterns

#### Statistical Methods
* Ensure significant sample sizes
* A/B testing for specific changes
* Progression charts for rewards
* Heat maps for battle analysis
* Monte Carlo simulations for scenarios

### AI-Driven Testing

#### Adaptive AI System
* Adjusts to player skill
* Learns from player behavior
* Avoids perfect optimization
* Tests balance in various scenarios

#### AI Balance Tools
* Exploit detection
* Strategy validation
* Edge case testing
* Situational analysis
* Intransitive decision making

## Meta-Game Elements

### Economy Systems

#### Resource Management
* Health and Energy balance
* Special resource mechanics
* Item and equipment balance
* Trading considerations

#### Economic Controls
* Open vs closed economies
* Inflation management
* Power creep prevention
* Trading limitations
* Gift mechanics

### Player Experience

#### Engagement Elements
* Visual and audio feedback
* Clear ability impacts
* Satisfying interactions
* Strategic depth
* Learning curve

#### Strategic Depth
* Decision making complexity
* Build diversity
* Tactical options
* Risk vs reward
* Perfect imbalance

### Meta Evolution

#### Long-term Considerations
* Power creep management
* Content scaling
* Meta diversity
* Balance iterations
* Community feedback

#### Cognitive Factors
* Player agency vs choice paralysis
* Cognitive bias awareness
* Strategic intuition
* Learning progression
* Skill expression

## Implementation Process

### Continuous Balance

1. Regular Monitoring
    * Track win rates
    * Analyze ability usage
    * Monitor resource efficiency
    * Observe player behavior

2. Testing Cycle
    * Identify issues
    * Design solutions
    * Test changes
    * Gather feedback
    * Implement updates

3. Documentation
    * Record changes
    * Document rationale
    * Update guidelines
    * Track metrics
    * Share insights

### Class-Specific Balance

See individual class documentation for detailed balance considerations:
* [Conjuror](classes/conjuror.md)
* [Crystal Vanguard](classes/crystal_vanguard.md)
* [Zealot](classes/zealot.md)
* [The Blessed](classes/the_blessed.md)
* [Primal Shifter](classes/primal_shifter.md)
