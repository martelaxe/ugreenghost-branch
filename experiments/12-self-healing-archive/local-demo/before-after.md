# Local fixture result — not a UGREEN operation

The two approvals below are test inputs, not real user or platform approvals. No NAS was accessed.

- Source: `shared/review_17.txt`
- Destination: `projects/harbor/assets/launch-cover.txt`
- Simulated user approval: true; simulated gateway approval: true
- Local Python filesystem copy status: verified
- Source SHA-256 before and after: `30a7b76f7a756e0c515ac352d162d2151deb8f93c390363459b35ccbd4d6802e` / `30a7b76f7a756e0c515ac352d162d2151deb8f93c390363459b35ccbd4d6802e`
- Destination SHA-256: `30a7b76f7a756e0c515ac352d162d2151deb8f93c390363459b35ccbd4d6802e`
- Added paths: ['projects/harbor/assets/launch-cover.txt']
- Changed existing paths: []
- Removed paths: []

The expected fixture path exists with matching bytes; this does not establish that an external application opens the project or that UGREEN executes or enforces the same operation.
