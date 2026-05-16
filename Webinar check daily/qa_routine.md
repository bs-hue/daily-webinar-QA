# Kundli Pathshala — Daily QA Routine
# Runs at 6:00 PM IST every day

## TRIGGER PROMPT (paste this in Claude Code at 6 PM or set as scheduled prompt)

---

Run the Kundli Pathshala daily QA check using the following steps exactly:

### URLS TO TEST

**Landing Pages:**
- PFB: https://aap.astroarunpandit.org/kundli-pathshala-webinar-pfb/
- PGA: https://aap.astroarunpandit.org/kundli-pathshala-webinar-pga/

**Thank You Pages:**
- CFB: https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-cfb/
- PGA: https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-pga/

**WhatsApp Redirect:**
- https://aap.astroarunpandit.org/new-kundli-webinar-whatsapp-group/

### DRIVE FOLDER
Upload final PDF to folder ID: 1OBzjU-FplLV5JJg1xCw514Y3u7o92glv

### STEPS

Follow qa_steps.md to run the full check, then run generate_and_upload.py to create the PDF and upload to Drive.

---
