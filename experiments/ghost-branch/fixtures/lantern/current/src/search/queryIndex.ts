export function filterRecords(rows: Array<{ title: string }>, query: string) {
  const needle = query.toLowerCase().trim();
  return rows.filter(row => row.title.toLowerCase().includes(needle));
}
