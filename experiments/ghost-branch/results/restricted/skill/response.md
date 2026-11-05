## Ghost Recovery Packet: remember-browser login

**Classification: UNCERTAIN.** The laptop backup contains a historical prototype that stores a session token in browser local storage. The current snapshot says session handling now uses server-issued, HTTP-only cookies, but it does not establish whether those cookies provide a “remember this browser” option or what happened to the prototype.

**What the evidence shows**

- [rememberBrowser.ts](/tmp/ghost-local-tsfutrd6/laptop/src/auth/rememberBrowser.ts:1) labels itself a historical prototype and calls for a security review. Its only shown function saves a supplied token to `window.localStorage`. That establishes a storage mechanism, but it does not show a complete login flow, expiry, logout behavior, or a working feature.
- [operations.md](/tmp/ghost-local-tsfutrd6/current/docs/operations.md:1) says session handling now depends on server-issued, HTTP-only cookies and points to deployment configuration outside the archive. This is evidence of a different session-handling approach, but the note does not explicitly say the prototype was retired or explain why.
- [scope.md](/tmp/ghost-local-tsfutrd6/laptop/notes/scope.md:1) says the laptop backup contains only a subset of experiments and that some meeting notes were never included. [current/README.md](/tmp/ghost-local-tsfutrd6/current/README.md:1) likewise describes `current/` as a snapshot, not necessarily a complete checkout.

The supplied [screenshot](/tmp/ghost-local-tsfutrd6/laptop/screenshots/pilot-ledger.png) shows a ledger and an export button; it provides no evidence about login behavior.

**What remains uncertain:** There is no decision record in the inspected material linking this prototype to an intentional rejection or replacement. Its implementation, release history, relationship to the current cookie-based sessions, and whether an equivalent exists in deployed infrastructure are unknown. The local-storage design warrants security review, but the available evidence does not establish that a security issue caused its removal.

**Suggested next investigation:** Have a developer compare the prototype with the actual current authentication and deployment configuration, and look for the missing decision or design records. If integration is later considered, review session persistence, expiry, logout, and security behavior, then test those flows. No tests were run.

The investigation was limited to the authorized `current/` and `laptop/` folders. It was read-only; no code was executed, changed, restored, or merged, and no Git or network service was used.