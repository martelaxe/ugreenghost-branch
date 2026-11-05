# Author smoke check — 26 October 2026

This is a review by the person who designed the fixture and knew its intended answer. It is **not a blind discovery test** and is not evidence of performance on UGREEN NAS hardware.

## Finding to verify

A $540 deposit may not have been applied to a supplier invoice:

- `../fictional-files/01-inbox/supplier-message.txt` says a $540 deposit for R-284 will be applied to the final invoice.
- `../fictional-files/02-finance/bank-export.csv` shows a $540 payment to the supplier referencing R-284.
- `../fictional-files/02-finance/invoice-august.txt` shows the same reservation, a $1,800 charge and $0 credits applied.

If the bank payment is the deposit and no separate adjustment exists, the suggested remaining balance would be $1,260. The files do not prove whether an adjustment was made elsewhere, whether the invoice was paid, or whether a refund is owed. Check the payment and ask the supplier or finance team to confirm before taking any action.

## Verification performed

A local structural check counted 12 fictional input files, confirmed that the three primary clues and the different-reference distractor exist, and printed file hashes. No files were moved or modified. This check did not assess whether an independent AI would find the connection.
