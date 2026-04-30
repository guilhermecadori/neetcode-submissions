def concatenate(s1: str, s2: str) -> str:
    string = s1 + s2
    return string if len(string) <= 10 else "Too long!"

# do not modify below this line
print(concatenate("He", "llo"))
print(concatenate("Hello ", "world!"))
print(concatenate("Length", "of10"))
