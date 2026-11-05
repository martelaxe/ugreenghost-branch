Moving [assets/cover.svg](/tmp/ugreen-final-qkiy01gf/assets/cover.svg) could affect the winter program’s layout and draft. No files were changed.

- **Production:** [current/production.md](/tmp/ugreen-final-qkiy01gf/current/production.md:1) says the program references `../assets/cover.svg` as its cover and that the artwork is supplied from the shared assets folder during layout. That relative path resolves to the target. If the layout process relies on it, moving the file could leave the artwork unavailable until the reference is updated.
- **Draft:** [winter/design.md](/tmp/ugreen-final-qkiy01gf/winter/design.md:1) says `../assets/cover.svg` is included in the draft and that the final export has not yet been made. This path also resolves to the target. The note does not establish how the draft stores or loads the artwork, so the effect on export remains uncertain.

The intended destination is unspecified, so the replacement paths cannot yet be determined. The notes establish relationships to the file, but they do not show the live layout application’s behavior or any dependencies outside this workspace.

**Next safe step:** Choose the destination, then verify how the production layout and draft load the cover and determine the replacement paths before moving it.

The local read-only inventory covered the workspace root, with a limit of 50 returned paths and 20 selected documents. It found five regular files; I reviewed all four documents and checked that the target exists. The search did not reach its cap. These were local checks, not UGREEN expert calls.