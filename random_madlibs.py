from madlibs import madlib, adj, verb1, verb2, famous_person
import random

if __name__ == "__main__":
    m = random.choice([madlib, adj, verb1, verb2, famous_person])
    print(m)