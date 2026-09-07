# Zoopla Scraper — Extract UK Property Listings, Prices & Estate Agents

Scrape Zoopla properties for sale and to rent with prices, bedrooms, floor areas, photos, and estate agent phone numbers — plus full listing profiles and property value estimates for any UK address. No coding required.

Type a UK location, pick for-sale or to-rent, set your price and bedroom filters, click Start, and get one clean JSON record per listing: title, address, price with formatted labels, bedrooms/bathrooms, floor area, listed-on date, photos, and the estate agent's name and phone number.

Paste Zoopla listing URLs instead and get the full property profile — description, features, tenure, price history, EPC rating, exact coordinates with UPRN, nearest stations, service charge and council tax info, floor plans, and the agent's sales and lettings numbers. Add addresses to the valuation list and each also brings Zoopla's automated value estimate: the sale estimate with lower/upper range and confidence, plus a monthly rent estimate.

Covers the whole UK — England, Scotland, Wales, and Northern Ireland — and exports to JSON, CSV, or Excel in one click.

**Rated Excellent — 4.6 based on 25 reviews** on [Trustpilot](https://www.trustpilot.com/review/omkar.cloud).

## Output example: Zoopla property data in JSON

Each listing becomes one dataset item. Here is a trimmed search result:

```json
{
  "id": "74079940",
  "title": "2 bed flat for sale",
  "address": "Church Walk, London NW2",
  "link": "https://www.zoopla.co.uk/for-sale/details/74079940/",
  "summary": "A charming two-bedroom ground floor flat situated on the peaceful and picturesque Church Walk, NW2. Spanning over 600 sq ft, the property offers ...",
  "property_type": "flat",
  "bedrooms": 2,
  "bathrooms": 1,
  "receptions": 1,
  "floor_area": { "size_sqft": 646, "source": "structured_data" },
  "price": {
    "amount": 425000,
    "currency": "GBP",
    "label": "£425,000",
    "short_label": "£425k",
    "qualifier": null
  },
  "listed_on": "2026-08-27",
  "flag": "Just added",
  "tags": ["Leasehold"],
  "is_premium": true,
  "is_under_offer": false,
  "media": {
    "main_image": "https://lid.zoocdn.com/645/430/2ceaffdf3328428915bf741ae20a48ea0d3af506.jpg",
    "gallery": [
      "https://lid.zoocdn.com/645/430/3f7f8c22b9a649f75d561e6881d4abec55f430fe.jpg",
      "https://lid.zoocdn.com/645/430/10ba9635f7fc17105479790b3adbd9deff50e1eb.jpg"
    ],
    "image_count": 6,
    "floor_plan_count": 1
  },
  "agent": {
    "branch_id": 419,
    "name": "Chancellors - Hampstead",
    "phone": "020 3478 2899",
    "link": "https://www.zoopla.co.uk/find-agents/branch/chancellors-hampstead-london-419/"
  }
}
```

*Trimmed for readability*

The listings are live — the `Just added` flag, price, and agent phone number are the same ones a visitor sees on zoopla.co.uk when the run executes.

## What data does the Zoopla Scraper extract?

| Data group | Fields |
|------------|--------|
| Listing | Title, address, canonical Zoopla link, summary, property type, listed-on date, premium/under-offer flags |
| Prices | Asking price with formatted labels and qualifiers (Guide price, Offers over), monthly rent with per-week labels, price history and price per sq ft in full profiles |
| Rooms & size | Bedrooms, bathrooms, receptions, floor area in sq ft |
| Property facts | Tenure, chain-free/shared-ownership flags, EPC rating, service charge, council tax band, ground rent (full profiles) |
| Location | Exact coordinates, street, postcode, outcode, town, county, UPRN, nearest stations with distances (full profiles) |
| Media | Photos, floor plans, image counts |
| Estate agent | Branch id, name, phone (sales + lettings in full profiles), logo, profile link |
| Valuations | Sale estimate with lower/upper range and confidence, monthly rent estimate, value change since last sale, property attributes |

## How to scrape Zoopla properties

1. Click **Try for free**.
2. Enter one or more **UK locations** — for example `London` or `Manchester` — with your section (for sale / to rent / new homes) and filters. Or paste **Zoopla listing URLs** (like `https://www.zoopla.co.uk/for-sale/details/74079940/`) to scrape full property profiles, and **UK addresses** to get value estimates.
3. Click **Start** and wait for the run to finish.
4. Open the **Dataset** tab to preview your data, then download it as **JSON, CSV, Excel, XML, or an HTML table**.

No proxies, no browser setup, no CAPTCHA solving — you type locations and get structured data back.

## Input

```json
{
  "searchQueries": ["London"],
  "section": "for-sale",
  "priceMin": 300000,
  "priceMax": 500000,
  "bedsMin": 2,
  "bedsMax": 4,
  "propertyType": "flats",
  "keywords": "garden",
  "radius": 5,
  "sortBy": "newest",
  "maxProperties": 100,
  "zooplaPropertyUrls": [
    { "url": "https://www.zoopla.co.uk/for-sale/details/74079940/" }
  ],
  "valuationAddresses": ["45 Princes Avenue, South Croydon, CR2 9BE"]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `searchQueries` | array | UK locations to search — towns, areas, postcodes, or outcodes (`London`, `NW3`, `london/croydon`). Pasted zoopla.co.uk search URLs work too, with their embedded filters applied. Each matching listing becomes one dataset record. |
| `section` | string | `for-sale` (default), `to-rent`, or `new-homes`. |
| `priceMin` / `priceMax` | number | Price bounds in GBP. For rentals these are monthly rent bounds. |
| `bedsMin` / `bedsMax` | number | Bedroom bounds (0–15). |
| `propertyType` | string | `detached`, `semi_detached`, `terraced`, `flats`, `bungalow`, `park_home`, `farms_land`, `detached_bungalow`, `semi_detached_bungalow`, `terraced_bungalow`. |
| `furnishedState` | string | To-rent only: `furnished`, `part_furnished`, `unfurnished`. |
| `keywords` | string | Free-text keywords to match in the listing — e.g. `garden`, `garage`, `chain free`. |
| `radius` | number | Search radius in miles around the location (0–40). |
| `sortBy` | string | `newest` (default), `highest_price`, `lowest_price`, `most_reduced`, `most_popular`. |
| `maxProperties` | number | Maximum listings to collect per search query. |
| `zooplaPropertyUrls` | array | Zoopla listing URLs to scrape in full — one record per listing with description, features, tenure, price history, EPC, coordinates, nearest stations, floor plans, and the agent's contact details. |
| `valuationAddresses` | array | Full UK addresses (including postcode) or bare UPRNs — one value-estimate record each, with sale and rent estimates, ranges, and confidence. |

## How much does it cost to scrape Zoopla?

Scraping Zoopla costs **$5 per 1,000 properties** ($0.005 per property). Apify gives you **$5 in free credits** every month, so you can scrape your first 1,000 properties and test the Zoopla Scraper before paying anything.

## FAQs

### Why scrape Zoopla?

- **Property investment research** — find undervalued properties by comparing asking prices against the area's sold prices and Zoopla's own value estimates.
- **Market analysis** — track prices, price drops, and time on market across areas, property types, and bedroom counts.
- **Lead generation** — every listing carries its estate agent's name and phone number; full profiles add the lettings line too.
- **Portfolio valuation** — feed your addresses into the valuation list and get sale + rent estimates with confidence ranges for every property you hold.
- **Proptech apps** — power search, comparison, and valuation features with live listing data.

### Can I scrape full listing details?

Yes. Paste listing URLs into **zooplaPropertyUrls** and each becomes one record with the complete profile: description, features, tenure, price history, price per sq ft, EPC rating, exact coordinates with UPRN, nearest stations, service charge / council tax / ground rent, photos, floor plans, and the agent's sales and lettings phone numbers.

### Can I get property value estimates?

Yes. Add full UK addresses (including postcode) — or bare UPRNs — to **valuationAddresses** and each returns Zoopla's automated valuation: the current sale estimate with lower/upper range and a confidence level, the value change since the last sale, and a monthly rent estimate.

### Can I scrape multiple locations or listings in one run?

Yes. All three input lists accept any number of entries — every location is searched and every listing URL and address is scraped, each becoming its own dataset item. If a listing can't be retrieved, it's skipped and noted in the run log, and the rest of your run still completes.

### Which areas are covered?

All of the UK — England, Scotland, Wales, and Northern Ireland. Anything you can search on zoopla.co.uk works: towns, London boroughs, outcodes like `NW3`, and full postcodes.

### How accurate is the scraped data?

It comes straight from live Zoopla pages — real asking prices, HM Land Registry-backed sold prices, Zoopla's own value estimates, and real agent contact details, in the same structure you see on the site.

## Support

Built by developers, for developers — when you reach out, you talk to the engineers who built the Actor, not a support script. Message us anytime and we'll resolve your query within 1 working day.

[![Contact Us on WhatsApp about Zoopla Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/whatsapp-us.png)](https://api.whatsapp.com/send?phone=918178804274&text=I%20have%20a%20question%20about%20the%20Zoopla%20Scraper.)

Email: [happy.to.help@omkar.cloud](mailto:happy.to.help@omkar.cloud?subject=Zoopla%20Scraper%20Question)

[![Email Us about Zoopla Scraper](https://raw.githubusercontent.com/omkarcloud/assets/master/images/ask-on-email.png)](mailto:happy.to.help@omkar.cloud?subject=Zoopla%20Scraper%20Question)

## Love It? Star It! ⭐

From one business owner to another: if this Actor saved you hours of copying property prices off Zoopla, please [rate the Zoopla Scraper on Apify](https://apify.com/omkar-cloud/zoopla-scraper/reviews).

Here's why it matters: most people judge an Actor by its reviews before trying it. Your rating helps the next person — someone deciding whether this Actor really delivers clean Zoopla data — hit "Try for free" with confidence, and it helps the Actor rank higher in the Apify Store.

It takes only 1 second, and means the world to me.
