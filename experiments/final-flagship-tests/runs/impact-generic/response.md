I couldn’t inspect the collection: the local command tool failed because its required sandbox component, `bwrap`, is unavailable. I therefore can’t identify which files actually reference `assets/cover.svg`.

Before moving it, you can search from the collection root:

```bash
rg -n -i --hidden -g '!.git' 'cover\.svg'
```

Check each match’s relative path: documents, HTML, CSS, manifests, or scripts that point to the old location may need updating. Also check for references constructed from separate path components, and for links inside binary documents or compressed archives, which a text search may miss. After the move, open the affected documents or pages to confirm the cover still loads.