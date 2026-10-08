# Unruly Taste: online ordering (DEMO)

Live: https://bbscalton.github.io/unruly-taste-demo/

Mobile-first static ordering page for **Unruly Taste** (fast food, 5th Street, Alberttown, Georgetown, Guyana).
Built by Neuereatec Enterprise as a **demo**: sample menu, prices in GYD and subject to change.

- Tap menu items → choose flavour / side / boxes → cart (G$ total) → pickup or delivery.
- Checkout requires the customer's name and WhatsApp number (defaults to +592).
- "Send order on WhatsApp" opens `wa.me/<ORDER_WHATSAPP>` with a formatted order (order no., items, total,
  pickup/delivery, customer name + WhatsApp) **plus the customer receipt** and a one-tap link to send that
  receipt to the customer.
- Receipt includes a reorder link (`?reorder=…`) that refills the cart.

## Menu
`menu.js` is the single source of truth for the menu (strict JSON inside). The Unruly Taste voice bot downloads it
from the live site and builds its spoken menu from it, so page and bot stay in sync.

## Config
`config.js` → `ORDER_WHATSAPP` (digits, with country code). **Demo value is a test line, not the business's
number.** Swap it (and `ORDER_WHATSAPP_DISPLAY`, `DEMO: false`) once Unruly Taste approves.

## Images
All food images are generated demo illustrations. See `images/README.md` for the list of slots to swap.

## Plan / not built yet
See `PLAN.md` (auto-receipt via the WhatsApp bridge, "ready for pickup" callback, voice ordering).

## Deploy
GitHub Pages from `main` / root (same as the other bbscalton Pages sites). Push to `main` to publish.
