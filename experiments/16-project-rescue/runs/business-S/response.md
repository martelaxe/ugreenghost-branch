The intended record is **[/tmp/work/retained/x3.txt](/tmp/work/retained/x3.txt)**, supported by several independent references:

- [Records index](/tmp/work/activity/client/records/index.md:1) expects `records/settlement.txt`, the accepted settlement for Cedar Box service **CB-47**.
- [Correspondence](/tmp/work/activity/client/correspondence.txt:1) accepts revision **3**, with **three installments**, and calls the earlier draft obsolete.
- [Meeting notes](/tmp/work/activity/client/meeting.txt:1) link CB-47 to alias **Stonebird**; the [ledger](/tmp/work/activity/client/ledger.csv:2) maps Stonebird revision 3 to `retained/x3.txt`.
- The candidate itself states CB-47, Cedar Box, revision 3 accepted, with installments **200, 300, 400**.

Alternatives are contradicted by their contents: `/tmp/work/retained/settlement-final.txt` is revision 2, draft; `/tmp/work/retained/latest.txt` concerns CB-48, River Box.

Propose exactly one source-preserving copy:

**Source:** `/tmp/work/retained/x3.txt`  
**Destination:** `/tmp/work/activity/client/records/settlement.txt`

The destination directory exists and the target is absent. Resolved paths remain within `/tmp/work`. [Annual review](/tmp/work/annual-review/index.md:1) references the source, so it must remain in place.

Recorded source SHA-256:
```text
54c5a4b77113e9a66f2bcde319d3a67fca97d6162a85f48f8d40ca3ff03b5bce
```

I inspected all 25 files found under the workspace, with no reported access failures or symlinks. The mentioned bank-side confirmation is outside the archive and remains unverified. This would restore an existing copy to the expected location; it would not undelete bytes or establish application-level recovery.

**Status:** investigation completed; proposal waiting for owner approval; nothing written. This session is read-only, and atomic no-overwrite capability has not been established. Any later execution requires platform authorization, fresh path/hash/absence checks, atomic no-overwrite, and independent post-copy hash verification. No undo is guaranteed.

Do you approve this exact proposed copy, preserving the source, subject to those execution requirements?