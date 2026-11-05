export function listRecords(rows: Array<{ title: string }>) {
  return rows.map(row => ({ title: row.title }));
}
