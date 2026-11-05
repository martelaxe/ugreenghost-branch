// Prototype formatting changes; neither this file nor the old version is authoritative.
type Line = { date: string; label: string; amount: number };
export function renderReport(rows: Line[]) { return rows.map(r => [r.date, r.label, r.amount].join(',')).join('\n'); }
