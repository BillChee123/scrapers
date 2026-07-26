import json
import os

from apify_client import ApifyClient

# Load the Apify API token from an environment variable instead of hard-coding it.
api_token = os.environ.get("APIFY_API_TOKEN")
if not api_token:
    raise RuntimeError("Missing APIFY_API_TOKEN environment variable")

client = ApifyClient(api_token)

# Prepare the Actor input
run_input = {
    "results_wanted": 20,
    "startUrl": "https://www.propertyguru.com.sg/property-for-sale?listingType=sale&page=1&propertyId=21747&isCommercial=false&_freetextDisplay=Sky+Vue&propertyNanoId=buw9im&bedrooms=2",
}

# Run the Actor and wait for it to finish
run = client.actor("shahidirfan/propertyguru-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])

# for item in client.dataset(run["defaultDatasetId"]).iterate_items():
#     print(item)

items = list(client.dataset(run["defaultDatasetId"]).iterate_items())
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(items, f, indent=2, ensure_ascii=False)

# 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/python/docs/quick-start