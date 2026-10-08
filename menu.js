/* Unruly Taste MENU DATA (single source of truth, DEMO / sample menu, prices in GYD).
 * Used by: this ordering page (app.js) AND the Unruly Taste voice bot, which downloads this file and
 * parses the JSON object below (keep it strict JSON: double quotes, no comments/functions inside).
 * price null = no posted solo price ("price confirmed on WhatsApp"). opts = name of a list in "lists".
 * Item ids are 2 lowercase letters (used in reorder links); option order matters for old reorder links,
 * so ADD new options at the END of a list. */
window.UT_MENU = {
 "version": 1,
 "business": {
  "name": "Unruly Taste",
  "owner": "Johntel",
  "address": "5th Street, Alberttown (between Light & Albert Street), Georgetown, Guyana",
  "pickupAddress": "5th Street, Alberttown (between Light & Albert St), Georgetown",
  "status": "Opening Soon",
  "hours": "Hours coming soon",
  "services": [
   "delivery",
   "takeout",
   "in-store pickup"
  ],
  "instagram": "@unruly_taste",
  "deliveryNote": "Delivery charges apply (confirmed on WhatsApp).",
  "extrasNote": "Refreshers and milkshakes come with combo deals only (not sold separately).",
  "payment": "Pay on pickup or delivery."
 },
 "currency": "G$",
 "lists": {
  "flavours": [
   "BBQ",
   "Honey Glaze",
   "Lemon Pepper",
   "Garlic Parmesan",
   "Thai Chili",
   "Jerk",
   "Sweet & Spicy",
   "Mango Habanero",
   "Exotic Honey Hot Jalapeño",
   "Caribbean Sunshine",
   "Firecracker",
   "Brown Sugar BBQ"
  ],
  "sides": [
   "Fries",
   "Mac & Cheese",
   "Waffles",
   "Plantain"
  ],
  "protein": [
   "Wings",
   "Strip chicken"
  ],
  "boxes": [
   "Hot Box",
   "Wrap Box"
  ]
 },
 "sections": [
  {
   "id": "deals",
   "title": "🔥 Deals"
  },
  {
   "id": "wings",
   "title": "🍗 Wings"
  },
  {
   "id": "combos",
   "title": "🍔 Combos"
  },
  {
   "id": "boxes",
   "title": "📦 Boxes"
  }
 ],
 "items": [
  {
   "id": "db",
   "sec": "deals",
   "name": "Thursday Double Bubble",
   "price": 5000,
   "day": 4,
   "dayName": "Thursday",
   "img": "deal-thursday-double-bubble.svg",
   "desc": "Any 2 boxes (Hot Box or Wrap Box), each with wings or strip chicken, for one price.",
   "groups": [
    {
     "key": "b1",
     "label": "Box 1",
     "short": "Box 1",
     "opts": "boxes"
    },
    {
     "key": "p1",
     "label": "Box 1 comes with",
     "short": "with",
     "opts": "protein"
    },
    {
     "key": "f1",
     "label": "Box 1 wing flavour",
     "short": "Flavour",
     "opts": "flavours",
     "showIf": [
      "p1",
      0
     ]
    },
    {
     "key": "b2",
     "label": "Box 2",
     "short": "Box 2",
     "opts": "boxes"
    },
    {
     "key": "p2",
     "label": "Box 2 comes with",
     "short": "with",
     "opts": "protein"
    },
    {
     "key": "f2",
     "label": "Box 2 wing flavour",
     "short": "Flavour",
     "opts": "flavours",
     "showIf": [
      "p2",
      0
     ]
    }
   ]
  },
  {
   "id": "mm",
   "sec": "deals",
   "name": "Friday Mega Meal",
   "price": 6000,
   "day": 5,
   "dayName": "Friday",
   "img": "deal-friday-mega-meal.svg",
   "desc": "1 Hot Box + 1 Wrap Box + 2 refreshers.",
   "groups": [
    {
     "key": "hp",
     "label": "Hot Box comes with",
     "short": "Hot Box with",
     "opts": "protein"
    },
    {
     "key": "hf",
     "label": "Hot Box wing flavour",
     "short": "Flavour",
     "opts": "flavours",
     "showIf": [
      "hp",
      0
     ]
    },
    {
     "key": "wp",
     "label": "Wrap Box comes with",
     "short": "Wrap Box with",
     "opts": "protein"
    },
    {
     "key": "wf",
     "label": "Wrap Box wing flavour",
     "short": "Flavour",
     "opts": "flavours",
     "showIf": [
      "wp",
      0
     ]
    }
   ]
  },
  {
   "id": "wt",
   "sec": "wings",
   "name": "Wings (12pc)",
   "price": 2500,
   "img": "wings-12pc.svg",
   "desc": "12 crispy wings tossed in your choice of 12 flavours.",
   "groups": [
    {
     "key": "f",
     "label": "Choose flavour",
     "short": "Flavour",
     "opts": "flavours"
    }
   ]
  },
  {
   "id": "ws",
   "sec": "wings",
   "name": "Wings + a Side",
   "price": 2500,
   "img": "wings-with-side.svg",
   "desc": "Wings with your pick of fries, mac & cheese, waffles or plantain.",
   "groups": [
    {
     "key": "f",
     "label": "Choose flavour",
     "short": "Flavour",
     "opts": "flavours"
    },
    {
     "key": "s",
     "label": "Choose your side",
     "short": "Side",
     "opts": "sides"
    }
   ]
  },
  {
   "id": "wc",
   "sec": "combos",
   "name": "Wings Combo",
   "price": 2500,
   "img": "wings-combo.svg",
   "desc": "Wings + fries + mac & cheese.",
   "groups": [
    {
     "key": "f",
     "label": "Choose flavour",
     "short": "Flavour",
     "opts": "flavours"
    }
   ]
  },
  {
   "id": "bw",
   "sec": "combos",
   "name": "Burger & Wings Combo",
   "price": 2800,
   "img": "burger-wings-combo.svg",
   "desc": "Burger + wings, served with fries and dipping sauces.",
   "groups": [
    {
     "key": "f",
     "label": "Choose wing flavour",
     "short": "Flavour",
     "opts": "flavours"
    }
   ]
  },
  {
   "id": "hb",
   "sec": "boxes",
   "name": "Hot Box",
   "price": null,
   "img": "hot-box.svg",
   "desc": "Chicken burger + fries + mac & cheese, with wings or strip chicken. Solo price confirmed on WhatsApp.",
   "groups": [
    {
     "key": "p",
     "label": "Comes with",
     "short": "with",
     "opts": "protein"
    },
    {
     "key": "f",
     "label": "Wing flavour",
     "short": "Flavour",
     "opts": "flavours",
     "showIf": [
      "p",
      0
     ]
    }
   ]
  },
  {
   "id": "wb",
   "sec": "boxes",
   "name": "Wrap Box",
   "price": null,
   "img": "wrap-box.svg",
   "desc": "Tropical chicken wrap + fries + mac & cheese, with wings or strip chicken. Solo price confirmed on WhatsApp.",
   "groups": [
    {
     "key": "p",
     "label": "Comes with",
     "short": "with",
     "opts": "protein"
    },
    {
     "key": "f",
     "label": "Wing flavour",
     "short": "Flavour",
     "opts": "flavours",
     "showIf": [
      "p",
      0
     ]
    }
   ]
  }
 ]
};
