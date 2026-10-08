# images/ (DEMO placeholders: swap with real photos later)

Every image on the site lives in this folder. All food pictures are **generated illustrations**
(SVG, made by `tools/gen-images.py`) marked "DEMO IMAGE". None of them are Unruly Taste's real
photos or logo. Real Facebook photos are NOT used because the business hasn't given permission yet.

To swap: drop a real photo in this folder (JPG/WebP, about 1200x900, 4:3) and change the file name
in `app.js` (`img:` on the menu item) or in `index.html` (hero / og image).

| Slot (file)                         | Where it shows                         | Swap with (real photo)                          |
|-------------------------------------|----------------------------------------|-------------------------------------------------|
| `hero-spread.svg`                   | Top banner (index.html `.hero`)        | Signature "Unruly Taste" dish or food spread    |
| `deal-thursday-double-bubble.svg`   | Thursday Double Bubble card + sheet    | Two boxes (Hot Box + Wrap Box) side by side     |
| `deal-friday-mega-meal.svg`         | Friday Mega Meal card + sheet          | Hot Box + Wrap Box + 2 refreshers               |
| `wings-12pc.svg`                    | Wings (12pc)                           | 12 wings with sauces                            |
| `wings-with-side.svg`               | Wings + a Side                         | Chicken & waffles / wings with a side           |
| `wings-combo.svg`                   | Wings Combo                            | Wings + fries + mac & cheese                    |
| `burger-wings-combo.svg`            | Burger & Wings Combo                   | Burger + wings + fries + dipping sauces         |
| `hot-box.svg`                       | Hot Box                                | Chicken burger box with fries + mac & cheese    |
| `wrap-box.svg`                      | Wrap Box                               | Tropical chicken wrap box                       |
| `og-share.png`                      | Link preview (WhatsApp/Facebook share) | Branded share card with the real logo           |
| `favicon.svg`                       | Browser tab icon ("UT" text badge)     | Real logo (with permission)                     |

Header/footer wordmark "UNRULY TASTE" is plain CSS text (index.html `.wordmark`), not the real
logo. Swap for the logo image once approved.
