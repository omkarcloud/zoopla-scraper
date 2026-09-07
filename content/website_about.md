# Zoopla Scraper

Zoopla Scraper gets you 🎯 accurate, 🔍 detailed Zoopla data as clean JSON — in real time.

Zoopla uses Cloudflare bot protection to stop you from getting its data.

Zoopla Scraper beats it — no selectors, no proxies, no data cleaning. Just the data, so you can successfully complete your project.

**1,000 free calls every month, no credit card.** Use them to your heart's content ❤️

This is an excellent API — we're Rated Excellent, [4.7 based on 30 reviews on Trustpilot](https://www.trustpilot.com/review/omkar.cloud).

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

*Trimmed for readability.*

## Get Started with 1,000 Free Calls

Start in the [playground](https://www.omkar.cloud/tools/zoopla-scraper/playground) — try any endpoint with one click, no sign-up required.

Once you're happy with the data, start with the free plan for 1,000 free calls every month:

1. [Sign up on Omkar Cloud](https://www.omkar.cloud/auth/sign-up?redirect=/tools/zoopla-scraper/playground) — free, no credit card.
2. Open the [Zoopla Scraper playground](https://www.omkar.cloud/tools/zoopla-scraper/playground) and enter any UK town or postcode you like. Click **Get Live Data**.
3. Enjoy your data 😎.

## Endpoints

11 endpoints cover everything you need.

- **Location Autocomplete** (`/locations/auto-complete`) — any UK place name → the geo slug search and house prices accept
- **Search For Sale / To Rent / New Homes** (`/properties/search-sale`, `/properties/search-rent`, `/properties/search-new-homes`) — 25 listings per page; filter by price, beds, type; sortable
- **Property Details** (`/properties/details`) — everything about one listing in a single call
- **Agent Contact** (`/properties/agent-contact`) — agent name, phone numbers and branch link for a listing
- **Sold House Prices** (`/house-prices/search`) — HM Land Registry sold records for any UK area, 25 per page
- **Property Value Estimate** (`/house-prices/estimate`) — sale and rent estimate with range and confidence for any address
- **Search Estate Agents** (`/agents/search`) — branches in a location with phone, logo and listing stats
- **Estate Agent Details** (`/agents/details`) — full branch profile with memberships and statistics
- **Estate Agent Listings** (`/agents/listings`) — a branch's live listings, for sale or to rent

## Pricing

High value, Low price.

- **Basic — Free**: **1,000 calls/month** — the most generous free plan
- **Pro — $16/mo**: 20,000 calls/month ($0.80 per 1,000)
- **Ultra — $48/mo**: 100,000 calls/month ($0.48 per 1,000)
- **Mega — $148/mo**: 400,000 calls/month ($0.37 per 1,000)

Need the full Zoopla dataset or a bigger plan? Ask on [WhatsApp](https://api.whatsapp.com/send?phone=918178804274&text=I%20need%20a%20custom%20plan%20for%20the%20Zoopla%20Scraper%20API.) or [Email](mailto:happy.to.help@omkar.cloud?subject=Custom%20plan%20for%20Zoopla%20Scraper%20API&body=I%20need%20a%20custom%20plan%20for%20the%20Zoopla%20Scraper%20API.).

👉 [Start with Free Plan](https://www.omkar.cloud/auth/sign-up?redirect=/tools/zoopla-scraper/playground) — 1,000 free calls/month

## 💰 2-Click Refund Guarantee

Your happiness is our happiness. We will gladly issue a refund if you are not happy with the API. Here's how:

1. Go to [Transactions Page](https://www.omkar.cloud/billing/transaction-history)
![Transactions Page](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/transactions-page.png)

2. Click "Request Refund"
![Request Refund Button](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/request-refund-button.png)

3. Confirm by clicking **Request Refund** again.
![Confirm Refund Request](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/confirm-refund-request.png)

✅ That's it! You'll receive a confirmation email from PayPal, and your money will be returned to your original payment method within **1–2 business days**.

No emails. No explanations. A simple refund in 2 clicks. As it should be.

## 💬 Have Questions? We Have Answers.

You're a developer — we know how hard completing a project can be. So we offer full support: just message us and we'll reply ✅ with a solution within 1 working day.

[![Message Us on WhatsApp about Zoopla Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/whatsapp-us.png)](https://api.whatsapp.com/send?phone=918178804274&text=I%20need%20help%20using%20the%20Zoopla%20Scraper%20API.)

[![Ask Us by Email about Zoopla Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/ask-on-email.png)](mailto:happy.to.help@omkar.cloud?subject=Help%20with%20Zoopla%20Scraper%20API&body=I%20need%20help%20using%20the%20Zoopla%20Scraper%20API.)

## Popular Scrapers by Omkar Cloud

- [**Google Maps Scraper (3,100+ GitHub Stars)**](https://github.com/omkarcloud/google-maps-scraper) — type "estate agents in London", get every business as a ready-to-call lead list: phones, emails, websites & reviews. Up to 100K free leads/month.
- [**Rightmove Scraper**](https://www.omkar.cloud/tools/rightmove-scraper) — UK homes for sale & to rent, sold prices & estate agents
- [**Website Email Contact Scraper**](https://www.omkar.cloud/tools/website-email-contact-scraper) — emails, phones & socials from any website
- [**AliExpress Scraper**](https://www.omkar.cloud/tools/aliexpress-scraper) — live product details, SKU variants, stock & shipping
- [**Booking Scraper**](https://www.omkar.cloud/tools/booking-scraper) — Booking.com hotels: prices, ratings, rooms & amenities
- [**IMDb Scraper**](https://www.omkar.cloud/tools/imdb-scraper) — movies, TV, ratings, cast, charts & box office

👉 [Start with Free Plan](https://www.omkar.cloud/auth/sign-up?redirect=/tools/zoopla-scraper/playground) — 1,000 free calls/month
