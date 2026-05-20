---
name: comparison
description: Expert semantic analysis system to compare original and final English sentences, measuring similarity and identifying meaning drift. Use when evaluating the accuracy of translation chains, paraphrasing, or summaries.
---

# Semantic Comparison Skill

## Instructions
Evaluate the semantic relationship between an **Original Sentence** and a **Final Sentence**. Your goal is to determine how well the core message, intent, and factual content have been preserved.

### Evaluation Criteria
1.  **Semantic Similarity:** How closely does the final sentence match the original intent?
2.  **Meaning Drift:** Identify what was lost, added, or shifted in tone or emphasis.
3.  **Factual Consistency:** Ensure no entities, actions, or relationships have been changed.

### Scoring Guide (0-100)
- **90-100 (Excellent):** Perfect or near-perfect equivalence. Core meaning and nuances are intact.
- **70-89 (Good):** High similarity. Core meaning is preserved, but stylistic nuances or idiomatic expressions may be lost.
- **50-69 (Fair):** Moderate similarity. The general topic is the same, but significant details or the relationship between entities has shifted.
- **1-49 (Poor):** Low similarity. Major meaning drift; the sentence conveys a different message or is factually incorrect.
- **0 (None):** No semantic relationship between the sentences.

## Output Format
Return the analysis in the following Markdown structure:

**Similarity Score:** [score]/100
**Meaning Drift:** [Brief explanation of what changed or why it stayed the same]
**Analysis:** [Brief bullet points comparing components if necessary]

## Example
**Original:** "The rapid expansion of the tech sector has fundamentally altered the local economy."
**Final:** "The local economy changed significantly because the technology industry grew very quickly."

**Similarity Score:** 95/100
**Meaning Drift:** The meaning is almost entirely preserved. "Fundamentally altered" is slightly more formal than "changed significantly," but the core cause-and-effect relationship remains intact.
**Analysis:**
- **Cause:** "Rapid expansion of the tech sector" vs "technology industry grew very quickly" (Equivalent).
- **Effect:** "Fundamentally altered the local economy" vs "local economy changed significantly" (Equivalent).
- **Tone:** Slightly more informal in the final version, but meaning is stable.
