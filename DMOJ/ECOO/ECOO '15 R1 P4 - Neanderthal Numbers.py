w=["ook","ookook","oog","ooga","ug","mook","mookmook","oogam","oogum","ugug"]

from functools import lru_cache

@lru_cache(None)
def peter(s):
    if len(s)==0:
      return 1
    i=0
    for a in w:
        if s.startswith(a):
            i+=peter(s[len(a):])
    return i
for _ in range(10):
  print(peter(input()))