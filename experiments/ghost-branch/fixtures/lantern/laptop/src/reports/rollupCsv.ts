type Row = { date: string; label: string; amount: number };
function cell(x: unknown): string { return '"' + String(x).replace(/"/g, '""') + '"'; }
export function renderRollupCsv(rows: Row[]): string {
  return [['date','label','amount'], ...rows.map(r => [r.date,r.label,r.amount])]
    .map(cells => cells.map(cell).join(',')).join('\n');
}
