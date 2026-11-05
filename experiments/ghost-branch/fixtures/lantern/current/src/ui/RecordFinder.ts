import { filterRecords } from '../search/queryIndex';
export function findVisibleRecords(rows: Array<{ title: string }>, query: string) { return filterRecords(rows, query); }
