# A little program to check if the user is 'smuurt' or 'dumb'                @RARI

def are_you_smuurt():
    # User input prompt with some playful wording
    response = input("Are you smuurt? (yes/no): ").strip().lower()
    
    # Check if they are indeed 'smuurt'
    if response == "yes":
        print(" Congratulations! You are officially smuurt!")
    elif response == "no":
        print(" Oh no, you're...dumbass ")
    else:
        print(" Hmm, undecided, I see! Maybe you're just mysterious. ")

are_you_smuurt()
