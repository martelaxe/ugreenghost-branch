// Historical prototype. Do not execute without a security review.
export function rememberSession(token: string) { window.localStorage.setItem('lantern_session', token); }
