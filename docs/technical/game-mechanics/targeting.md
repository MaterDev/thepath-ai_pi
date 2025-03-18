---
title: Targeting System Reference
description: Technical specification of the targeting system, including target types, targeting keys, and their applications in combat.
---

# Targeting System Reference

!!! info "Overview"
    This document details the various targeting mechanisms available in the combat system, including how different abilities and effects select their targets.

## Target Types
| Target Type | Description |
|------------|-------------|
| Self | Effect applies to `s` only |
| Single Enemy | Effect applies to `t` only |
| All Entities | Effect applies to `s` and `t` |
| Field | Effect applies to `f`, affecting conditions |
| Random | Effect applies to random choice between `s` or `t` |
| Both | Effect applies to `s` and `t` equally |
| None | Effect applies to `f` without targeting |
| Reflected | Effect originates from `s` but applies to `t` |
| Either | Effect can be applied to choice of `s` or `t` |
| Last Hit | Effect applies to last entity (`s` or `t`) that took damage |

## Targeting Keys
- `s`: source/self (the entity using the ability)
- `t`: target (the enemy entity)
- `f`: field (the battle environment)

!!! note "Implementation Details"
    When implementing targeting logic, ensure proper validation of target type against the ability being used. Some abilities may have restrictions on valid targets based on their effects or the current battle conditions.


