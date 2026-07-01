from modules.scoring_engine import (
    filler_word_ratio,
    evaluate_understanding
)

text = """
Machine learning is actually like a branch of AI.
"""

audio = {
    "pause_ratio":0.12,
    "rms_energy":0.03
}

count,total,ratio = filler_word_ratio(text)

score,level = evaluate_understanding(
    85,
    ratio,
    audio
)

print("Filler Count:",count)
print("Total Words:",total)
print("Ratio:",ratio)
print("Score:",score)
print("Level:",level)