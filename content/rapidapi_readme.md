# Zoopla Scraper

**1,000 free calls every month, no credit card.** Use them to your heart's content ❤️

This is an excellent API made by Omkar Cloud, which is Rated Excellent — [4.7 based on 30 reviews on Trustpilot](https://www.trustpilot.com/review/omkar.cloud).

## What can I get

- 🏠 **Live UK listings for sale, to rent & new homes** — price, beds, floor area, photos, agent phone; 25 per page, filter & sort
- 📋 **Full property details** — price history, tenure, EPC rating, floor plans, nearest stations, coordinates & UPRN
- 💷 **Sold prices & valuations** — HM Land Registry sold records, plus Zoopla's sale & rent estimate for any UK address
- 🧑‍💼 **Estate agent directory** — every branch in a location with phone, logo, listing stats and live listings

## Why Zoopla Scraper

Most other Zoopla APIs fail you in one of four ways:

- 🗄️ **Inaccurate, cached, stale data**
- 🧩 **Low-detail endpoints** — a few fields per call, never the full picture
- 💸 **Pay more to get the same data**
- 🪦 **Works today, breaks next month** — nobody maintains it

Zoopla Scraper is scraped live on every call, priced honestly, and actively maintained.

## Example: A Full Zoopla Listing

```json
{
  "id": 74017763,
  "title": "1 bed flat for sale",
  "address": "Clifford Road, Walthamstow E17",
  "link": "https://www.zoopla.co.uk/for-sale/details/74017763/",
  "section": "for-sale",
  "property_type": "flat",
  "condition": "pre-owned",
  "published_at": "2026-08-17T10:34:17",
  "description": "A modern studio apartment offering over 30 square meters of living space with a private outdoor patio...",
  "features": ["Studio Apartment", "Front Patio", "Modern Kitchen"],
  "bedrooms": 1,
  "bathrooms": 1,
  "living_rooms": 1,
  "floor_area": { "size_sqft": 322, "source": "comparables_epc" },
  "price": { "amount": 290000, "currency": "GBP", "label": "£290,000", "is_auction": false },
  "is_chain_free": false,
  "is_shared_ownership": false,
  "location": {
    "latitude": 51.592807,
    "longitude": -0.007352,
    "street_name": "Clifford Road",
    "postcode": "E17 4JE",
    "outcode": "E17",
    "town": "London",
    "county": "London",
    "country_code": "gb",
    "uprn": "10093562790"
  },
  "epc": { "rating": "D", "images": ["https://lid.zoocdn.com/645/430/0ac3dfab8fadb0c67087e2da18c0211da6ff89fb.png"] },
  "nearest_stations": [
    { "name": "Wood Street", "distance_miles": 0.5 },
    { "name": "Walthamstow Central", "distance_miles": 0.9 }
  ],
  "media": {
    "images": [
      "https://lid.zoocdn.com/645/430/cbca77e24b20cd7f7fb96afd70fe1ad54d585ca0.jpg",
      "https://lid.zoocdn.com/645/430/aa181049abe179b0986e8d9faf1afbe4e7df4be2.jpg"
    ],
    "floor_plans": ["https://lid.zoocdn.com/645/430/88a17dc318feee6ff5ae22f962c03c12c6d876ff.jpg"]
  },
  "agent": {
    "branch_id": 58585,
    "name": "Estates East - Walthamstow",
    "brand_name": "Estates East",
    "phone": "020 8520 9300",
    "lettings_phone": "020 8539 4213",
    "logo": "https://st.zoocdn.com/zoopla_static_agent_logo_(778425).png",
    "link": "https://www.zoopla.co.uk/find-agents/branch/estates-east-walthamstow-london-58585/"
  }
}
```

## Get Started with 1,000 Free Calls

1. [Start with **Free Plan**](https://rapidapi.com/Chetan11dev/api/zoopla-scraper/pricing) — 1,000 calls/month, no credit card.
2. Open [Zoopla Scraper](https://rapidapi.com/Chetan11dev/api/zoopla-scraper), pick an endpoint — params are pre-filled — and click **Test Endpoint**.
3. Enjoy your data 😎.

## Endpoints

11 endpoints cover everything you need.

| Endpoint | Path | What you get |
|---|---|---|
| **Search Properties For Sale** | `/properties/search-sale` | 25 listings/page with price, beds, baths, floor area, photos, agent phone; filter + sort |
| **Location Autocomplete** | `/locations/auto-complete` | UK place suggestions with the geo slug the search and house-prices endpoints accept |
| **Search Properties To Rent** | `/properties/search-rent` | Rentals, same filters plus furnished state; rent per month and per week |
| **Search New Homes** | `/properties/search-new-homes` | New-build listings with the developer as agent |
| **Get Property Details** | `/properties/details` | Everything about one listing in one call (see above) |
| **Get Property Agent Contact** | `/properties/agent-contact` | Agent name, phone numbers, branch id and profile link for a listing |
| **Search Sold House Prices** | `/house-prices/search` | HM Land Registry sold records: address, UPRN, last sale date and price |
| **Get Property Value Estimate** | `/house-prices/estimate` | Sale estimate with range + confidence, rent estimate, attributes, live listings |
| **Search Estate Agents** | `/agents/search` | Branches in a location: phone, logo, listing count, average asking price |
| **Get Estate Agent Details** | `/agents/details` | Full branch profile with coordinates, memberships and statistics |
| **Get Estate Agent Listings** | `/agents/listings` | A branch's live listings, for sale or to rent |

## Pricing

High value, Low price.

| Plan | Price | Calls / month | Per 1,000 |
|---|---|---|---|
| **Basic** | **Free** | **1,000** — most generous free plan | $0 |
| **Pro** | $16/mo | 20,000 | $0.80 |
| **Ultra** | $48/mo | 100,000 | $0.48 |
| **Mega** | $148/mo | 400,000 | $0.37 |

Need the full Zoopla dataset or a bigger plan? Ask on [WhatsApp](https://api.whatsapp.com/send?phone=918178804274&text=I%20need%20a%20custom%20plan%20for%20the%20Zoopla%20Scraper%20API.) or [Email](mailto:happy.to.help@omkar.cloud?subject=Custom%20plan%20for%20Zoopla%20Scraper%20API&body=I%20need%20a%20custom%20plan%20for%20the%20Zoopla%20Scraper%20API.).

👉 [Start with Free Plan](https://rapidapi.com/Chetan11dev/api/zoopla-scraper/pricing) — 1,000 free calls/month

## 💬 Have Questions? We Have Answers.

You're a developer — we know how hard completing a project can be. So we offer full support: just message us and we'll reply ✅ with a solution within 1 working day.

[![Message Us on WhatsApp about Zoopla Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/whatsapp-us.png)](https://api.whatsapp.com/send?phone=918178804274&text=I%20need%20help%20with%20using%20the%20Zoopla%20Scraper%20API.)

[![Ask Us on Email about Zoopla Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/ask-on-email.png)](mailto:happy.to.help@omkar.cloud?subject=Help%20with%20Zoopla%20Scraper%20API&body=I%20need%20help%20with%20using%20the%20Zoopla%20Scraper%20API.)

👉 [Start with Free Plan](https://rapidapi.com/Chetan11dev/api/zoopla-scraper/pricing) — 1,000 free calls/month
