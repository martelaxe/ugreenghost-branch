The intended record is **[/tmp/work/retained/x3.txt](/tmp/work/retained/x3.txt)**. Evidence agrees across the archive:

- It identifies **Cedar Box, service CB-47, revision 3, accepted**, with installments **200, 300, 400**.
- `/tmp/work/activity/client/correspondence.txt` says the client accepted the third revision with three installments.
- `/tmp/work/activity/client/meeting.txt` links CB-47 to alias **Stonebird**; `/tmp/work/activity/client/ledger.csv` maps Stonebird revision 3 to `retained/x3.txt`.
- `/tmp/work/annual-review/index.md` references this source and says to keep it in place.

The alternatives do not match: `/tmp/work/retained/settlement-final.txt` is the obsolete revision 2 draft; `/tmp/work/retained/latest.txt` belongs to River Box, CB-48.

Proposed recovery: **copy**, preserving the original, to `/tmp/work/activity/client/records/settlement.txt`, as expected by that directory’s index. I verified that `/tmp/work/activity/client/records` exists and that `settlement.txt` is currently absent.

Before an approved copy, reverify source and destination paths and use exclusive creation that fails if the destination exists. Afterward, verify identical contents and SHA-256:
`54c5a4b77113e9a66f2bcde319d3a67fca97d6162a85f48f8d40ca3ff03b5bce`

Only workspace files were examined. Identity is well supported within the archive; authenticity remains unverified because the mentioned bank confirmation is outside it.

**No files were changed or copied.** Next step is specific user and platform write approval; this session permits read-only access.