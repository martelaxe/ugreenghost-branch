# Project Rescue — Round 1 proposal (review draft)

1. **What does your Skill do? (one sentence)**

   Project Rescue finds a context-supported candidate for a missing project file and proposes one approved copy that preserves the source.

2. **Who is your target user, and what is their problem?**

   Creators and small teams may have a missing project dependency while an existing usable copy has an opaque name, outdated alternatives, or another active use.

3. **What is your solution?**

   Compare the missing reference, review history and candidate records to identify a supported version; explain contradictions and stop when identity is ambiguous.

4. **What is the main user flow?**

   Authorize folders, investigate references and candidates, review one proposed source and destination, approve the exact operation, and independently verify the copy if the platform can safely execute it.

5. **How is your idea different from existing tools or common AI solutions?**

   The intended workflow combines cross-file identity evidence, shared-source preservation and approval-gated action across project types. Generic AI and application-specific relinking overlap; superior performance and uniqueness are not established.

6. **Which UGREEN AI NAS features does your Skill use, and at which step?**

   File-agent discovers, reads, checks paths and hashes, and conditionally copies; document-agent extracts and compares project references. All work stays within owner-authorized scopes.

7. **What is your technical approach?**

   A Markdown parent delegates to registered experts using actual completed results. The user supplies the goal and source and destination authorization. Separate owner and gateway approval are required; uncertain identity, collisions or unestablished atomic no-overwrite stop execution. Runtime model and data flows depend on UGREEN configuration.

8. **What have you built so far? What is not built yet? What still needs testing on a NAS?**

   A Markdown Skill passed static checking. Local Codex identified intended candidates in two fictional archives; generic Codex did too. A separate local adapter copied one file with simulated approvals. Real NAS execution, safe copy semantics, approval resumption and readback remain untested.

9. **How will you test your Skill if you become a Finalist? Name two core test cases and one edge case.**

   Test a creative asset and a business record with misleading names and supported identity; confirm the shared source remains. Edge case: an occupied target or unavailable atomic no-overwrite must block the copy.

10. **What are the known limits, risks, or outside dependencies of your Skill?**

   It finds existing accessible files, not deleted bytes; identity and archive coverage may remain uncertain. Byte equality does not prove application repair. UGREEN expert results, data handling, gateway approvals and collision guarantees remain unknown. Stop when safety is not established.

## Third-party and AI disclosure

Third-party and AI disclosure: No third-party executable components or open-source libraries are included in the Skill. UGREEN Uliya Skill Creation Tool and NAS runtime are supplied by UGREEN under its applicable terms (https://ai.ugreen.com/pages/hackathon-starter-kit). OpenAI Codex was used for research, drafting and local testing under OpenAI terms (https://openai.com/policies/terms-of-use/). The target runtime model and any external data flows depend on its configuration and require verification.
