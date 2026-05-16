# Kundli Pathshala — Daily QA Automation

## What this repo does

Runs automated QA checks on Kundli Pathshala webinar landing pages daily at 6:00 PM IST.
Uses Tavily to scrape pages, generates a PDF report, and uploads to Google Drive via connector.

## Schedule

**Time:** 6:00 PM IST daily  
**Drive folder:** https://drive.google.com/drive/folders/1OBzjU-FplLV5JJg1xCw514Y3u7o92glv

## How to run manually

Open Claude Code and paste the prompt from:
`Webinar check daily/qa_runner.md`

## Folder structure

```
Webinar check daily/
├── qa_runner.md          ← automated prompt (main entry point)
├── qa_steps.md           ← detailed check steps reference
├── qa_routine.md         ← overview and URL list
├── generate_and_upload.py ← PDF generator (uses reportlab)
└── requirements.txt      ← Python dependencies
```

## Tools used

- **Tavily** — scrapes and checks each URL
- **Drive MCP connector** — uploads final PDF to Google Drive
- **reportlab** — generates formatted PDF report

## URLs monitored

| Page | URL |
|------|-----|
| Landing PFB | https://aap.astroarunpandit.org/kundli-pathshala-webinar-pfb/ |
| Landing PGA | https://aap.astroarunpandit.org/kundli-pathshala-webinar-pga/ |
| Thank You CFB | https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-cfb/ |
| Thank You PGA | https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-pga/ |
| WhatsApp | https://aap.astroarunpandit.org/new-kundli-webinar-whatsapp-group/ |

## Date rule

Webinar runs every **Saturday at 5:30 PM IST**.  
All pages must show the next upcoming Saturday's date.  
Expired or mismatched dates are flagged in the report.
