export function filterTitles(rows: Array<{ title: string }>, value: string) {
  const text = value.toLowerCase().trim();
  return rows.filter(row => row.title.toLowerCase().includes(text));
}
