# Example Queries and Expected Responses

This document provides sample emails showing how the AI model should respond in each scenario.

---

## Scenario 1: Exact / Close Match to Answered Question

### Inbound Customer Email:
> "Hello Rownd Team,
> I am excited about the new 5X CNC machine. When will pre-orders open on Kickstarter, and how much will it cost?
> Best regards, Alex"

### Expected AI Output:
**Matched FAQs:** FAQ ID 1 (Pre-order date) and FAQ ID 2 (Estimated price)

**Draft Response for Customer:**
> Hi Alex,
>
> Thank you for your interest in the Rownd 5X!
>
> Pre-orders for the Rownd 5X are currently planned to begin in September. Official details, including final pricing, will be announced together with the launch of the pre-order campaign.
>
> Please stay tuned for our upcoming launch announcements!
>
> Best regards,
> Rownd Team

---

## Scenario 2: Unanswered Question (Requires Employee Escalation)

### Inbound Customer Email:
> "Hi there,
> Can the Rownd 5X machine titanium alloy Ti-6Al-4V efficiently, and does it come with a 2-year enterprise warranty policy?
> Thanks, Marcus"

### Expected AI Output:
**Status:** No verified answer available.

**Notification:**
> **Action Required:** No close answer found in our verified FAQs for the specific cutting performance on Ti-6Al-4V or the enterprise warranty policy.
>
> **Please forward this email to our employees.**

---

## Scenario 3: Mixed Email (One Answered, One Unanswered)

### Inbound Customer Email:
> "Hello,
> Does the Rownd 5X include tool setting out of the box? Also, do you offer educational discounts for universities in Germany?
> Regards, Professor Schmidt"

### Expected AI Output:
**Matched FAQs:** FAQ ID 35 (Tool setting)

**Draft Response for Customer:**
> Dear Professor Schmidt,
>
> Thank you for reaching out to us.
>
> An automatic tool measurement probe will be included as a standard feature on every Rownd 5X machine.
>
> Regarding your question about educational discounts for universities in Germany: I have forwarded this inquiry to our sales and academic partnerships team, and a representative will follow up with you directly.
>
> Best regards,
> Rownd Team

**Employee Escalation Notice:**
> **Action Required:** The question regarding educational discounts is not covered in our verified FAQs. Please forward this part of the email to our sales/support employees for follow-up.
