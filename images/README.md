# images/ (real, approved Unruly Taste photos)

All food pictures and the logo on the site are now **Unruly Taste's own photos/logo** (from their
Facebook page, approved by the business for this site). The old generated "DEMO IMAGE" SVG
placeholders have been removed. The top DEMO banner on the page stays (sample menu, test WhatsApp line).

Source originals live outside the repo (`/workspace/fastfood/unruly-taste-facebook-photos/` on the
build box). Every card photo here is cropped to 4:3 and resized to 800x600 WebP (each < 150 KB).

**Phone number rule:** the business phone number that appears on some of the business's graphics is NOT
approved for live use. It has been cropped out of every image here (the two promo flyers lose their
bottom contact strip; the combo photos lose the small logo/contact card in the corner). Keep it that
way when adding new images.

| File                                 | Where it shows                         | Real photo used (source)                          |
|--------------------------------------|----------------------------------------|---------------------------------------------------|
| `deal-thursday-double-bubble.webp`   | Thursday Double Bubble card + sheet    | Thursday Double Bubble promo flyer (top part, `slot-deal-thursday.png`) |
| `deal-friday-mega-meal.webp`         | Friday Mega Meal card + sheet          | Friday Mega Meal promo flyer (top part, `slot-deal-friday.png`)         |
| `wings-12pc.webp`                    | Wings (12pc)                           | Tray of mixed wings (`slot-wings-12pc.png`)       |
| `wings-with-side.webp`               | Wings + a Side                         | Wings with fries (`slot-wings-with-side.png`)     |
| `wings-combo.webp`                   | Wings Combo                            | Wings + mac & cheese box (`slot-wings-combo.png`) |
| `burger-wings-combo.webp`            | Burger & Wings Combo                   | Burger, wings, fries + sauce (`slot-burger-wings-combo.png`) |
| `hot-box.webp`                       | Hot Box                                | Chicken burger, fries + mac & cheese (`slot-hot-box.png`) |
| `wrap-box.webp`                      | Wrap Box                               | Chicken wraps + mac & cheese (`slot-wrap-box.png`) |
| `logo.webp`                          | Header + footer logo (alt "Unruly Taste") | Real logo (`logo-hires.png`, background made transparent) |
| `favicon-32.png`, `favicon-192.png`, `apple-touch-icon.png` | Browser tab / home-screen icon | Real logo (`logo-hires.png`) |
| `og-share.jpg` (1200x630)            | Link preview (WhatsApp/Facebook share) | Real logo + wings tray + Hot Box photo            |

Not used: the Facebook cover photo (`slot-cover.png`) shows the unapproved phone number and the
page has no hero slot, so it is not published. `tools/gen-images.py` is the old placeholder
generator and is no longer needed.

To swap a photo: crop to 4:3, export ~800x600 WebP under 150 KB, then change `img:` on the item
in `menu.js`.
