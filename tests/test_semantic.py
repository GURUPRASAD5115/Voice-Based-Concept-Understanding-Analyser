from modules.semantic_eval import calculate_similarity

student = """
Machine Learning is a branch of Artificial Intelligence
that enables computers to learn from data.
"""

reference = """
Machine Learning is a branch of Artificial Intelligence
that enables machines to learn from data.
"""

score, level = calculate_similarity(
    student,
    reference
)

print("Similarity Score:", score)
print("Understanding:", level)