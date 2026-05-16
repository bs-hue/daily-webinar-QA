# Kundli Pathshala — Automated QA Runner

## This is the daily automated prompt for Claude Code

When this routine runs, Claude must:

1. Use Tavily to check each URL below
2. Follow all steps in qa_steps.md
3. Compile the full report
4. Run generate_and_upload.py to create the PDF
5. Upload the PDF to Google Drive using the Drive connector (folder ID: 1OBzjU-FplLV5JJg1xCw514Y3u7o92glv)

---

## AUTOMATED PROMPT

Run the full Kundli Pathshala webinar QA check now. Today's date is used automatically.

### URLs to check:

1. https://aap.astroarunpandit.org/kundli-pathshala-webinar-pfb/
2. https://aap.astroarunpandit.org/kundli-pathshala-webinar-pga/
3. https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-cfb/
4. https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-pga/
5. https://aap.astroarunpandit.org/new-kundli-webinar-whatsapp-group/

### For each URL run these checks:

**STEP 1 — PAGE LOAD**
Use Tavily extract to load the page. Confirm it loads successfully. Note any errors.

**STEP 2 — DATE CHECK (MOST IMPORTANT)**
- Find all dates visible on the page (UI only, not hidden DOM elements)
- Today's date: use current date automatically
- Webinar is every Saturday at 5:30 PM IST
- Next upcoming Saturday = expected date
- Mark: ✅ VALID (future date), ❌ EXPIRED (past date), ⚠️ MISMATCH (different across pages)
- Compare all landing pages — they must show the same date

**STEP 3 — LINK CHECK**
Find all visible links. Check each destination. Mark ✅ working or ❌ broken.

**STEP 4 — BUTTON CHECK**
Find all visible buttons (Register, Buy Now, Enroll, WhatsApp, Call, Submit, etc.)
Check what each does. Mark ✅ working or ❌ broken.

**STEP 5 — FORM CHECK**
If any form exists, check fields and submission. Mark ✅ / ❌ / N/A.

**STEP 6 — CONTENT CHECK**
Check for spelling/grammar errors and duplicate sections (visible text only).

---

### After checking all 5 URLs:

Produce the final report in this format:

---
## URL 1: [name] — [url]
| Element | Type | Status | Notes |
|---------|------|--------|-------|
| Page Load | Page | ✅/❌ | ... |
| Webinar Date | Date | ✅/❌/⚠️ | date found |
| [Button] | Button | ✅/❌ | what happened |
| [Link] | Link | ✅/❌ | where it goes |
| Form | Form | ✅/❌/N/A | result |
| Spelling | Content | ✅/❌ | issues |
| Duplicates | Content | ✅/❌ | sections |

(repeat for all 5 URLs)

---
## DATE CONSISTENCY CHECK
- PFB date: [date]
- PGA date: [date]
- CFB Thank You date: [date]
- PGA Thank You date: [date]
- All match: ✅ YES / ❌ NO

## OVERALL SUMMARY
- Total pages tested: 5
- Dates valid: X/5
- Expired dates: X
- Date mismatches: X
- Broken buttons: X
- Broken links: X
- Form issues: X
- Content issues: X
- Issues found:
  1. ...
  2. ...
---

### Final step:
1. Save the report text
2. Run: python "Webinar check daily/generate_and_upload.py"
3. Take the base64 PDF output and upload to Google Drive folder ID: 1OBzjU-FplLV5JJg1xCw514Y3u7o92glv
   - File name: Kundli-Pathshala-QA-YYYY-MM-DD.pdf
   - Use the Drive MCP connector (mcp__f8846947 create_file tool)
   - Set parentId to: 1OBzjU-FplLV5JJg1xCw514Y3u7o92glv
   - Set contentMimeType to: application/pdf
   - Set disableConversionToGoogleType to: true
