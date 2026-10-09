# Khoj Doot — SME Website Component Catalogue

> **Version:** 1.0.0  
> **Status:** Production Architecture Standard  
> **Scope:** Reusable Component Library for Regional Micro & Informal Enterprises  

---

## 1. Overview & Architectural Principles

This catalogue defines the standard modular component ecosystem for **Khoj Doot (खोजदूत)**. Designed specifically for informal, micro, and small enterprises (SMEs)—such as home kitchens, handmade artisans, neighborhood repair/tailoring services, and local traders—this library strictly separates **Business Facts**, **Component Structure**, and **Design Systems**.

### Three-Layer Separation

```text
┌────────────────────────────────────────────────────────┐
│ 1. Business Data Layer (Ground-Truth Facts)            │
│    Owner name, verified contacts, real offerings,      │
│    authentic location, verified photos, stated policies │
└──────────────────────────┬─────────────────────────────┘
                           │ Consumed by
┌──────────────────────────▼─────────────────────────────┐
│ 2. Component Library Layer (Semantic Structure)        │
│    Layout trees, fallbacks, accessibility, responsive  │
│    behavior, business-aware conditional visibility     │
└──────────────────────────┬─────────────────────────────┘
                           │ Styled by
┌──────────────────────────▼─────────────────────────────┐
│ 3. Design System Layer (Visual Tokens & Variants)      │
│    Colors, typography, border-radius, spacing,         │
│    image treatments, and presentation personalities    │
└────────────────────────────────────────────────────────┘
```

### Trust & Factual Accuracy Guarantee

* **Zero Hallucination Rule:** Components must *never* fabricate pricing, reviews, star ratings, government registrations (FSSAI/GST), delivery promises, or opening hours.
* **Missing-Data Fallback:** If optional data is missing, the component either falls back gracefully or is omitted entirely.
* **Privacy by Default:** For home-based businesses, private residential door numbers are withheld unless explicitly permitted for public storefront visits. Neighborhood or city coverage is displayed instead.

---

## 2. Component Families & Detailed Specifications

---

### Family 1: Business Identity & First Impression

#### Component `ID-01`: Top Announcement & Operational Bar
* **Component ID:** `ID-01-ANNOUNCEMENT`
* **Customer Problem Solved:** Communicates immediate operational reality (e.g., "Orders open for Sunday feast" or "Vacation notice: Dispatch resumes Monday") to prevent customer friction.
* **Required Data:** `status_message` (string).
* **Optional Data:** `badge_type` (`info`, `urgent`, `alert`), `action_link` (URL).
* **Show/Hide Condition:** Hidden if `status_message` is null or empty.
* **Supported Layout Variants:**
  - *Compact Banner:* Single line marquee/ticker atop the site.
  - *Accent Pill:* Centered pill above the header navigation.
* **Interactions:** Dismiss button (`aria-label="Close announcement"`), optional tap-to-action.
* **Mobile vs. Desktop:** Desktop shows full text horizontally; mobile truncates with marquee or stacked 2-line wrap.
* **Accessibility:** `role="region" aria-label="Announcement"`, WCAG AA contrast against background.
* **Missing-Data Fallback:** Entire component collapses cleanly (0px height).
* **Trust & Factual Constraint:** Text must originate directly from verified business input.

#### Component `ID-02`: Brand Header & Navigation
* **Component ID:** `ID-02-HEADER`
* **Customer Problem Solved:** Establishes merchant identity and provides immediate navigation and contact triggers.
* **Required Data:** `business_name` (string).
* **Optional Data:** `logo_url` (image URL), `category_tag` (string), `phone` (string), `languages` (list).
* **Show/Hide Condition:** Always visible.
* **Supported Layout Variants:**
  - *Minimal Centered:* Logo/name centered, contact buttons below.
  - *Split Navigation:* Brand on left, direct call/WhatsApp CTA on right.
  - *Artisan Monogram:* Stylized typographic seal with regional script subtitle.
* **Interactions:** Tap logo to scroll to top; tap phone/WhatsApp triggers dialer or chat.
* **Mobile vs. Desktop:** Mobile sticks compact sticky top-bar with direct call icon; desktop displays full brand name with category badge.
* **Accessibility:** `<header role="banner">`, semantic `<h1>` or `<span>`, keyboard focusable CTA.
* **Missing-Data Fallback:** If `logo_url` is missing, renders accessible typographic monogram.
* **Trust & Factual Constraint:** Never displays unofficial verification checkmarks.

#### Component `ID-03`: Hero Showcase Banner
* **Component ID:** `ID-03-HERO`
* **Customer Problem Solved:** Gives customers a 3-second comprehension of what the business does, who runs it, and how to engage.
* **Required Data:** `business_name` (string), `primary_offering` (string).
* **Optional Data:** `hero_image_url` (image URL), `location_summary` (string), `phone` (string), `whatsapp` (string), `badge` (string).
* **Show/Hide Condition:** Always visible.
* **Supported Layout Variants:**
  - *Full Bleed Editorial:* High-impact visual background with dark contrast overlay.
  - *Split Card Layout:* Brand headline and primary action on left; photography card on right.
  - *Warm Kitchen Banner:* Rustic background container with prominent portion/order CTA.
* **Interactions:** Direct CTA click ("Order on WhatsApp", "Call Now", "Explore Offerings").
* **Mobile vs. Desktop:** Desktop uses 2-column or high-aspect ratio container; mobile stacks content vertically with thumb-accessible CTA.
* **Accessibility:** `<h1>` heading tag, descriptive `alt` for hero image, 48px minimum touch target for primary CTA.
* **Missing-Data Fallback:** If `hero_image_url` is absent, uses theme-specific geometric or warm tinted background container with typography.
* **Trust & Factual Constraint:** Headline must reflect actual products, not inflated claims.

---

### Family 2: Products, Services & Pricing

#### Component `PROD-01`: Core Offering Grid & Menu
* **Component ID:** `PROD-01-OFFERING-GRID`
* **Customer Problem Solved:** Displays what the merchant produces or sells, with clear portion/item names and stated prices.
* **Required Data:** `items` (list of objects containing `title`).
* **Optional Data:** `description`, `price` (number), `unit` (e.g., "per kg", "per tiffin", "per piece"), `image_url`, `tags` (e.g., "Pure Veg", "Handmade").
* **Show/Hide Condition:** Visible if `items` has at least 1 item; hidden if empty.
* **Supported Layout Variants:**
  - *Menu Card Stack:* Traditional restaurant/tiffin style, horizontal rows with price right-aligned.
  - *Visual Grid Card:* Visual cards with photo at top, title, description, and price badge below.
  - *Service Tier:* Service cards with bulleted feature checklist and consultation button.
* **Interactions:** Optional item selection to generate pre-filled WhatsApp message.
* **Mobile vs. Desktop:** Desktop displays 3-column responsive grid; mobile displays 1-column card stack.
* **Accessibility:** Semantically structured `<article>` or `<ul>`/`<li>`, aria price format.
* **Missing-Data Fallback:** If price is absent, displays "Price on inquiry" or omits price tag cleanly. Never displays ₹0.
* **Trust & Factual Constraint:** Prices must strictly match merchant input. Never fabricate discounted prices.

#### Component `PROD-02`: Pricing Tier & Rate Card
* **Component ID:** `PROD-02-RATE-CARD`
* **Customer Problem Solved:** Explains service rates, subscription plans (e.g., monthly tiffins), or batch pricing.
* **Required Data:** `rate_statement` or `tiers` (list).
* **Optional Data:** `validity`, `minimum_order`, `notes`.
* **Show/Hide Condition:** Visible only if rates/pricing are explicitly provided in seed facts.
* **Supported Layout Variants:**
  - *Tier Comparison:* 2 or 3 parallel boxes (e.g., "Daily", "Weekly", "Monthly").
  - *Simple Rate Note:* Clean highlight banner stating transparent pricing rules.
* **Interactions:** Tap tier to select and trigger WhatsApp pre-filled inquiry.
* **Mobile vs. Desktop:** Stacks vertically on mobile with swipe indicators.
* **Accessibility:** High-contrast text, tabular accessibility tags if comparative.
* **Missing-Data Fallback:** Omitted if no rate statements exist.
* **Trust & Factual Constraint:** Hidden charges must never be obscured.

---

### Family 3: Trust & Proof

#### Component `TRUST-01`: Maker Story & Authenticity
* **Component ID:** `TRUST-01-MAKER-STORY`
* **Customer Problem Solved:** Builds emotional trust by introducing the person behind the craft or food.
* **Required Data:** `story_text` (string) OR `owner_name` (string).
* **Optional Data:** `owner_photo` (URL), `experience_years` (number), `heritage_background` (string).
* **Show/Hide Condition:** Visible if `story_text` or `owner_name` is present.
* **Supported Layout Variants:**
  - *Editorial Quote:* Large serif quotation with author sign-off and photo.
  - *Warm Portrait Card:* Owner picture beside bio narrative.
  - *Heritage Timeline:* Compact milestones (e.g., "Started in 2018 in Nashik").
* **Interactions:** Static read; optional "Read More" disclosure.
* **Mobile vs. Desktop:** Responsive side-by-side on desktop; portrait image stacks above narrative on mobile.
* **Accessibility:** Semantic `<blockquote>` or `<section>`, clear image `alt` text.
* **Missing-Data Fallback:** If photo is missing, displays typographic signature card.
* **Trust & Factual Constraint:** Only claims authentic facts verified in the business profile.

#### Component `TRUST-02`: Quality & Hygiene Pledge
* **Component ID:** `TRUST-02-QUALITY-PLEDGE`
* **Customer Problem Solved:** Reassures customers about cleanliness, pure ingredients, or genuine handmade materials.
* **Required Data:** `pledge_points` (list of strings).
* **Optional Data:** `icon_keys`, `verification_note`.
* **Show/Hide Condition:** Visible only when specific quality facts are present (e.g., "Pure Veg", "No Preservatives", "100% Pure Silk").
* **Supported Layout Variants:**
  - *Pill Badges:* Horizontal scrollable pill row.
  - *3-Column Feature Icons:* Illustrated icons with brief explanations.
* **Interactions:** Informational only.
* **Mobile vs. Desktop:** Wraps to 2x2 grid on mobile or horizontal scroll row.
* **Accessibility:** SVG icons marked `aria-hidden="true"`, text conveys full meaning.
* **Missing-Data Fallback:** Completely omitted if no explicit pledges exist.
* **Trust & Factual Constraint:** Never fabricate certifications like "FSSAI Certified" unless proof is supplied.

---

### Family 4: Ordering, Booking & Conversion

#### Component `CONV-01`: One-Click WhatsApp Ordering Action
* **Component ID:** `CONV-01-WHATSAPP-ACTION`
* **Customer Problem Solved:** Bridges the discovery-to-order gap using the #1 familiar messaging tool for Indian SMEs.
* **Required Data:** `phone` or `whatsapp_number` (string).
* **Optional Data:** `default_message` (string), `business_name` (string), `item_context` (string).
* **Show/Hide Condition:** Visible whenever a valid mobile number is present.
* **Supported Layout Variants:**
  - *Floating Action Button (FAB):* Persistent bottom-right WhatsApp button.
  - *Full-Width Conversion Banner:* Prominent green button within page flow.
  - *Inline Card Button:* Attached directly to each product card.
* **Interactions:** Opens WhatsApp Web on desktop or WhatsApp App on mobile with URI encoded pre-filled text.
* **Mobile vs. Desktop:** FAB anchored to bottom thumb zone on mobile; desktop shows full banner CTA.
* **Accessibility:** Focus ring, `aria-label="Order on WhatsApp from {business_name}"`.
* **Missing-Data Fallback:** Replaced by direct `tel:` call button if WhatsApp is indeterminate.
* **Trust & Factual Constraint:** Generates friendly customer message without fake order promises.

#### Component `CONV-02`: Custom Order & Inquiry Form
* **Component ID:** `CONV-02-CUSTOM-INQUIRY`
* **Customer Problem Solved:** Allows customers with specific requirements (e.g., bulk catering, custom blouse stitching, bulk gifts) to initiate dialogue.
* **Required Data:** `phone` (string).
* **Optional Data:** `inquiry_types` (list of strings, e.g., ["Bulk Order", "Custom Design", "Home Delivery"]).
* **Show/Hide Condition:** Displayed for crafts, tailoring, and catering businesses.
* **Supported Layout Variants:**
  - *WhatsApp Link Generator:* Dynamic dropdown that formats a pre-filled WhatsApp message.
  - *Direct Contact Form:* Clean native form that dispatches inquiry to backend or merchant email/WhatsApp.
* **Interactions:** Dropdown selection updates contact prompt.
* **Mobile vs. Desktop:** Single column on all viewports for ease of typing.
* **Accessibility:** Explicit `<label>` elements for every input, keyboard accessible.
* **Missing-Data Fallback:** Falls back to simple click-to-call link.
* **Trust & Factual Constraint:** Never implies instant 24/7 automated response unless stated.

---

### Family 5: Delivery, Shipping, Pickup & Fulfilment

#### Component `FUL-01`: Local Delivery & Service Radius
* **Component ID:** `FUL-01-DELIVERY-RADIUS`
* **Customer Problem Solved:** Eliminates disappointment by telling customers if their neighborhood is served.
* **Required Data:** `service_areas` (list of strings) OR `city` (string).
* **Optional Data:** `delivery_fee_policy`, `minimum_order`, `lead_time`.
* **Show/Hide Condition:** Visible when delivery data exists.
* **Supported Layout Variants:**
  - *Area Tag Cloud:* Visual chips for each covered locality (e.g., "Gangapur Road", "College Road").
  - *Fulfilment Highlights:* 2-column card comparing "Pickup Available" vs "Home Delivery".
* **Interactions:** Informational chips.
* **Mobile vs. Desktop:** Flex-wrap on mobile and desktop.
* **Accessibility:** Semantic list tags.
* **Missing-Data Fallback:** Displays generic city location ("Serving {city} and nearby areas").
* **Trust & Factual Constraint:** Do not claim "Free Delivery" unless verified.

#### Component `FUL-02`: Pickup & Advance Notice Guidelines
* **Component ID:** `FUL-02-PICKUP-POLICY`
* **Customer Problem Solved:** Sets expectations for lead times (e.g., "Order 4 hours in advance", "Fresh batch daily at 12 PM").
* **Required Data:** `lead_time` OR `pickup_window` (string).
* **Optional Data:** `landmark_note`.
* **Show/Hide Condition:** Visible if lead time or pickup guidelines are stated.
* **Supported Layout Variants:**
  - *Highlighted Clock Card:* Icon with clean lead time notice.
  - *Numbered 3-Step Flow:* "1. Choose -> 2. Confirm Notice -> 3. Collect Fresh".
* **Interactions:** Static informative.
* **Mobile vs. Desktop:** Compact on mobile.
* **Accessibility:** High-contrast text, icon `aria-hidden="true"`.
* **Missing-Data Fallback:** Omitted if no lead time constraints exist.
* **Trust & Factual Constraint:** Reflects real merchant capacity.

---

### Family 6: Local Discovery & Visiting

#### Component `LOC-01`: Location & Landmark Pin
* **Component ID:** `LOC-01-LANDMARK-PIN`
* **Customer Problem Solved:** Directs customers to the workshop, shop, or pickup point with recognizable local landmarks.
* **Required Data:** `city` (string).
* **Optional Data:** `address` (string), `landmark` (string), `map_url` (URL), `is_residential` (boolean).
* **Show/Hide Condition:** Always visible.
* **Supported Layout Variants:**
  - *Storefront Location:* Full address, landmark, and "Open in Google Maps" button.
  - *Privacy-Protected Area:* Neighborhood & City only (e.g., "Near Sambhaji Stadium, Nashik") for home kitchens.
* **Interactions:** Click opens Google Maps or Apple Maps app.
* **Mobile vs. Desktop:** Full card width on mobile with prominent direction icon.
* **Accessibility:** Map link opens with `rel="noopener noreferrer"` and descriptive text.
* **Missing-Data Fallback:** If full address is omitted or residential, displays neighborhood/city only.
* **Trust & Factual Constraint:** **Zero exposure of private domestic home numbers** without explicit owner consent.

#### Component `LOC-02`: Hours & Visiting Schedule
* **Component ID:** `LOC-02-HOURS`
* **Customer Problem Solved:** Prevents wasted visits or calls outside operational hours.
* **Required Data:** `hours` (string or structured schedule).
* **Optional Data:** `weekly_off_day` (e.g., "Closed on Mondays").
* **Show/Hide Condition:** Visible if hours are specified.
* **Supported Layout Variants:**
  - *Today's Status Badge:* "Open Today: 10:00 AM - 7:00 PM".
  - *Full Schedule Table:* Compact daily table.
* **Interactions:** Static.
* **Mobile vs. Desktop:** Clean 2-column row (Day | Hours).
* **Accessibility:** Semantic tabular markup or definition list (`<dl>`).
* **Missing-Data Fallback:** Displays "Contact for current availability".
* **Trust & Factual Constraint:** Never assume standard 9-5 hours for informal home makers.

---

### Family 7: Education & Decision Support

#### Component `EDU-01`: Frequently Asked Questions (FAQ)
* **Component ID:** `EDU-01-FAQ-ACCORDION`
* **Customer Problem Solved:** Answers recurring buyer questions (e.g., "Is food spicy?", "Can I customize colours?", "How long does delivery take?").
* **Required Data:** `faq_items` (list of objects with `question` and `answer`).
* **Optional Data:** `category_filter`.
* **Show/Hide Condition:** Visible if at least 1 FAQ item exists.
* **Supported Layout Variants:**
  - *Accessible Accordion:* Expandable details/summary elements.
  - *Two-Column Q&A List:* Static open view for short FAQs.
* **Interactions:** Native `<details><summary>` toggle with smooth accordion animation.
* **Mobile vs. Desktop:** Full width on mobile; max-width 780px on desktop.
* **Accessibility:** Native keyboard navigation with `Enter` and `Space`, screen reader accessible.
* **Missing-Data Fallback:** Omitted if no FAQs provided.
* **Trust & Factual Constraint:** Only states accurate answers directly relevant to the merchant.

#### Component `EDU-02`: Craft & Material Guide
* **Component ID:** `EDU-02-MATERIAL-GUIDE`
* **Customer Problem Solved:** Educates buyers on handmade materials (e.g., "Silk Thread on Acrylic Base", "100% Pure Ghee", "Hand-painted Terracotta").
* **Required Data:** `materials` or `ingredients` (list of strings).
* **Optional Data:** `care_instructions` (string).
* **Show/Hide Condition:** Visible for craft, jewellery, and specialty food businesses with material data.
* **Supported Layout Variants:**
  - *Tag Showcase:* Pill tags with icon accents.
  - *Illustrated Guide:* Detail cards showing care tips.
* **Interactions:** Static.
* **Mobile vs. Desktop:** Horizontal scroll or flex wrap on mobile.
* **Accessibility:** Descriptive text.
* **Missing-Data Fallback:** Omitted if not provided.
* **Trust & Factual Constraint:** True to verified material disclosures.

---

### Family 8: Social Proof & Engagement

#### Component `SOC-01`: Verified Customer Experiences
* **Component ID:** `SOC-01-TESTIMONIALS`
* **Customer Problem Solved:** Builds buyer confidence through authentic feedback from real local patrons.
* **Required Data:** `reviews` (list of objects with `quote` and `customer_name` or `source`).
* **Optional Data:** `date`, `item_ordered`.
* **Show/Hide Condition:** Visible ONLY if actual verified testimonials are provided.
* **Supported Layout Variants:**
  - *Quote Cards Carousel:* Horizontal swipeable cards.
  - *Masonry Testimonial Wall:* Editorial masonry blocks.
* **Interactions:** Swipe on mobile; scroll on desktop.
* **Mobile vs. Desktop:** Single card visible at a time on mobile; 3-card grid on desktop.
* **Accessibility:** `<blockquote>`, `<cite>`, contrast checked.
* **Missing-Data Fallback:** Completely omitted if no real reviews exist. **NEVER RENDER FAKE 5-STAR REVIEWS.**
* **Trust & Factual Constraint:** Strict prohibition against generative AI fabrication of fake customer quotes.

#### Component `SOC-02`: Community & Word-of-Mouth Recognition
* **Component ID:** `SOC-02-COMMUNITY-PROOF`
* **Customer Problem Solved:** Validates local reputation (e.g., "Serving Nashik foodies since 2021", "Featured at local Diwali exhibition").
* **Required Data:** `proof_text` (string).
* **Optional Data:** `badge_icon`.
* **Show/Hide Condition:** Visible if historical community milestones exist.
* **Supported Layout Variants:**
  - *Metric Counter Strip:* "500+ Happy Families", "5+ Years of Trust".
  - *Simple Badge:* Understated seal near hero or footer.
* **Interactions:** Static.
* **Mobile vs. Desktop:** Stacked vertically on mobile.
* **Accessibility:** Accessible text.
* **Missing-Data Fallback:** Omitted if unverified.
* **Trust & Factual Constraint:** Only displays true verified milestones.

---

### Family 9: Policies & Footer

#### Component `POL-01`: Terms, Ordering Notice & Payments
* **Component ID:** `POL-01-TERMS-PAYMENT`
* **Customer Problem Solved:** Clarifies how transactions work (e.g., "UPI and Cash accepted", "Advance payment for bulk orders", "No returns on fresh food").
* **Required Data:** `payment_methods` (list) OR `cancellation_policy` (string).
* **Optional Data:** `upis_accepted` (boolean).
* **Show/Hide Condition:** Visible if policy or payment methods are specified.
* **Supported Layout Variants:**
  - *Icon Strip:* Accepted payment icons (UPI, GPay, PhonePe, Cash).
  - *Notice Card:* Bulleted policy card.
* **Interactions:** Static.
* **Mobile vs. Desktop:** Wrap on mobile.
* **Accessibility:** Clear readable text.
* **Missing-Data Fallback:** Displays standard regional payment availability (e.g., "UPI / Cash").
* **Trust & Factual Constraint:** Does not claim online card processing unless verified.

#### Component `POL-02`: Site Footer & Digital Card Link
* **Component ID:** `POL-02-FOOTER`
* **Customer Problem Solved:** Bottom anchor with quick contacts, language switcher link, and verified Khoj Doot merchant badge.
* **Required Data:** `business_name` (string).
* **Optional Data:** `phone`, `city`, `khoj_card_url`, `copyright_year`.
* **Show/Hide Condition:** Always visible.
* **Supported Layout Variants:**
  - *Modern Compact:* Single bar with copyright and direct call icon.
  - *Editorial Comprehensive:* Brand summary, quick links, and network badge.
* **Interactions:** Quick action buttons.
* **Mobile vs. Desktop:** Mobile provides sticky bottom action bar; desktop shows full footer.
* **Accessibility:** Semantic `<footer>`, high contrast.
* **Missing-Data Fallback:** Uses current year and basic business name.
* **Trust & Factual Constraint:** Links to verified Khoj Doot card endpoint.

---

### Family 10: Photos, Video & Visual Storytelling

#### Component `VIS-01`: Real Photography Gallery
* **Component ID:** `VIS-01-PHOTO-GALLERY`
* **Customer Problem Solved:** Showcases real workshop products, food packaging, or finished craft items.
* **Required Data:** `photos` (list of photo URLs or filenames).
* **Optional Data:** `captions` (list of strings).
* **Show/Hide Condition:** Visible if at least 1 authentic photo exists; hidden if empty.
* **Supported Layout Variants:**
  - *Curated Photo Grid:* 2x2 or 3x3 responsive grid with rounded corners.
  - *Masonry Mosaic:* Dynamic heights for crafts and fashion.
  - *Horizontal Filmstrip:* Swipeable row with subtle momentum scroll.
* **Interactions:** Tap to enlarge or view full photo.
* **Mobile vs. Desktop:** 2-column on mobile, 3- or 4-column on desktop.
* **Accessibility:** Explicit `alt` descriptions, lazy loading `<img loading="lazy">`.
* **Missing-Data Fallback:** If no photos exist, component collapses cleanly. Do not use generic stock photos that mislead customers.
* **Trust & Factual Constraint:** Only renders genuine merchant photos.

#### Component `VIS-02`: Process & Workshop Snapshot
* **Component ID:** `VIS-02-PROCESS-SNAPSHOT`
* **Customer Problem Solved:** Demonstrates how items are made (e.g., dough kneading, silk thread winding, embroidery machine).
* **Required Data:** `process_steps` (list of objects with `step_title` and `description`).
* **Optional Data:** `step_image_url`.
* **Show/Hide Condition:** Visible when merchant provides creation workflow details.
* **Supported Layout Variants:**
  - *Numbered Cards:* 1-2-3 sequential cards.
  - *Visual Timeline:* Step-by-step timeline.
* **Interactions:** Static.
* **Mobile vs. Desktop:** Stacked vertically on mobile.
* **Accessibility:** Ordered list `<ol>` semantics.
* **Missing-Data Fallback:** Omitted if absent.
* **Trust & Factual Constraint:** Must describe actual maker process.

---

### Family 11: Accessibility, Language & Low-Bandwidth Support

#### Component `ACC-01`: Regional Language Switcher
* **Component ID:** `ACC-01-LANG-SWITCHER`
* **Customer Problem Solved:** Enables non-English native speakers (e.g., Marathi, Hindi) to read in their comfort language.
* **Required Data:** `available_languages` (list of language codes, e.g., `["mr", "hi", "en"]`).
* **Optional Data:** `current_language` (string).
* **Show/Hide Condition:** Visible when multi-language content is available.
* **Supported Layout Variants:**
  - *Header Pill Toggle:* "मराठी | English | हिंदी".
  - *Dropdown Selector:* Compact native select.
* **Interactions:** Toggles active language and dynamically updates text content.
* **Mobile vs. Desktop:** Fixed in header or floating pill.
* **Accessibility:** `aria-label="Select language"`, proper `lang` attributes.
* **Missing-Data Fallback:** Defaults to primary language (e.g., Marathi `mr-IN`).
* **Trust & Factual Constraint:** Language translations must remain faithful to source facts.

#### Component `ACC-02`: Low-Bandwidth "Lite Mode" Toggle & Print Card
* **Component ID:** `ACC-02-LITE-MODE`
* **Customer Problem Solved:** Ensures immediate loading on 2G/3G mobile networks in semi-urban India.
* **Required Data:** None (utility component).
* **Optional Data:** `save_data_header`.
* **Show/Hide Condition:** Always available.
* **Supported Layout Variants:**
  - *Header Toggle:* "Text Only / Data Saver".
  - *Printable Rate Card Link:* Clean printable view.
* **Interactions:** Disables heavy background images and applies high-contrast typography.
* **Mobile vs. Desktop:** Optimized for mobile touch.
* **Accessibility:** High-contrast AAA compliant.
* **Missing-Data Fallback:** Progressive enhancement.
* **Trust & Factual Constraint:** Never hides core contact or pricing data.

---

### Family 12: Operational & Exceptional States

#### Component `OPS-01`: Batch & Availability Status Alert
* **Component ID:** `OPS-01-BATCH-ALERT`
* **Customer Problem Solved:** Prevents orders when stock is depleted or kitchen is full (e.g., "Today's lunch tiffins fully booked! Accepting dinner pre-orders till 4 PM").
* **Required Data:** `alert_status` (`available`, `limited_batch`, `sold_out`, `preorder_only`).
* **Optional Data:** `cutoff_time` (string), `next_batch_date` (string).
* **Show/Hide Condition:** Visible when operational status is non-standard.
* **Supported Layout Variants:**
  - *Warning Toast / Banner:* High visibility amber/red top alert.
  - *Badge Overlay:* Pill badge next to item names.
* **Interactions:** Informative; CTA directs to pre-order for next cycle.
* **Mobile vs. Desktop:** Sticks above hero on mobile.
* **Accessibility:** `role="status"` or `aria-live="polite"`.
* **Missing-Data Fallback:** Omitted when normal operations apply.
* **Trust & Factual Constraint:** Accurately reflects real-time stock/capacity.

#### Component `OPS-02`: Missing-Data Graceful Fallback Container
* **Component ID:** `OPS-02-FALLBACK-CONTAINER`
* **Customer Problem Solved:** Prevents broken layouts or empty gray voids when a merchant hasn't provided photos, menus, or pricing.
* **Required Data:** `component_name` (string).
* **Optional Data:** `prompt_text` (string).
* **Show/Hide Condition:** Triggered automatically when required component fields are missing.
* **Supported Layout Variants:**
  - *Gentle Inquire Box:* "Full catalogue available on WhatsApp — Click to message".
  - *Typographic Monogram Placeholder:* Geometric monogram instead of missing image.
* **Interactions:** Directs inquiry to merchant.
* **Mobile vs. Desktop:** Resizes cleanly.
* **Accessibility:** Clear descriptive text.
* **Missing-Data Fallback:** Self-contained fallback.
* **Trust & Factual Constraint:** Transparently discloses that details are available directly from owner.

---

## 3. Summary Component Matrix

| Family | Component ID | Component Name | Default Food | Default Craft | Default Service |
|---|---|---|:---:|:---:|:---:|
| 1. Identity | `ID-01` | Top Announcement Bar | Optional | Optional | Optional |
| 1. Identity | `ID-02` | Brand Header & Nav | **Yes** | **Yes** | **Yes** |
| 1. Identity | `ID-03` | Hero Showcase Banner | **Yes** | **Yes** | **Yes** |
| 2. Offerings | `PROD-01` | Core Offering Grid / Menu | **Yes (Menu)** | **Yes (Gallery)** | **Yes (Services)** |
| 2. Offerings | `PROD-02` | Pricing Tier / Rate Card | **Yes (Tiffin Rate)**| Optional | **Yes (Quotes)** |
| 3. Trust | `TRUST-01` | Maker Story & Authenticity | Optional | **Yes (Maker)** | Optional |
| 3. Trust | `TRUST-02` | Quality & Hygiene Pledge | **Yes (Hygiene)** | **Yes (Materials)**| **Yes (Guarantee)**|
| 4. Conversion | `CONV-01` | WhatsApp One-Click Action | **Yes** | **Yes** | **Yes** |
| 4. Conversion | `CONV-02` | Custom Inquiry Form | Optional | **Yes (Custom)** | **Yes (Consult)** |
| 5. Fulfilment | `FUL-01` | Local Delivery Radius | **Yes (Areas)** | Optional | **Yes (Service Area)**|
| 5. Fulfilment | `FUL-02` | Pickup & Advance Notice | **Yes (Lead Time)**| Optional | Optional |
| 6. Discovery | `LOC-01` | Location & Landmark Pin | **Yes (Protected)**| **Yes (City/Pin)**| **Yes (Landmark)** |
| 6. Discovery | `LOC-02` | Hours & Schedule | **Yes (Meal Times)**| Optional | **Yes (Open Hours)**|
| 7. Education | `EDU-01` | Frequently Asked Questions | Optional | Optional | Optional |
| 7. Education | `EDU-02` | Craft & Material Guide | Optional | **Yes** | Optional |
| 8. Social Proof | `SOC-01` | Verified Experiences | Optional | Optional | Optional |
| 8. Social Proof | `SOC-02` | Community Recognition | Optional | Optional | Optional |
| 9. Policies | `POL-01` | Terms & Payments | **Yes** | **Yes** | **Yes** |
| 9. Policies | `POL-02` | Site Footer & Digital Card | **Yes** | **Yes** | **Yes** |
| 10. Visual | `VIS-01` | Real Photography Gallery | **Yes** | **Yes** | Optional |
| 10. Visual | `VIS-02` | Process / Workshop Snapshot | Optional | **Yes** | Optional |
| 11. Access | `ACC-01` | Regional Language Switcher | **Yes** | **Yes** | **Yes** |
| 11. Access | `ACC-02` | Lite Mode & Low Bandwidth | **Yes** | **Yes** | **Yes** |
| 12. Ops | `OPS-01` | Batch / Availability Alert | **Yes** | Optional | Optional |
| 12. Ops | `OPS-02` | Graceful Fallback Container| **Yes** | **Yes** | **Yes** |

