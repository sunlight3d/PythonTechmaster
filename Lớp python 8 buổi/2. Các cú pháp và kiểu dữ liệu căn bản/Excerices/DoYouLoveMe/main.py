
answer = "no"
while answer.lower() != "yes":
    try:
        answer = input("Do you love me ? ")
    except Exception:
        pass

