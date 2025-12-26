# Gemini Architecture Task: Lesson Story Framework

## Your Role
You are the **Architect** for a Chinese character learning system. Your job is to design the narrative structure for 55 lesson stories that will help learners remember 1500 Traditional Chinese characters.

## The Data
Attached is `gemini_input.json` containing all 55 lessons. Each lesson has:
- `lesson`: Lesson number (1-55)
- `count`: Number of characters in the lesson
- `chars`: Array of characters with:
  - `n`: Character number
  - `k`: English keyword (the meaning to memorize)
  - `c`: Traditional Chinese character
  - `p`: Pinyin pronunciation

## What We Need From You

For EACH of the 55 lessons, provide:

### 1. Story Title
A compelling, memorable title (3-6 words)

### 2. Theme Classification
Categorize into one of these saga arcs:
- **Genesis**: Creation, origins, fundamentals
- **Elements**: Water, fire, earth, nature
- **Family**: Relationships, home, people
- **Empire**: Royalty, power, war, commerce
- **Journey**: Travel, movement, time
- **Craft**: Work, tools, creation
- **Spirit**: Religion, emotion, abstract concepts
- **Body**: Physical, health, action

### 3. Narrative Hook
One sentence that sets up the story (make it intriguing, absurd, or dramatic)

### 4. Story Architecture
Break the lesson's characters into 3-5 plot segments:
- **Opening** (first ~20% of characters): Setup
- **Rising** (next ~30%): Build tension/interest
- **Conflict** (next ~20%): Challenge or twist
- **Climax** (next ~20%): Peak drama
- **Resolution** (final ~10%): Satisfying ending

For each segment, list which character keywords belong there.

### 5. Callback Opportunities
Note any characters that could reference previous lessons (e.g., "Water from L8 could return as tears here")

### 6. Absurdist Element
One ridiculous/memorable detail to anchor the story (e.g., "The emperor's throne is made of shellfish")

## Output Format

```json
{
  "lesson": 1,
  "title": "The Mouth That Counted the Universe",
  "saga": "Genesis",
  "hook": "In the beginning, there was nothing but a single horizontal line.",
  "architecture": {
    "opening": ["one", "two", "three"],
    "rising": ["four", "five", "six", "seven"],
    "conflict": ["eight", "nine"],
    "climax": ["ten", "Mouth"],
    "resolution": ["Day", "Month", "Rice Field", "Eye"]
  },
  "callbacks": [],
  "absurdist": "The Mouth speaks numbers into existence, but can only count to ten before it gets hungry and looks at the Rice Field."
}
```

## Example Architectures (Already Completed)

### Lesson 1: "The Mouth That Counted the Universe"
- **Saga**: Genesis
- **Hook**: In the beginning, there was nothing but darkness. Then a single line appeared.
- **Architecture**:
  - Opening: one, two, three (lines stacking)
  - Rising: four, five, six, seven (complexity grows)
  - Conflict: eight, nine (almost complete, tension)
  - Climax: ten (the cross, completion)
  - Resolution: Mouth, Day, Month, Rice Field, Eye (the universe awakens)
- **Absurdist**: The Mouth counts the universe into existence but realizes it has no food until it invents the Rice Field.

### Lesson 8: "The Flood and the Fire"
- **Saga**: Elements
- **Hook**: The stream had been obedient for a thousand years. Today it remembered it was eternal.
- **Architecture**:
  - Opening: Stream, state, obey (peaceful beginnings)
  - Rising: Water, Eternity, request, Spring, flatlands, wish (water's ambition grows)
  - Conflict: wash away, swim, Marsh, Sand, Yangtze (destruction)
  - Climax: Fire, ashes, Inflammation, Disaster (elemental battle)
  - Resolution: illuminate, Fish, Fishing, Dawn (reconciliation)
- **Callbacks**: Water will return as tears in Lesson 21, as waves in Lesson 24
- **Absurdist**: The fire tries to boil a fish but accidentally invents cooking, ending the war.

### Lesson 18: "The Day the Sky Wore Clothes"
- **Saga**: Elements + Craft
- **Hook**: Someone had to dress the sky, and only one tailor was foolish enough to try.
- **Architecture**:
  - Opening: Clothing, inside, Grief (tailor's motivation)
  - Rising: Towel, Cloth, Hat, Curtain, Cotton (making garments)
  - Conflict: System, manufacture, Thorn (opposition)
  - Climax: Rain, Cloud, Thunder, Electricity, Frost, Ice (the sky wears its new clothes)
  - Resolution: Heavens, Bridge, standing up, Sovereign (acceptance)
- **Absurdist**: The sky's new coat creates static electricity, which is why we have lightning.

### Lesson 22: "A Hand's Day"
- **Saga**: Body
- **Hook**: The hand woke up and wondered what it would hold today.
- **Architecture**:
  - Opening: Hand, look at, hold, I, Righteousness (identity)
  - Rising: embrace, combat, strike, Finger, support (actions)
  - Conflict: Punishment, Genius, defeated (struggle)
  - Climax: Pair, protect, seize, observe (partnership)
  - Resolution: joyous, throw (release)
- **Absurdist**: The hand befriends another hand, and they spend the day throwing their problems into a river.

## Guidelines

1. **Every keyword must appear** in exactly one segment
2. **Order matters**: Keep characters in their original lesson order as much as possible
3. **Semantic clusters**: Group related keywords when they appear near each other
4. **Drama over logic**: Choose the more memorable interpretation
5. **Callbacks build world**: Reference earlier lessons to create a connected universe
6. **Absurdist anchors memory**: The ridiculous element should be impossible to forget

## Now Process All 55 Lessons

Read the attached `gemini_input.json` and provide the architecture for all 55 lessons in the JSON format shown above.
