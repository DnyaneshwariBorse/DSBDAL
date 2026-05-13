import requests

try:
    print("Fetching data from Steam API...")
    url = "https://store.steampowered.com/appreviews/730?json=1"
    response = requests.get(url)
    data = response.json()

    print("\nTotal Reviews:", data["query_summary"]["total_reviews"])
    print("Rating:", data["query_summary"]["review_score_desc"])
    print("-" * 50)

    for i, r in enumerate(data["reviews"], 1):
        # We use encode/decode to remove emojis so it doesn't crash your terminal
        customer = str(r["author"].get("personaname", "Unknown")).encode('ascii', 'ignore').decode('ascii')
        review_text = str(r["review"][:200]).encode('ascii', 'ignore').decode('ascii')
        
        print(f"\nReview #{i}")
        print("Customer:", customer)
        print("Rating:", "Recommended" if r["voted_up"] else "Not Recommended")
        print("Review:", review_text)
        print("Votes:", r["votes_up"])
        print("-" * 50)

except Exception as e:
    print("An error occurred:", e)

