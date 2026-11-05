## The Workshop’s Missing Answer

*A short fictional archive mystery.*

Your goal is to reconstruct the two-part answer for a workshop exhibit. All necessary clues are below. No outside knowledge is needed.

**The evidence**

- **Exhibit ticket:** “Neighborhood workshop, 17 April 2019.”
- **Visitor label:** “April 2019: the final two-part answer is the lantern-sign color followed by the number of sheets left.”
- **Workshop diary:** “In 2019 our lantern sign was BLUE. In 2022 we repainted the sign YELLOW.”
- **Stock card:** “For April 2019: we had 18 blue paper sheets before the activity.”
- **Activity sheet:** “April 2019: the class used 6 blue paper sheets; none of the others were used.”
- **Loose paper:** “A different workshop in 2022 began with 30 sheets. It is unrelated to the April 2019 activity.”

**Your move:** Identify the relevant sign color, then calculate the remaining blue sheets. Submit one line in the format `COLOR NUMBER`.

---

## SPOILER — Solution and exact sources

**Answer: `BLUE 12`**

1. The ticket dates the exhibit to April **2019**, so use the diary’s **BLUE** sign, before the 2022 repaint.
2. The matching stock and activity records give **18 − 6 = 12** blue sheets remaining.

Source paths relative to the workspace:

- Ticket: `02-box/ticket.txt`
- Answer rule: `02-box/label.txt`
- Sign history: `01-school/diary.txt`
- Starting stock: `01-school/stock.txt`
- Sheets used: `03-notes/usage.txt`
- Unrelated 2022 stock: `04-decoys/extra-paper.txt`

**Limits:** I inspected all 18 workspace files. The relevant records contain no direct contradiction; the different colors and stock figures concern different years or workshops. Other paper quantities are unspecified, so the numerical answer uses the documented blue sheets. No files were modified.