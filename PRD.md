# PRD - Multi-Agent Translation Chain with Skills

## Project Goal
Build an AI agent workflow that translates a sentence through multiple languages using separate Skills, then compares the final English sentence to the original sentence.

## Required Flow
1. English to French
2. French to Hebrew
3. Hebrew back to English
4. Compare original English sentence with final English sentence

## Level
Level 3 - One agent using multiple Skills.

## Main Components
- Translation Skill: English to French
- Translation Skill: French to Hebrew
- Translation Skill: Hebrew to English
- Comparison Skill: compare semantic similarity between original and final text

## Expected Output
The system should produce:
- Original English sentence
- French translation
- Hebrew translation
- Final English translation
- Similarity score / distance
- Short explanation of meaning changes

## Example Input
One for all and all for one
