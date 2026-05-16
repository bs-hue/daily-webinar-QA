# QA Check Steps — Kundli Pathshala Webinar Pages

## URLs
| ID  | Type        | URL |
|-----|-------------|-----|
| PFB | Landing     | https://aap.astroarunpandit.org/kundli-pathshala-webinar-pfb/ |
| PGA | Landing     | https://aap.astroarunpandit.org/kundli-pathshala-webinar-pga/ |
| CFB | Thank You   | https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-cfb/ |
| TYP | Thank You   | https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-pga/ |
| WA  | WhatsApp    | https://aap.astroarunpandit.org/new-kundli-webinar-whatsapp-group/ |

## Date Rule
- Webinar is every **Saturday at 5:30 PM IST**
- Date shown on page must be the **next upcoming Saturday**
- If date has already passed → ❌ EXPIRED
- If date is this coming Saturday or future → ✅ VALID
- All landing pages must show the **same date** → flag ⚠️ MISMATCH if different

## Checks Per Page

### STEP 1 — PAGE LOAD
- Use Tavily to fetch the page
- Confirm page loads (no 404, 500, blank)
- Note load speed / any errors

### STEP 2 — DATE CHECK (MOST IMPORTANT)
- Find ALL dates visible on the page (visible UI only, not hidden DOM elements)
- Compare against today's date
- Next Saturday from today's date is the expected date
- Mark each date as ✅ VALID, ❌ EXPIRED, or ⚠️ MISMATCH

### STEP 3 — LINK CHECK
- Find every visible anchor/link on the page
- Check each link destination
- Mark ✅ working or ❌ broken

### STEP 4 — BUTTON CHECK
- Find every visible button (Register, Buy Now, Enroll, WhatsApp, Call, Submit, etc.)
- Note what each button does when clicked (form, payment page, popup, redirect, error, nothing)
- Mark ✅ working or ❌ broken

### STEP 5 — FORM CHECK
- Check if any registration or enquiry form is visible
- Note form fields present
- Check if form submission works
- Mark ✅ working or ❌ broken / ⚠️ not tested

### STEP 6 — CONTENT CHECK
- Spelling and grammar errors (visible text only)
- Duplicate sections
- Broken images or media

## Report Format

For each URL produce this table:

| Element | Type | Status | Notes |
|---------|------|--------|-------|
| Page Load | Page | ✅/❌ | HTTP status, load time |
| Webinar Date | Date | ✅/❌/⚠️ | Date found on page |
| [Button Name] | Button | ✅/❌ | What happened |
| [Link Name] | Link | ✅/❌ | Where it goes |
| Form | Form | ✅/❌/N/A | Submit result |
| Spelling | Content | ✅/❌ | Issues found |
| Duplicates | Content | ✅/❌ | Sections duplicated |

## Final Summary Format

```
DATE CONSISTENCY CHECK:
- PFB date: [date found]
- PGA date: [date found]
- CFB date: [date found]
- TYP date: [date found]
- All match: ✅ YES / ❌ NO

OVERALL SUMMARY:
- Total pages tested: 5
- Dates valid: X/5
- Expired dates: X
- Date mismatches: X
- Broken buttons: X
- Broken links: X
- Form issues: X
- Content issues: X
- ISSUES LIST:
  1. [issue]
  2. [issue]
```
