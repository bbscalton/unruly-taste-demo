# Unruly Taste ordering: plan & status (DEMO)

## What works today (static GitHub Pages site)
| Step | How | Automated? |
|---|---|---|
| Browse menu, choose flavour/side/box, qty, cart total in G$ | In the page (cart saved on the phone) | ✅ automatic |
| Pickup or delivery (+ address) | Checkout form | ✅ automatic |
| Customer must give name + WhatsApp number (default +592) | Checkout validation | ✅ automatic |
| Order sent to the order line | Opens `wa.me/<ORDER_WHATSAPP>` with the formatted order; **customer taps Send** | ⚠️ semi: customer taps Send |
| Receipt shown to customer | Confirmation screen: Copy / Save (.txt) / Share receipt + reorder link | ✅ automatic (on screen) |
| Receipt to customer's WhatsApp | Order message contains the receipt **and** a ready `wa.me/<customer>?text=<receipt>` link. Staff tap it, then Send | ❌ manual (1 tap + Send) |
| Reorder | Receipt link `?reorder=…` refills the cart | ✅ automatic |

ORDER_WHATSAPP is set in `config.js`. In this demo it is a test line, not the business's own number.

## Planned: bridge auto-sends the receipt (not built)
The order line is linked to a WhatsApp Web bridge (Playwright-driven WhatsApp Web session, the one
that already auto-answers voice calls). Plan:
1. **Detect**: add a message watcher in the bridge: poll/observe the chat list for unread messages whose
   text starts with `🍗 *NEW ORDER · UNRULY TASTE*`. Parse `Order:`, `Customer WhatsApp:` (the `Chat:
   https://wa.me/<digits>` line is machine-readable) and the block between `===== RECEIPT FOR CUSTOMER =====`
   and `================================`.
2. **Guard**: only act on orders whose number matches `UT-YYMMDD-XXXX`, de-duplicate by order number
   (small JSON store), rate-limit (e.g. 10/min), never message a number more than once per order, and
   skip while a voice call is active (the same browser page handles calls; receipts wait in a queue).
3. **Send**: reuse the bridge's existing "open chat by number" helper to open the customer's chat, type the
   receipt text, press Send, verify the message bubble appears, then return to the chat list.
4. **Confirm**: reply in the order chat "Receipt sent to +592 …" (or "Receipt FAILED: …") so staff see it.
5. **Toggle**: feature flag (`AUTO_RECEIPT=off|on`), off by default; test against a test number first.
Better long-term option: WhatsApp Business Cloud API (official, template "order receipt"), which avoids
browser automation for messaging; needs a Meta Business account + verified number.

## Planned feature (NOT built): "ready for pickup" callback
Staff reply `ready` (or `ready UT-261008-KW6Y`) in the customer's/order chat → bridge detects the
keyword from a staff message → looks up the order's customer number → places a WhatsApp voice call
to the customer and plays a short message ("Hi <name>, your Unruly Taste order <no> is ready for
pickup at 5th Street, Alberttown"), with a text fallback if the call isn't answered. Needs: the
message watcher above, an order store (order no → customer number), the bridge's outbound-call path,
a TTS clip, and rules (only staff numbers can trigger, once per order, business hours only).

## Planned: AI voice line for Unruly Taste
A menu-ordering voice persona (separate bot backend with the same API as the existing voice bot:
caller check, voice chunk/end, TTS) could take orders by voice and send the same order format.
Not built in this demo.
