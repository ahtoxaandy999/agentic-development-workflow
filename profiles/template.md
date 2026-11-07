# Profile template

Copy this into your project's agent entry file (or a file it links to) and
fill every value. The core and the skills use these placeholders; a value
left empty means the rule that needs it cannot be followed.

```markdown
## Workflow profile

ADW source: <tag> @ <full commit SHA>   (what you copied from)
Kind: code | non-code

| Placeholder | Value |
| --- | --- |
| `<plan file>` | path of the single planning file (Now / Next / Later / Owner questions) |
| `<decision dir>` | folder with one file per decision |
| `<workflow file>` | the loop with this project's commands, or "this section" |
| `<change id>` | what identifies a candidate: full commit SHA, or a document version |
| `<check fast>` | command or procedure run while working |
| `<check full>` | command or procedure run once on the final id |
| `<review channel>` | where verdicts go: pull request comment, or a review file path |
| `<owner language>` | language for questions to the owner |
| `<question tool>` | how agents ask the owner multiple-choice questions |
| `<status dir>` | status files, only when several sessions run at once; else "none" |
| `<flaky list>` | known-flaky checks with owner and due date (code); else "none" |

Who accepts: <agents merge on PASS + green checks | the owner accepts every change>
Risky paths (strongest reviewer, owner acceptance): <paths or "none">
Owner-class additions: <items added to the list in core/decisions.md, or "none">
Minor additions: <items, or "none">
External actions that need the owner's yes: <list>
Skills used: <names from skills/>
```

## Updating

Copy again from a newer tag, compare with your adapted files, and change the
`ADW source` line. ADW never writes into your repository.
