def hamming_distance(s1, s2):
  if len(s1) != len(s2):
    return None
  else:
    distance = 0
    for i in range(len(s1)):
      if s1[i] != s2[i]:
        distance += 1
    return distance

print(hamming_distance("Hello","Hallo"))