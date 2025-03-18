---
title: Battle Conditions Reference
description: Technical specification of battle conditions, including speed priority, field effects, and class-based modifiers that affect combat.
---

# Battle Conditions Reference

!!! info "Overview"
    This document outlines the various conditions that can affect combat, including turn order priority, environmental effects, and class-specific modifiers.


## Speed Priority
| Priority | Description |
|----------|-------------|
| Quick | Moves that always act first in the turn |
| Normal | Standard priority moves |
| Slow | Moves that always act last in the turn |
| Counter | Only activates in response to opponent's move |
| Delayed | Takes effect at end of next turn |

## Field Conditions

### Class-Based Effects
| Condition | Description | Source |
|-----------|-------------|--------|
| Sacred Ground | Spiritual moves gain `x%` power boost, Physical moves deal `x%` less damage | The Blessed |
| Holy Sanctuary | Negative status effects expire after 1 turn, healing increased by `x%` | The Blessed |
| Crystal Field | Crystal attacks deal `x%` more damage, physical attacks deal `x%` less damage | Crystal Vanguard |
| Crystal Haven | Defense increased by `x%`, attack speed reduced by `x%` | Crystal Vanguard |
| Shadow Realm | Psychic and Spirit damage increased by `x%`, healing reduced by `x%` | Wraithwood Seer |
| Mind Field | All attacks have `x%` chance to inflict confusion | Wraithwood Seer |
| Primal Arena | Physical and Root damage increased by `x%`, Spiritual decreased by `x%` | Primal Shifter |
| Wild Territory | All units gain `x%` speed but lose `x%` accuracy | Primal Shifter |
| Spirit Mist | All damage becomes Spirit type, status effects have double duration | Conjuror |
| Echo Chamber | All moves have `x%` chance to trigger twice | Conjuror |
| War Ground | Physical damage increased by `x%`, healing reduced by `x%` | Zealot |
| Passion Field | Attack speed increased by `x%`, defense reduced by `x%` | Zealot |

### Attack Type Effects
| Condition | Description | Source |
|-----------|-------------|--------|
| Blade Storm | Slash damage increased by `x%`, evasion reduced by `x%` | Slash |
| Sharp Wind | All attacks gain Slash property, accuracy reduced by `x%` | Slash |
| Pierce Veil | Pierce attacks ignore `x%` defense, all units take `x%` more damage | Pierce |
| Needle Rain | Pierce attacks cause Bleed, defense reduced by `x%` | Pierce |
| Impact Zone | Blunt attacks deal `x%` more damage, speed reduced by `x%` | Blunt |
| Crushing Field | Blunt attacks have `x%` chance to Stun, movement speed reduced | Blunt |
| Spirit Nexus | Spirit damage increased by `x%`, physical damage reduced by `x%` | Spirit |
| Soul Mist | Spirit attacks have `x%` lifesteal, defense reduced by `x%` | Spirit |
| Blood Moon | Blood attacks gain `x%` lifesteal, healing reduced by `x%` | Blood |
| Crimson Field | Blood attacks deal bonus damage to shields, HP costs increased by `x%` | Blood |
| Bone Yard | Bone attacks deal `x%` more damage, healing reduced by `x%` | Bone |
| Ancestral Ground | Bone attacks ignore `x%` defense, speed reduced by `x%` | Bone |
| Fire Storm | Fire damage increased by `x%`, Water damage reduced by `x%` | Fire |
| Burning Ground | Fire attacks apply Burn, all units take `x%` more damage | Fire |
| Frost Field | Frost attacks slow targets by `x%`, Fire damage reduced by `x%` | Frost |
| Ice Mirror | Frost attacks have `x%` chance to freeze, movement speed reduced | Frost |

### Stat-Based Effects
| Condition | Description | Source |
|-----------|-------------|--------|
| Vitality Zone | All units gain `x%` max HP, healing reduced by `x%` | HP |
| Power Surge | Attack increased by `x%`, defense reduced by `x%` | Attack |
| Mystic Realm | Magic damage increased by `x%`, physical damage reduced by `x%` | Magic |
| Iron Wall | Physical defense increased by `x%`, speed reduced by `x%` | Physical Defense |
| Magic Barrier | Magic defense increased by `x%`, attack reduced by `x%` | Magic Defense |
| Swift Current | Speed increased by `x%`, defense reduced by `x%` | Speed |
| Fortune Field | Critical hit chance increased by `x%`, defense reduced by `x%` | Luck |


