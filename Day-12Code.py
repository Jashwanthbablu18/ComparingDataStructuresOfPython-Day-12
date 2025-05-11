# Day 12 - Comparing Data Structures
# Topic: List vs Set vs Dict vs Tuple

# This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("📊 Welcome to Day 12 of Python 30-Day Challenge!")
    print("🔹 Topic: Comparing Data Structures")
    print("🔎 Let's explore List, Set, Tuple, and Dictionary with real-life examples.\n")

# This dictionary holds the datastructure name as key and its description,use case...cons as sub key values.
dataStructuresInPy = {
    # About Lists
    "list": {
        "description": "Ordered, mutable, and yes — duplicates allowed.",
        "use_case": "To-do list, shopping cart items, playlist queue.",
        "pros": ["Maintains order", "Indexable", "Supports duplicates"],
        "cons": ["Slower lookup time", "No uniqueness enforcement"]
    },

    # About sets
    "set": {
        "description": "Unordered and unique-only club. Mutable too.",
        "use_case": "Tracking unique visitors, tag clouds, etc.",
        "pros": ["Fast membership test", "No duplicates"],
        "cons": ["Unordered (no positions)", "No indexing support"]
    },

    # About tuples
    "tuple": {
        "description": "Ordered, immutable, and totally fine with duplicates.",
        "use_case": "GPS coordinates, config settings, DB records (like rows).",
        "pros": ["Faster than lists", "Immutable", "Can be used as dict keys"],
        "cons": ["Can't modify it", "Very few built-in methods"]
    },

    # About dictionaries
    "dict": {
        "description": "Key-value pair collection (insertion order preserved since Python 3.6+).",
        "use_case": "User profiles, config files, student gradebooks.",
        "pros": ["Fast access via keys", "Organized/structured", "Can grow/change easily"],
        "cons": ["Slightly heavier in memory", "Keys must be unique"]
    }
}

# This function takes data structure key as a parameter and displays about it by retriving from above dictionary.
def dataStructuresInPyInfo(ds_key):

    # this variable gets the data structure parameter into dataStructuresInPy
    struct = dataStructuresInPy.get(ds_key)
    
    if struct:

        # This displays the data structure in uppercase
        print(f"\n📦 {ds_key.upper()} STRUCTURE")

        # This displays the description of the data structure
        print("🔍 Description:", struct["description"])

        # This displays the use case of the data structure
        print("✅ Common Use Case:", struct["use_case"])

        # This displays Pros and Cons of the data structure by looping 
        print("👍 Pros:")
        for Adv in struct["pros"]:
            print(f"   - {Adv}")
        print("👎 Cons:")
        for DisAdv in struct["cons"]:
            print(f"   - {DisAdv}")
        print("-" * 40)
    
    # If data structure isn't found
    else:
        print("❓ Structure not found.") # This won't going to happen, for a case kept.

def main():

    # Calls show_intro() to display the introduction.
    show_intro()

    # This loop runs until it breaks (exits)
    while True:

        # Displays options to choose
        print("\nChoose a data structure to explore:")
        print("1. List")
        print("2. Set")
        print("3. Tuple")
        print("4. Dict")
        print("5. Exit")

        # asks user to choose option, and removes extra spaces by .strip()
        user_choice = input("👉 Enter choice (1-5): ").strip()

        # If user chooses option 1 then display info about list
        if user_choice == "1":
            dataStructuresInPyInfo("list")

        # If user chooses option 2 then display info about set
        elif user_choice == "2":
            dataStructuresInPyInfo("set")

        # If user chooses option 3 then display info about tuple
        elif user_choice == "3":
            dataStructuresInPyInfo("tuple")

        # If user chooses option 4 then display info about dictionary
        elif user_choice == "4":
            dataStructuresInPyInfo("dict")

        # If user chooses option 5 then breaks the loop and exits
        elif user_choice == "5":
            print("👋 Exiting Comparison CLI...")
            break

        # If user chooses invalid option 
        else:
            print("❌ Invalid input.")

# calling main() to starting execution of program
if __name__ == "__main__":
    main()
