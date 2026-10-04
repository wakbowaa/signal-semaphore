# Frontend design contract

## Product posture
The page is a working railway signal cabin, not a landing page or analytics dashboard. The first viewport must expose line state, semaphore arm, and the current write action.

## Composition
- Three zones: line brief, central signal mast, operator desk.
- Custom components: semaphore mast, enamel line plate, lever action, punched bell ticket, block meter.
- No card grid, metric strip, hero button, illustration panel, or generic sidebar.

## Visual system
Night navy, signal red, lamp green, warm enamel, and brass are token-only colors. Narrow display type carries station authority; monospace labels carry machine state.

## Motion and effects
Arm sweep, lamp ignite, lever pull, ticket feed, and bell pulse are named states. CSS linkage and radial lamp bloom are the two effects. Reduced motion disables all transitions.

## Responsive rule
At 900px the cabin becomes a vertical signal stack. At 480px all controls remain one-column and touch-safe without horizontal overflow.
