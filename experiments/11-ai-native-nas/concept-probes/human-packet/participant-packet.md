# Two fictional NAS experiences

Each excerpt is an actual local AI response to a different fictional task; neither was tested on a UGREEN NAS. Read the assigned order. The source archive for each is under `archives/X/` or `archives/Y/`. The tasks and output lengths differ, so this is an exploratory concept comparison, not an experiment measuring model quality.

## Experience X

**User request:** I am considering moving `assets/shared/cover.txt` to `archive/unused/cover.txt`. Before I touch anything, help me understand what work in this archive could be affected, and give me a practical next step.

The proposed move could affect **two projects**. The archive labels `assets/shared/cover.txt:3` an “active source asset,” so filing it under `unused` would conflict with the recorded usage.

| Work | Observed evidence | Likely impact if moved without updating references |
|---|---|---|
| Autumn Walk program | `projects/autumn/program.md:1–2` references `../../assets/shared/cover.txt` and says the layout uses this source. | The recorded path would stop resolving; layout or republication work could be affected. |
| Winter guide | `projects/winter/readme.md:1` references the same file. `projects/winter/status.md:1` says design handoff is pending. | The draft’s cover reference would stop resolving, potentially affecting handoff. |

The Summer guide and 2022 brochure reference the separate `assets/shared/cover_old.txt` (`projects/summer/readme.md:1`, `projects/old/record.md:1`). Those recorded references would remain valid.

**Coverage limits:** I inspected all 12 files present in the workspace. Autumn’s exported PDF is absent according to `projects/autumn/program.md:2`; its production note mentions sponsor notes that I could not locate (`projects/autumn/production.md:1`). External partner files are explicitly unchecked (`admin/vendor-note.txt:1`), and the inventory is incomplete for applications and external copies (`admin/inventory.txt:1`). Actual application behavior and external dependencies remain unknown.

**Practical next step:** keep the asset in place for now. Treat any later move as a coordinated migration: update both project references to `../../archive/unused/cover.txt` and verify the Autumn layout and Winter handoff against the relocated asset before calling it unused.

No files were changed.

## Experience Y

**User request:** I have an unfinished project in this archive. Help me turn the material into a small useful thing I can actually make within the documented constraints.

Make a **one-page River Walk observation handout**, with four sections that could become a folded guide if A4 paper and printing are available. The text below is ready to copy.

**Observed evidence:** The goal is to help visitors notice changing water levels during a short walk (`project/purpose.txt:1`). Rowan has one free afternoon and a $15 limit (`planning/time.txt:1`). Rowan permits their written field notes in a free educational handout; that permission does not cover outside photos or other contributors (`rights/use.txt:1`).

**Recommendation—inference:** A text-only handout is a manageable first version. The planned three viewing points lack documented locations (`project/steps.txt:1`), so this version supplies observation prompts without inventing a route.

---

### River Walk: Notice the Water

*A short observation guide*

Water levels can look different from one visit to the next. Use a visible fixed feature to help describe what you notice.

### From Rowan’s field notes

“Low water exposed the third step; one week later the water reached the first step.”

These are observations, not scientific measurements.

### Look, describe, compare

From a safe, permitted place, choose a fixed feature you can see without approaching the water.

- What feature are you looking at?
- Where does the water meet it today?
- What would you look for on another visit?

Stay out of the water and off exposed steps. This handout does not identify an approved walking route.

### Your observation

Date and time: ____________________

Place or visible feature: ____________________

Today I noticed: ____________________

On another visit I could compare: ____________________

*Based on Rowan’s written field notes. Free educational handout.*

---

To make it in one afternoon:

1. Copy the four sections onto one page. If materials are available, try a four-panel A4 fold, as suggested in `materials/fold.txt:1`.
2. Check that the text is readable and the observation blanks are usable.
3. Confirm current paper, printer access, and total cost before printing; keep spending within $15. Prior availability and the 2022 receipt establish no current stock (`materials/fold.txt:1`; `personal/receipt.txt:1`).
4. Leave photographs and public display out of this first version. IMG-42’s file and public-use permission are absent (`materials/image-index.txt:1`); library permission and a date remain unconfirmed (`planning/venue.txt:1`).

**Coverage and unknowns:** I read all 12 files returned by the workspace file listing, including hidden and ignored files. No files were changed or external sources accessed. The archive does not establish current printing access, actual viewing-point locations, route safety or access permission, or an approved venue. The handout is ready as text; physical production depends on confirming supplies within budget.

## Questions

1. Which experience would you actually want to use on your NAS? X / Y / neither. Why?
2. Which result would change what you would do next? X / Y / both / neither. How?
3. Which felt surprising or memorable? X / Y / both / neither. Why?
4. What was generic, confusing, incorrect, unsafe or missing?
5. What would you need to verify before acting on the result?
6. Would either make you more excited about an AI NAS? Yes / maybe / no. Explain.

Choose neither if appropriate; please do not include personal data.
