# Investigation Report

## Scope

Reviewed all 12 files in the workspace without modifying them. The archive supports **one significant actionable finding**.

## 1. A paid $540 deposit appears to be missing from the equipment invoice

**Confidence: High that the records require reconciliation; moderate that the invoice overstates the remaining balance.**

### Supporting evidence

| Source filename | Evidence |
|---|---|
| `01-inbox/supplier-message.txt` | Harbor Light Rentals reserved equipment for **18–19 July**, reference **R-284**. Its 9 May message states: “The reservation deposit is $540; it will be applied to the final equipment invoice.” |
| `02-finance/bank-export.csv` | A **10 May 2026** transaction records `HARBOR LIGHT RENTALS R-284,-540.00`, supporting payment of that deposit. |
| `02-finance/invoice-august.txt` | Invoice **H-991**, issued **3 August 2026**, charges **$1,800** for **18–19 July**, references **R-284**, and shows **“Credits applied: $0”** and **“Amount due: $1,800.”** |
| `04-notes/handwritten-summary.txt` | On **5 August**, Maya noted that the lighting invoice seemed higher than remembered and that she could not find the earlier paperwork. |

### Reasoning and significance

The supplier, reservation reference, and rental dates connect the deposit promise and bank debit directly to invoice H-991. If $1,800 is the full rental charge and the promised deposit credit remains applicable, the remaining balance should be **$1,260**.

Paying the invoice as written would bring total payments to **$2,340**, potentially **$540 above the stated rental charge**. The reservation message also supplies the earlier paperwork Maya was trying to locate.

### Uncertainties and alternative interpretations

The archive does not establish whether the deposit was later refunded, credited elsewhere, or addressed in a revised invoice. It also does not show whether H-991 has been paid. Those possibilities could resolve the discrepancy, but none is documented here.

### Recommended next actions

1. Reconcile reservation **R-284** against the supplier’s account ledger, including any refund or separate credit.
2. Provide the supplier with the reservation message, bank transaction, and invoice; request a corrected **$1,260** balance if no other adjustment exists.
3. If H-991 was already paid in full, request a **$540 refund or documented credit**, subject to reconciliation.

## Other observations

`05-admin/venue-confirmation.txt` confirms the East Room for **18 July**, while `03-projects/shoot-log.txt` dates the shoot **19 July**. This is worth clarifying when reconstructing the project, but it does **not** establish a booking error: the shoot may have used another location, or the archive may omit an updated confirmation.

The older invoice in `06-archive/older-invoice.txt` concerns a different reservation, **R-109**, and does not establish that July’s rental rate was excessive.

## Optional file organization improvements

- Group the reservation message, payment evidence, final invoice, and reconciliation under **R-284**.
- Maintain a supplier register with columns for deposit paid, credit applied, remaining balance, and payment status.
- Store venue confirmations and shoot logs together, recording date changes explicitly.