# 🌍 Personalized Adventure Guide

print("=" * 50)
print("🌍 PERSONALIZED ADVENTURE GUIDE")
print("=" * 50)

name = input("\n👤 Enter your name: ").strip().title()

print(f"\nWelcome, {name}! Let's plan your perfect trip. ✈️")

# Destination Recommendations

def destination_guide(choice):
    if choice == "Mountain":
        print("\n🏔️ Mountain Adventure")
        print("Recommended destinations:")
        print("1. Manali")
        print("2. Shimla")
        print("3. Mussoorie")
        print("4. Rishikesh")

        activities = [
            "🥾 Trekking",
            "🏕️ Camping",
            "🪂 Paragliding",
            "📸 Mountain sightseeing"
        ]

        packing = [
            "🧥 Warm clothes",
            "🥾 Comfortable shoes",
            "🧴 Sunscreen",
            "🎒 Backpack"
        ]

        return activities, packing

    elif choice == "Beach":
        print("\n🏖️ Beach Adventure")
        print("Recommended destinations:")
        print("1. Goa")
        print("2. Kerala",
        )
        print("3. Andaman")
        print("4. Pondicherry")

        activities = [
            "🏊 Swimming",
            "🏄 Water sports",
            "🌅 Sunset sightseeing",
            "🚤 Boat rides"
        ]

        packing = [
            "👕 Light clothes",
            "🩴 Comfortable footwear",
            "🕶️ Sunglasses",
            "🧴 Sunscreen"
        ]

        return activities, packing

    else:
        print("\n❌ Invalid destination type.")
        return [], []

# Budget Category

def budget_category(total_budget):
    if total_budget >= 20000:
        return "💎 Luxury Trip"
    elif total_budget >= 10000:
        return "✨ Comfortable Trip"
    elif total_budget >= 5000:
        return "💰 Budget-Friendly Trip"
    else:
        return "🎒 Low-Budget Trip"

# Trip Cost Calculation

def calculate_cost(days, travelers, daily_budget):
    return days * travelers * daily_budget

# Main Program

while True:

    try:
        print("\nChoose your travel preference:")
        print("1. 🏔️ Mountain")
        print("2. 🏖️ Beach")

        choice = input("\nEnter your choice (1 or 2): ").strip()

        if choice == "1":
            destination = "Mountain"
        elif choice == "2":
            destination = "Beach"
        else:
            print("❌ Please choose either 1 or 2.")
            continue

        # Get destination recommendations
        activities, packing = destination_guide(destination)

        # Trip details
        days = int(input("\n📅 Enter number of days: "))
        travelers = int(input("👥 Enter number of travelers: "))
        daily_budget = float(input("💵 Enter your budget per person per day: "))

        # Validate values
        if days <= 0 or travelers <= 0 or daily_budget <= 0:
            print("❌ Days, travelers and budget must be greater than 0.")
            continue

        # Calculate total estimated cost
        total_cost = calculate_cost(
            days,
            travelers,
            daily_budget
        )

        # Budget category
        category = budget_category(total_cost)

        # Trip Summary
        print("\n" + "=" * 50)
        print("🧾 YOUR TRIP SUMMARY")
        print("=" * 50)

        print(f"👤 Traveler       : {name}")
        print(f"🌍 Trip Type      : {destination}")
        print(f"📅 Duration       : {days} days")
        print(f"👥 Travelers      : {travelers}")
        print(f"💵 Daily Budget   : ₹{daily_budget:.2f}")
        print(f"💰 Estimated Cost : ₹{total_cost:.2f}")
        print(f"🏷️ Trip Category  : {category}")

        # Activities
        print("\n🎯 Recommended Activities:")
        for activity in activities:
            print(f"   {activity}")

        # Packing list
        print("\n🎒 Suggested Packing List:")
        for item in packing:
            print(f"   {item}")

        print("\n🌟 Have a safe and memorable journey!")

        # Another trip
        again = input(
            "\nWould you like to plan another trip? (yes/no): "
        ).strip().lower()

        if again != "yes":
            print("\n👋 Thank you for using Personalized Adventure Guide!")
            break

    except ValueError:
        print("\n❌ Invalid input. Please enter numbers where required.")