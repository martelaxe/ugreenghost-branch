import { renderRollupCsv } from '../src/reports/rollupCsv';
// Historical sample only; not executed in this investigation.
const result = renderRollupCsv([{ date: '2024-10-03', label: 'Stall, north', amount: 12 }]);
if (!result.includes('"Stall, north"')) throw new Error('comma quoting');
