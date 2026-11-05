The available files show a **historical remember-browser prototype**, but they do not establish exactly what happened to the feature.

The prototype’s `rememberSession` function stored a session token in browser local storage under `lantern_session`. It is labeled historical and calls for a security review. The file does not show a login flow or establish that the prototype was released. [rememberBrowser.ts](/tmp/ghost-local-h31qvpk9/laptop/src/auth/rememberBrowser.ts)

The current snapshot says session handling **now depends on server-issued, HTTP-only cookies**. That indicates a different session mechanism, but the note does not say when or why it changed, whether remember-browser behavior was retained, or how deployed login behaves. It points to deployment configuration outside the available archive. [operations.md](/tmp/ghost-local-h31qvpk9/current/docs/operations.md)

Both sources have limits: the laptop backup is a subset of experiments with some meeting notes missing, and the current folder is not necessarily a complete checkout. The pilot note records an internal ledger export preview, not a login release. [scope.md](/tmp/ghost-local-h31qvpk9/laptop/notes/scope.md) · [README.md](/tmp/ghost-local-h31qvpk9/current/README.md) · [pilot.md](/tmp/ghost-local-h31qvpk9/laptop/notes/pilot.md)

So the evidence supports a local-storage prototype followed by a documented cookie-based session approach; it does **not** prove that remember-browser login shipped, was removed, or still works in production.