from collections import defaultdict
score = defaultdict(lambda: 0)
score['Alice'] = 10
score['Bob'] = 9
print(f"{score['Charlie'] = }")  # 0

