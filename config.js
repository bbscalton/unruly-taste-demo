/* =====================================================================
 * Unruly Taste ordering page: SITE CONFIG (DEMO)
 * ---------------------------------------------------------------------
 * ORDER_WHATSAPP = the WhatsApp number that RECEIVES orders, and that the
 * "Call / WhatsApp" buttons point to.
 *
 *   DEMO: this is Calton Andrew's test line (+592 712 9487), NOT
 *   Unruly Taste's own number. Unruly Taste has not approved going live.
 *
 *   SWAP LATER: once Unruly Taste approves, change ORDER_WHATSAPP (digits
 *   only, with country code, no "+") and ORDER_WHATSAPP_DISPLAY to the
 *   business number, then set DEMO to false.
 * ===================================================================== */
window.UT_CONFIG = {
  ORDER_WHATSAPP: '5927129487',            // <-- business order line (digits only). DEMO = Calton's line.
  ORDER_WHATSAPP_DISPLAY: '+592 712 9487', // <-- how that number is shown on the page.
  SITE_URL: 'https://bbscalton.github.io/unruly-taste-demo/', // used in receipts' reorder link
  DEMO: true,                              // shows the DEMO banner + "(DEMO)" in order messages
  DEFAULT_COUNTRY_CODE: '592',             // customers' numbers default to Guyana
  TIME_ZONE: 'America/Guyana',
  CURRENCY: 'G$'
};
