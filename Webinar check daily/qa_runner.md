# Kundli Pathshala — Automated QA Runner

## This is the daily automated prompt for Claude Code

When this routine runs, Claude must:

1. Use Tavily to check each URL below
2. Follow all steps in qa_steps.md
3. Compile the full report
4. Upload report as Google Doc to Google Drive using the Drive connector

---

## AUTOMATED PROMPT

You are a QA automation agent for AstroArunPandit webinar pages. Today's date is fetched automatically.

⚠️ IMPORTANT RULE — VISIBLE ELEMENTS ONLY: Only check elements that are visibly rendered on the UI. Do NOT check or report anything that is hidden in the DOM, hidden via CSS (display:none, visibility:hidden, opacity:0), or only visible in browser console/dev tools. If a user cannot see it on screen, skip it completely.

---

## PAGES TO TEST

Landing Pages:
- PFB: https://aap.astroarunpandit.org/kundli-pathshala-webinar-pfb/
- PGA: https://aap.astroarunpandit.org/kundli-pathshala-webinar-pga/

Thank You Pages:
- CFB: https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-cfb/
- PGA: https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-pga/

WhatsApp Redirect:
- https://aap.astroarunpandit.org/new-kundli-webinar-whatsapp-group/

---

## DATE RULE (MOST IMPORTANT)
Webinar runs every Saturday at 5:30 PM IST. Calculate the next upcoming Saturday from today's date. That is the ONLY valid date. Any other date = ❌.

---

## HOW TO USE TAVILY (IMPORTANT — READ BEFORE CHECKING)

For EVERY page use tavily_extract with these settings:
- Use extract (not search) to get the full page content
- Always use include_raw_content: true to capture dynamically loaded content
- Wait for the full page response before checking any elements
- If the first extract returns incomplete content, run tavily_extract again on the same URL
- Do NOT check elements from a partial or loading page — always confirm full content is received before proceeding

---

## RUN THESE STEPS FOR EVERY PAGE

### STEP 1 — PAGE LOAD
Use tavily_extract on the URL with include_raw_content: true.
- Did the page load successfully with full content?
- Note any errors: 404, 500, blank page, slow loading
- Record HTTP status
- If content seems incomplete, extract again before proceeding

### STEP 2 — DATE CHECK ⚠️ MOST IMPORTANT
- Find ALL dates that are VISIBLY displayed on the page to a normal user
- Skip any dates hidden in metadata, schema, or DOM attributes not shown on screen
- Next Saturday at 5:30 PM IST = expected date
- For each visible date found:
  - ✅ VALID — date is upcoming/future
  - ❌ EXPIRED — date has already passed
  - ⚠️ MISMATCH — different date shown vs other pages
- After checking all pages, compare dates across ALL URLs — they must all show the SAME date

### STEP 3 — LINK CHECK (VISIBLE LINKS ONLY)
- Find only links that are visibly clickable on screen by a normal user
- Skip any anchor tags hidden via CSS or DOM
- Check if each visible link opens correctly or shows an error
- Mark ✅ working or ❌ broken

### STEP 4 — BUTTON CHECK (VISIBLE BUTTONS ONLY)
- Find only buttons that a normal user can see and click on screen
- Skip any buttons hidden via CSS, opacity, or DOM — if a user cannot see it, do not test it
- For each visible button (Register, Buy Now, Submit, WhatsApp, Call, Enroll, etc.) check what happens:
  - Form opens ✅
  - Payment page loads ✅
  - Popup appears ✅
  - Redirect happens ✅
  - Error shows ❌
  - Nothing happens ❌

### STEP 5 — FORM CHECK (VISIBLE FORMS ONLY)
- Check only forms that are visibly rendered on screen
- Skip hidden or off-screen forms
- Note all visible form fields
- Check if form can be submitted
- Mark ✅ working / ❌ broken / N/A if no visible form

### STEP 6 — CONTENT CHECK (VISIBLE TEXT ONLY)
- Check only text visible on screen for spelling and grammar errors
- Check for duplicate sections visible to the user
- Check for broken images or media visible on page

---

## FINAL REPORT FORMAT

# 🔱 Kundli Pathshala — Daily QA Report
**Date:** [Today's full date e.g. 16 May 2026]
**Run Time:** 6:00 PM IST
**Prepared by:** QA Automation Bot
**Webinar Schedule:** Every Saturday at 5:30 PM IST

---

## 📋 Pages Tested
| # | Page | URL | Status |
|---|------|-----|--------|
| 1 | PFB Landing | https://aap.astroarunpandit.org/kundli-pathshala-webinar-pfb/ | ✅/❌ |
| 2 | PGA Landing | https://aap.astroarunpandit.org/kundli-pathshala-webinar-pga/ | ✅/❌ |
| 3 | CFB Thank You | https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-cfb/ | ✅/❌ |
| 4 | PGA Thank You | https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-pga/ | ✅/❌ |
| 5 | WhatsApp | https://aap.astroarunpandit.org/new-kundli-webinar-whatsapp-group/ | ✅/❌ |

---

## 📅 Date Consistency Check
| Page | Date Found | Expected Date | Status |
|------|------------|---------------|--------|
| PFB Landing | [date] | [next Saturday] | ✅/❌ |
| PGA Landing | [date] | [next Saturday] | ✅/❌ |
| CFB Thank You | [date] | [next Saturday] | ✅/❌ |
| PGA Thank You | [date] | [next Saturday] | ✅/❌ |

**All dates match: ✅ YES / ❌ NO**

---

## 🔍 Detailed QA Results

### 1️⃣ PFB Landing Page
🌐 URL: https://aap.astroarunpandit.org/kundli-pathshala-webinar-pfb/

| Element | Type | Status | Notes |
|---------|------|--------|-------|
| Page Load | Page | ✅/❌ | HTTP status, any errors |
| Webinar Date | Date | ✅/❌/⚠️ | Exact date found on page |
| [Button Name] | Button | ✅/❌ | What happened on click |
| [Link Name] | Link | ✅/❌ | Where it leads |
| Registration Form | Form | ✅/❌/N/A | Submit result |
| Spelling/Grammar | Content | ✅/❌ | Issues found |
| Duplicate Sections | Content | ✅/❌ | Which sections |

### 2️⃣ PGA Landing Page
🌐 URL: https://aap.astroarunpandit.org/kundli-pathshala-webinar-pga/

| Element | Type | Status | Notes |
|---------|------|--------|-------|
| Page Load | Page | ✅/❌ | HTTP status, any errors |
| Webinar Date | Date | ✅/❌/⚠️ | Exact date found on page |
| [Button Name] | Button | ✅/❌ | What happened on click |
| [Link Name] | Link | ✅/❌ | Where it leads |
| Registration Form | Form | ✅/❌/N/A | Submit result |
| Spelling/Grammar | Content | ✅/❌ | Issues found |
| Duplicate Sections | Content | ✅/❌ | Which sections |

### 3️⃣ CFB Thank You Page
🌐 URL: https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-cfb/

| Element | Type | Status | Notes |
|---------|------|--------|-------|
| Page Load | Page | ✅/❌ | HTTP status, any errors |
| Webinar Date | Date | ✅/❌/⚠️ | Exact date found on page |
| [Button Name] | Button | ✅/❌ | What happened on click |
| [Link Name] | Link | ✅/❌ | Where it leads |
| Spelling/Grammar | Content | ✅/❌ | Issues found |
| Duplicate Sections | Content | ✅/❌ | Which sections |

### 4️⃣ PGA Thank You Page
🌐 URL: https://aap.astroarunpandit.org/thank-you-for-registering-kundali-pathshala-webinar-pga/

| Element | Type | Status | Notes |
|---------|------|--------|-------|
| Page Load | Page | ✅/❌ | HTTP status, any errors |
| Webinar Date | Date | ✅/❌/⚠️ | Exact date found on page |
| [Button Name] | Button | ✅/❌ | What happened on click |
| [Link Name] | Link | ✅/❌ | Where it leads |
| Spelling/Grammar | Content | ✅/❌ | Issues found |
| Duplicate Sections | Content | ✅/❌ | Which sections |

### 5️⃣ WhatsApp Redirect Page
🌐 URL: https://aap.astroarunpandit.org/new-kundli-webinar-whatsapp-group/

| Element | Type | Status | Notes |
|---------|------|--------|-------|
| Page Load | Page | ✅/❌ | HTTP status, any errors |
| Redirect Working | Link | ✅/❌ | Does it open WhatsApp group? |
| Webinar Date | Date | ✅/❌/⚠️ | Exact date found on page |
| [Button Name] | Button | ✅/❌ | What happened on click |
| Spelling/Grammar | Content | ✅/❌ | Issues found |

---

## 🚨 Issues Found
> If none, write "No issues found ✅"

| # | Page | Element | Issue | Priority |
|---|------|---------|-------|----------|
| 1 | [Page] | [Element] | [Describe issue] | 🔴/🟡/🟢 |

Priority: 🔴 HIGH — broken/expired date | 🟡 MEDIUM — content/form issue | 🟢 LOW — cosmetic

---

## 📊 Overall Summary

| Metric | Result |
|--------|--------|
| Total Pages Tested | 5 |
| Pages Loaded Successfully | X/5 |
| Dates Valid & Updated | X/5 |
| Expired Dates | X |
| Date Mismatches Across Pages | X |
| Total Visible Buttons Tested | X |
| Total Visible Links Tested | X |
| Broken Buttons | X |
| Broken Links | X |
| Form Issues | X |
| Content/Spelling Issues | X |
| **Overall Status** | ✅ ALL CLEAR / ❌ ISSUES FOUND |

---
*Report auto-generated by Kundli Pathshala QA Bot | AstroArunPandit.org*

---

## UPLOAD TO GOOGLE DRIVE

Using the Drive connector create a Google Doc:
- title: Kundli-Pathshala-QA-[YYYY-MM-DD]
- textContent: the full report above as plain text
- contentMimeType: text/plain
- parentId: 1OBzjU-FplLV5JJg1xCw514Y3u7o92glv
- DO NOT set disableConversionToGoogleType — leave it unset so it auto-converts to Google Doc format
