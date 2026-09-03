---
id: ADW-BOOTSTRAP-RESEARCH-001
artifact_status: active
authority: evidence
research_status_at_publication: completed
recommendation_status_at_publication: proposed
evidence_as_of: 2026-09-02
owner: agentic-development-research
question: smallest-responsible-bootstrap-structure
scope: repository-bootstrap-and-context-architecture
repository: ahtoxaandy999/agentic-development-workflow
repository_state: "main; private; unborn/empty repository; no commit SHA (GitHub Contents 404, Commits 409), verified 2026-09-02"
supersedes: null
---

# Дослідження початкової структури Agentic Development Workflow

Цей звіт є доказовою запискою та рекомендацією. Він не є Workflow v1, не активує інструменти й не надає агентам нових повноважень. Рекомендації стають обов'язковими лише після окремого рішення про adoption та оновлення відповідного нормативного артефакту.

## A. Executive verdict

### GO WITH CHANGES

Окремий репозиторій **ahtoxaandy999/agentic-development-workflow** виправданий як версіонований міжпроєктний control plane для правил координації, доказів, рішень і навігації. Він має залишатися репозиторієм управління workflow, а не другим task tracker або складом копій продуктових репозиторіїв.

Запропоновані сім файлів надмірні на bootstrap-етапі. П'ять керівних файлів мають окремих власників відповідальності, але два tooling-документи не мають ще ні прийнятого tool-selection process, ні перевірених permission contracts, ні реальних користувачів. Водночас початковий commit повинен містити сам цей research note, якщо його джерела пройдуть незалежний source review. Рекомендований baseline тому складається із шести файлів: п'ять керівних артефактів плюс незмішаний з policy доказовий звіт.

Домінантні ризики:

1. змішування provider authorization, connector capability та ChatGPT approval policy для GitHub;
2. перетворення research findings або project memory на неявну policy;
3. дублювання статусу між Markdown, GitHub Issues/Projects та чатами;
4. великий AGENTS.md, який витісняє task context і швидко старіє;
5. передчасне кодування Apps, MCP, AFK і parallel-execution механіки до появи перевірених bottlenecks та owner;
6. плутанина між candidate commit, passing checks, PR і фактичним acceptance.

**Рівень упевненості:** високий щодо стану репозиторію, потреби в центральному control plane, six-file bootstrap і офіційно задокументованої семантики `project-only memory`; середній щодо ефективної конфігурації конкретного account/workspace/surface та майбутнього tooling registry через configuration-dependent поведінку й неповні pre-install permission details.

**Припущення:** чинні accepted premises залишаються прийнятими; репозиторій лишається private; початково є один accountable maintainer/coordinator; DR-001 передує Workflow v1; DR-005 окремо досліджує tooling; цей звіт буде незалежно перевірено перед adoption.

## B. Verified current facts

Позначення: **V** = перевірений факт із первинного джерела; **U** = перевірене спостереження поточного UI або connector; **R** = rollout/account/workspace/surface-dependent; **I** = висновок. Позначка **нестабільно** означає, що факт треба перевіряти повторно перед gate.

### B.1 Repository facts

| Факт | Статус | Доказ і свіжість |
|---|---|---|
| Репозиторій доступний під поточною GitHub identity | V | Connected GitHub repository inspection, 2026-09-02; [repository](https://github.com/ahtoxaandy999/agentic-development-workflow) |
| Visibility | V | private, 2026-09-02 |
| Default branch | V | main, 2026-09-02 |
| GitHub repository ID | V | 1354694953, 2026-09-02 |
| Вміст | V | root Contents повернув 404 “This repository is empty”; size = 0 |
| Commit history | V | commit search повернув 409 “Git Repository is empty” |
| Поточний SHA | V | відсутній. main є unborn default branch, тому bootstrap не може посилатися на неіснуючий SHA |
| Branch-protection platform capability | V, нестабільно | GitHub дозволяє створити protection rule для branch, якого ще не існує. [GitHub: Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule) |
| Effective pre-creation protection path for this private repo | R/U, не перевірено | Availability і workable settings залежать від plan/tier, ownership, actor/bypass options та intended branch-creation path; потрібен capability/configuration check перед materialization |
| Записи під час дослідження | V | не виконувалися |

Це точний стан на 2026-09-02. Його не можна переносити в майбутнє без повторної перевірки.

### B.2 ChatGPT platform facts

Офіційну документацію OpenAI Help Center перевірено 2026-09-02. Це current capability evidence, а не UI inference. Ефективна доступність і поведінка все одно залежать від plan, account memory, workspace settings та surface і потребують canary перед operational use.

| Факт | Статус | Наслідок |
|---|---|---|
| ChatGPT Project об'єднує chats, files, instructions і supported app links; Project Instructions діють тільки в цьому Project і перекривають global custom instructions | V, нестабільно | Project корисний як working context, але не замінює repo truth. [OpenAI Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) |
| Projects підтримують `Default memory` і `Project-only memory`; режим вибирають при створенні та можуть змінити пізніше у Project settings | V, нестабільно | Capability не є unresolved; canary перевіряє лише ефективну конфігурацію account/workspace/surface. Зміна може застосовуватися кілька годин. [OpenAI Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) |
| У `Project-only memory` previously saved memories не використовуються; chats можуть посилатися на інші chats у тому самому Project, але не на chats поза ним; зовнішні chats також не можуть посилатися всередину | V, нестабільно | Command Center отримує задокументований context firewall без втрати cross-chat continuity всередині Project. [OpenAI Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) |
| `ChatGPT Work` недоступний у Project із `Project-only memory` | V, нестабільно | Command Center не повинен планувати Work; Research Lab із `Default memory` залишається Work surface, якщо Work доступний account/workspace. [OpenAI Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) |
| `Default memory` завжди дозволяє same-Project chat references, але external-chat behavior відрізняється за plan: Enterprise/Edu ізольовані, non-Enterprise including Business можуть мати cross-project/non-project references | V, R, нестабільно | “Standard memory” у planning terminology слід записувати як official `Default memory`; Research Lab має прийняти contamination risk і minimum inputs. [OpenAI Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) |
| Project memory вимагає enabled memory settings; workspace feature controls можуть вимкнути memory, Deep Research або інші tools всередині Projects | V, R, нестабільно | Відсутня опція у конкретному UI може бути account/workspace configuration, а не відсутність capability. [OpenAI Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) |
| Apps підтримуються у Projects на перелічених поточних plans, але конкретна App capability залежить від plan, region, workspace, role, model і interface | V, R, нестабільно | Per-App і per-surface canary обов'язковий; Project support не доводить Work/Deep Research support кожної App. [OpenAI Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt), [Apps in ChatGPT](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt) |
| Задокументована модель Project sources вимагає upload, supported app link або connector retrieval; звідси операційний висновок: ChatGPT Project сам по собі не встановлює current repository state | I на основі V, нестабільно | Uploaded або Project-stored copy є snapshot, а не доказом current state. Repository state можна встановити лише через live connector/git/API і exact-SHA verification. [OpenAI Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) |
| Required team guidance слід зберігати у AGENTS.md або checked-in docs; memory є recall layer | V, нестабільно | Project memory не має нормативної влади. [OpenAI Memories](https://learn.chatgpt.com/docs/customization/memories) |

### B.3 GitHub connector facts: три окремі permission layers

| Layer | Перевірений факт на 2026-09-02 | Чого факт не доводить | Bootstrap rule |
|---|---|---|---|
| **A. Provider authorization** | Connected GitHub identity читає private target repo. Repository metadata повернуло `admin`, `maintain`, `pull`, `push`, `triage: true`. Target repo access доведено; повний GitHub App installation repository set не був окремо перелічений | Ці provider/repository permissions не є переліком connector tools і не доводять, що ChatGPT виконає write без approval або взагалі виконає його у цьому surface | Обмежити installation до selected repository, якщо setting доступний; не підключати production identities; перед зміною scope перевірити provider screen |
| **B. Connector capability** | Поточний tool surface рекламує read і write operations для files, branches, issues, PR та reviews; read operations фактично прочитали metadata/empty-state. Write canary не проводився | Advertised tool не доводить успішну provider authorization, workspace allowance, approval outcome або safety allowance конкретного write | Bootstrap використовує тільки read-only canary. Жодних connector writes; кожен майбутній write потребує окремого explicit execution gate |
| **C. ChatGPT approval policy** | Live permission inspection показав GitHub app-specific `Use my default`; global default `Allow low-risk actions`. OpenAI окремо документує `Always ask`, `Allow read actions`, `Allow low-risk actions`, `Allow all actions`; доступні options залежать від account, app, connection і workspace | Approval mode не надає provider access, не розширює connector capability і не гарантує, що action буде дозволено; sensitive action може бути blocked | Для control-plane repo обрати `Always ask` або `Allow read actions`/equivalent ask-before-write, де доступно; незалежно від UI mode policy цього bootstrap забороняє writes без окремого gate |

OpenAI прямо відокремлює app permission від підключення account, provider permissions, workspace policy й available app actions. Тому official read-oriented overview, exposed write-capable tools і live approval setting не є суперечністю: це різні layers/surfaces. Фактична успішність GitHub write тут **не доведена і не спростована**, бо authorized write canary був поза scope. [Managing app permissions in ChatGPT](https://help.openai.com/en/articles/20001495-managing-app-permissions-in-chatgpt), [Apps in ChatGPT](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)

### B.4 Work and Deep Research facts

| Факт | Статус | Наслідок |
|---|---|---|
| Work призначений для substantial task з clear outcome та reviewable output і може використовувати files, plugins та approved tools | V, R, нестабільно | Research Lab є природним місцем для довгих evidence deliverables. [OpenAI Work](https://learn.chatgpt.com/docs/get-started-with-work) |
| Cloud option у Work показується лише коли доступний | V, R, нестабільно | Не закладати cloud/AFK availability у baseline |
| Для independent parallel tasks OpenAI радить separate chats і не давати двом задачам write access до одного connected source | V, нестабільно | Майбутні execution waves потребують isolation та resource locks. [OpenAI Long-running work](https://learn.chatgpt.com/docs/long-running-work) |
| Deep research models синтезують багато джерел і в API вимагають хоча б одне data source | V, нестабільно | Deep Research доречний для широких, нестабільних, суперечливих питань, але не для простого git inspection. [OpenAI Deep Research](https://developers.openai.com/api/docs/guides/deep-research) |
| Deep Research у ChatGPT включає clarification, prompt rewriting і research; API сам цього не додає | V, нестабільно | Research question та plan мають бути явними незалежно від surface. [OpenAI Deep Research](https://developers.openai.com/api/docs/guides/deep-research) |
| Deep Research API підтримує web search, file search, read-oriented search/fetch remote MCP і code interpreter; довільні MCP tools не підтримуються | V, нестабільно | “Apps available in Deep Research” не можна виводити з Work/plugin availability. [OpenAI Deep Research](https://developers.openai.com/api/docs/guides/deep-research) |

У перевіреному офіційному corpus немає достатньої surface-specific гарантії про всі Apps усередині поточного ChatGPT Deep Research UI. Це missing evidence, а не негативний факт.

### B.5 Apps and plugin facts

Live catalog 2026-09-02 показав GitHub як installed; Atlassian Rovo, Google Drive, SharePoint, Notion, Figma, Slack, Gmail, Google Calendar, Outlook та Teams як available, але не installed. Catalog descriptions підтверджують загальне призначення, не точні OAuth scopes чи повний read/write tool contract.

OpenAI підтверджує, що plugin може містити skills, connectors, MCP і hooks; зовнішні connections використовують authentication та access controls відповідного сервісу; permissions треба окремо переглянути та схвалити. Hooks потрібно вважати кодом довіри. [OpenAI Plugins](https://learn.chatgpt.com/docs/plugins)

Тому для всіх неінстальованих Apps точні read capabilities, write capabilities, approval behavior і workspace scoping позначені “не перевірено до install-time permission screen/canary”. Популярність або присутність у каталозі не є доказом придатності.

### B.6 MCP facts

| Tool | Перевірений current fact | Counterevidence або межа |
|---|---|---|
| MCP protocol | Current security guidance описує confused deputy, token passthrough, SSRF, local server compromise, scope і consent risks | “Protocol-compatible” не означає trusted. [MCP Security Best Practices, 2026-07-28](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices) |
| Serena | Semantic symbol retrieval/navigation і refactoring через language tooling; заявлена підтримка Codex | Має edit/refactor/shell та memory surface; marketplace commands можуть бути застарілими; self-evaluation не є незалежним доказом. [Serena](https://github.com/oraios/serena) |
| Context7 | Доставляє version-specific library docs через CLI/skill або MCP | README попереджає, що community-contributed docs не мають гарантії accuracy/security. [Context7](https://github.com/upstash/context7) |
| Playwright MCP | Browser control через accessibility tree, persistent або isolated profiles | Власна документація радить CLI+skills як token-efficient coding default у частині сценаріїв; profiles містять login state; origin/workspace restrictions не є security boundary. [Playwright MCP](https://github.com/microsoft/playwright-mcp) |
| GitHub MCP | Built-in GitHub MCP для Copilot coding agent може бути scoped read-only до current repo; configured MCP може діяти автономно | Wider PAT має бути fine-grained, repository-specific і read-only; окремий MCP зараз дублює connected GitHub та git/gh. [GitHub MCP guidance](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers) |
| Sentry MCP | Search/triage errors і performance data; OAuth та project-scoped endpoint available | Немає реального Sentry bottleneck у порожньому control-plane repo. [Sentry MCP](https://mcp.sentry.dev/) |

### B.7 External workflow facts

#### Matt Pocock

Current primary source перевірено на commit **6654f6b60cd9d5be8b54c6fafe44346dabeb3b76**, 2026-08-24. Repo описує skills як small/composable, а не єдиний mandatory framework. Поточний ланцюг є **grill-with-docs → to-spec → to-tickets → implement → code-review**. [Pinned README](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/README.md)

Потрібні для bootstrap висновки:

- domain-modeling створює CONTEXT.md і ADR ліниво, лише коли з'явився реальний термін або hard-to-reverse decision; CONTEXT.md є glossary, а не implementation guide. [domain-modeling](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills/engineering/domain-modeling/SKILL.md)
- to-spec не повинен фіксувати volatile code paths; to-tickets віддає перевагу demoable tracer-bullet vertical slices, що вміщуються у fresh context, і явним blocking dependencies. [to-spec](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills/engineering/to-spec/SKILL.md), [to-tickets](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills/engineering/to-tickets/SKILL.md)
- phase-boundaries розрізняє clear, compact, handoff та subagent/AFK; handoff має посилатися на durable artifacts, не дублювати їх, і не містити secrets. [phase-boundaries](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills/engineering/ask-matt/PHASE-BOUNDARIES.md), [handoff](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/skills/productivity/handoff/SKILL.md)
- current docs фіксують documented shortcomings: orchestrated file writes можуть губитися, chat decisions не мають ledger, CONTEXT може стати lore, same-context review має confirmation bias, recursive review може не збігатися, parallel sessions у shared checkout дають branch/stash failures. [grill-with-docs current notes](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/docs/engineering/grill-with-docs.md), [implement current notes](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/docs/engineering/implement.md), [code-review current notes](https://github.com/mattpocock/skills/blob/6654f6b60cd9d5be8b54c6fafe44346dabeb3b76/docs/engineering/code-review.md), [grill-with-docs issue #284](https://github.com/mattpocock/skills/issues/284)
- current primary repo не дав bootstrap-worthy універсального status-line/token threshold. Він описує smart/dumb-zone management, але числовий поріг є harness-specific і має бути досліджений окремо.

Ці practices є evidence та requirements input, не шаблоном для копіювання. Removed або superseded skills, зокрема ubiquitous-language, не слід реанімувати як bootstrap artifacts.

#### OpenAI agentic engineering

OpenAI harness case study називає repository knowledge system of record, показує провал monolithic AGENTS.md і використовує короткий AGENTS.md як table of contents для progressive disclosure. Автори також прямо застерігають, що автономність залежить від конкретної структури та tooling і не узагальнюється без подібних інвестицій. [Harness engineering, 2026-02-11](https://openai.com/index/harness-engineering/)

Окремий long-horizon experiment показує agent loop plan/edit/test/observe/repair/update-docs та externalized state у repo, files, docs, worktrees і outputs. Але його Prompt.md/Plan.md stack є одним 25-hour experiment, а не універсальним bootstrap standard. [Run long horizon tasks with Codex, 2026-02-23](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex)

Symphony робить issue tracker state machine та control plane для isolated runs, dependency DAG і bounded concurrency, але OpenAI називає reference implementation low-key engineering preview для trusted environments. Не кожна ambiguous або judgment-heavy задача підходить цьому стилю. [Symphony repository](https://github.com/openai/symphony), [OpenAI Symphony report, 2026-04-27](https://openai.com/index/open-source-codex-orchestration-symphony/)

Git worktrees ізолюють parallel chats, а Codex Cloud підкреслює isolated environments, reproducibility і review before merge. [OpenAI Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees), [Codex Cloud](https://learn.chatgpt.com/docs/cloud)

#### Counterevidence щодо context files

Контрольоване дослідження на coding tasks знайшло, що context files у середньому збільшили inference cost більш ніж на 20%, developer-written instructions дали лише малий середній приріст, generated context погіршив результат, а overview не покращував discovery суттєво. Обмеження: Python-heavy benchmark і task-resolution outcome, не security чи governance. Це не аргумент відмовитися від AGENTS.md, але сильний аргумент залишити там лише мінімальні вимоги й маршрути. [Gloaguen et al., “Evaluating AGENTS.md”, 2026-02-12](https://arxiv.org/html/2602.11988v1)

## C. Design principles derived from evidence

| Source-derived finding | Inference for this repository | Recommendation |
|---|---|---|
| Repository-local versioned docs є доступним agent system of record; memory є recall layer | Cross-project rules і adoption state мають мати commit identity | Центральний repo є authoritative control plane; chats тільки посилаються на full SHA |
| Monolithic AGENTS.md витісняє task/code context і старіє | Root AGENTS.md не повинен дублювати README, charter чи Workflow v1 | Зробити AGENTS.md короткою agent-facing map + hard boundaries |
| Context files можуть знижувати success і збільшувати cost | “More docs” не є безкоштовним safety improvement | Створювати документ лише коли є distinct owner, bootstrap need та update trigger |
| GitHub README є primary human landing surface | README має пояснювати purpose і start-here, але не policy mechanics | Один human-facing index у root |
| ADR і glossary мають цінність після реального irreversible decision/term | Порожні architecture/ADR/CONTEXT dirs породжують planned-state theater | Створювати їх ліниво після grill/adoption |
| Deep Research може синтезувати багато джерел, але output сам не є рішенням | Publication-time evidence state і поточна adoption disposition мають різних owners | Research note фіксує snapshot; після materialization research register одноосібно зберігає current mutable disposition; explicit adoption gate |
| Separate chats/worktrees потрібні для independent parallel work | DAG сам не запобігає shared-resource conflicts | Пізніше task contract має мати dependencies, ownership, locks і isolation; зараз лише reserve the concept |
| Symphony масштабує issue-driven execution, але потребує mature harness і trusted environment | Автоматичний dispatcher у порожньому repo є передчасним | Не створювати schema/automation; дослідити після manual workflow evidence |
| Provider authorization, connector actions і ChatGPT approval modes є окремими шарами | Назва App або repository permission metadata не визначає effective action authority | Selected-repo provider scope, read-only canary, conservative approval, explicit fallback, no production account by default |
| Candidate diff/commit можна незалежно переглянути | Test pass або PR state не дорівнює acceptance | Пізніше фіксувати exact commit SHA, fresh review і human/coordinator acceptance окремо |
| GitHub rule може називати branch, якого ще не існує, але settings можуть обмежити його creation path | “Unborn” не означає автоматичну потребу в unprotected first commit і не гарантує безпечну preconfiguration | Перед materialization перевірити capability/configuration; обрати preconfigured rule або explicit one-time exception з immediate protection після candidate |
| Handoffs є secondary navigation artifacts | Copying full chat переносить шум, secrets і stale claims | Handoff тільки з pointers, state delta, blockers та next gate |

## D. Candidate-structure evaluation

### D.1 Summary decision table

| Path | Proposed owner | Bootstrap need | Authority | Main risks | Decision |
|---|---|---:|---|---|---|
| AGENTS.md | repository maintainer | так | agent-facing navigation | prompt bloat, duplicated policy | keep with changes |
| README.md | repository maintainer | так | human-facing navigation | becoming policy/tracker | keep with changes |
| PROJECT-CHARTER.md | accountable coordinator/maintainer | так | normative | hidden Workflow v1, overlap with README | keep with changes |
| docs/policies/research-evidence.md | research-governance owner | так | normative | process bloat, findings mixed into policy | keep with changes |
| docs/research/research-register.md | research coordinator | так | research-index | duplicate tracker, stale statuses | keep with changes |
| docs/tooling/chatgpt-app-matrix.md | відсутній до DR-005 | ні | tooling inventory | guessed permissions, stale catalog | defer |
| docs/tooling/mcp-stack.md | відсутній до DR-005 | ні | tooling inventory | premature selection, trust burden | defer |

Окремо додається `docs/research/ADW-BOOTSTRAP-RESEARCH-001.md` як evidence artifact. Поточний pre-review deliverable має `artifact_status: draft`; source-reviewed version, яку execution включить у bootstrap candidate, має `artifact_status: active`. Вона не конкурує з register: note зберігає publication-time evidence та reasoning. Після materialization register одноосібно зберігає current mutable research/adoption state; до того review record і bootstrap adoption record існують лише як authorization inputs, а не як нібито вже оновлений repository artifact.

### D.2 AGENTS.md

| Field | Contract |
|---|---|
| 1. Responsibility | Коротка agent-facing карта authoritative artifacts, maturity та hard operating boundaries |
| 2. Bootstrap need | Потрібен, бо Codex автоматично знаходить root AGENTS.md, а репозиторій створюється саме для agent-coordinated work |
| 3. Authority class | agent-facing navigation; сам не є власником повної policy |
| 4. May contain | read order; pointers, зокрема на register для current work; current maturity; prohibition on treating research as policy; no-write/no-secret/acceptance boundaries; request to reverify repo state |
| 5. Must not contain | Workflow v1; command catalog; duplicated charter; full repo overview; speculative tool stack; task state; chat history |
| 6. Initial status | у першому bootstrap candidate commit: `artifact_status: active`, `maturity: bootstrap`, `authority: navigation`; baseline acceptance не змінює file metadata |
| 7. Update trigger | authority path, maturity state, mandatory safety boundary або discovery behavior змінено |
| 8. Supersession/deletion | update in place; nested AGENTS.md лише коли реальна subtree-specific rule з owner; root не видаляється поки agents працюють з repo |
| 9. Future relationship | вказує на adopted workflow/policies/task contracts; не копіює їх |
| 10. Duplication risks | README purpose, charter premises, research policy lifecycle |
| 11. Max initial size | hard maximum **3 KiB**; line count може бути лише non-normative drafting guidance |
| 12. Heading outline | Repository role; Authority/read order; Current maturity; Agent boundaries; Verification and acceptance; Escalation |
| 13. Front matter | ні, він витрачає injected context і не потрібен discovery |
| 14. Competing owner | charter володіє mission/authority; policy володіє research lifecycle; README володіє human entrypoint |
| 15. Recommendation | **keep with changes** |

Офіційний Codex читає AGENTS.md root-to-current directory, ближчий файл має більший пріоритет, а combined default limit становить 32 KiB. Це підтримує один маленький root file зараз і nested files лише за фактичної потреби. [OpenAI AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)

### D.3 README.md

| Field | Contract |
|---|---|
| 1. Responsibility | Human-facing landing page і navigation |
| 2. Bootstrap need | Перший читач повинен зрозуміти purpose, maturity, source-of-truth та start-here без знання чатів |
| 3. Authority class | human-facing navigation |
| 4. May contain | what/why; current maturity; concise scope/non-scope; authority map; stable pointer “See Research Register for current research state and the next gate”; links |
| 5. Must not contain | policy details; active task ledger; tool registry; architecture; decision history; historical chat |
| 6. Initial status | у першому bootstrap candidate commit: `artifact_status: active`, `maturity: bootstrap`, `authority: navigation`; baseline acceptance не змінює file metadata |
| 7. Update trigger | repository purpose, entrypoint, scope label, maturity, navigation або authority map змінилися; не кожний research transition |
| 8. Supersession/deletion | update in place; history лишається у Git |
| 9. Future relationship | веде до charter, adopted workflow, research register, architecture index коли вони з'являться |
| 10. Duplication risks | повтор charter і register status |
| 11. Max initial size | рекомендовано 3-5 KiB; це size target, не hard acceptance guard |
| 12. Heading outline | Purpose; Current maturity; Start here; Authority map; Scope; Current work (stable register pointer); Repository state |
| 13. Front matter | ні, GitHub rendering та human scan не потребують |
| 14. Competing owner | charter володіє normative scope; register володіє research state |
| 15. Recommendation | **keep with changes** |

GitHub вважає README entry surface і рекомендує пояснювати what, why, how to get started, help та maintenance, залишаючи там лише потрібну стартову інформацію. [GitHub README guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)

### D.4 PROJECT-CHARTER.md

| Field | Contract |
|---|---|
| 1. Responsibility | Єдиний root owner mission, scope, non-scope, roles, authority hierarchy та bootstrap safety floor |
| 2. Bootstrap need | Без нього central repo може стати другим tracker, automation repo або policy dump |
| 3. Authority class | normative; adoption і maturity відображаються окремо |
| 4. May contain | mission; repo boundaries; accepted premises; coordinator/executor roles; authority precedence; acceptance principle; minimal security posture; amendment rule |
| 5. Must not contain | Workflow v1 phases; task schema; tool selection; implementation commands; project-specific domain decisions |
| 6. Initial status | bootstrap adoption decision відбувається до execution, тому перший candidate commit уже містить `artifact_status: active`, `adoption_status: accepted`, `maturity: bootstrap`, `authority: normative`; commit acceptance є окремим SHA-level state |
| 7. Update trigger | mission/scope/authority/security floor змінено explicit decision |
| 8. Supersession/deletion | supersede in place або новим charter version із explicit replaces link; не видаляти без successor |
| 9. Future relationship | обмежує Workflow v1, policies, tool registry та per-project adapters |
| 10. Duplication risks | README scope summary, AGENTS boundaries, future Workflow |
| 11. Max initial size | рекомендовано 6-8 KiB; line count лише non-normative guidance |
| 12. Heading outline | Status; Mission; Scope; Non-scope; Roles; Authority hierarchy; Acceptance semantics; Security floor; Amendment |
| 13. Front matter | так, status/authority/owner/approved_at або supersedes мають machine-readable value |
| 14. Competing owner | немає; README тільки резюмує і посилається |
| 15. Recommendation | **keep with changes**, root-level |

Root placement виправданий cross-cutting authority, високою discoverability та стабільним посиланням. Переміщення під docs не додає ownership, лише ще один hop.

### D.5 docs/policies/research-evidence.md

| Field | Contract |
|---|---|
| 1. Responsibility | Мінімальний normative contract для evidence production, source review, adoption separation, freshness і supersession |
| 2. Bootstrap need | DR-001 не можна запускати без правила, яке забороняє silent promotion research → policy |
| 3. Authority class | normative; adoption і maturity відображаються окремо |
| 4. May contain | when research; source hierarchy; required metadata; lifecycle; contradiction/freshness handling; source-review gate; adoption gate; sensitive-data rule; supersession |
| 5. Must not contain | конкретні findings; research queue; App/MCP choices; citations registry; Workflow v1 |
| 6. Initial status | перший candidate commit уже містить `artifact_status: active`, `adoption_status: accepted`, `maturity: bootstrap`, `authority: normative`, бо policy adopted до execution; baseline acceptance не переписує metadata |
| 7. Update trigger | evidence quality incident, new research surface, adopted lifecycle change |
| 8. Supersession/deletion | update in place з recorded supersedes; deletion лише якщо інший adopted policy повністю поглинув responsibility |
| 9. Future relationship | керує всіма research notes, включно DR-001/DR-005; adoption оновлює інші normative artifacts |
| 10. Duplication risks | report methodology, register status taxonomy |
| 11. Max initial size | рекомендовано 6-8 KiB; line count лише non-normative guidance |
| 12. Heading outline | Scope; Use/no-use criteria; Source policy; Metadata; Lifecycle; Source review; Adoption; Sensitive data; Freshness/supersession |
| 13. Front matter | так, status/authority/owner/version/effective_from |
| 14. Competing owner | register володіє queue/state, report володіє findings |
| 15. Recommendation | **keep with changes** |

### D.6 docs/research/research-register.md

| Field | Contract |
|---|---|
| 1. Responsibility | Після створення: канонічний компактний index і **єдиний owner current mutable** research/adoption state, dependencies, artifact pointers та next gate |
| 2. Bootstrap need | Authorized execution має вперше materialize reviewed research status, current bootstrap decision status, adoption scope/reference і next gate до DR-001; DR-001 та DR-005 далі мають бути видимими до появи external tracker decision |
| 3. Authority class | research-index |
| 4. May contain | ID; short question; owner; `research_status`; `current_decision_status`; `adoption_scope`; `adoption_ref`; `superseded_by`; evidence date; artifact link; dependency; `next_gate` |
| 5. Must not contain | повний report; normative findings; implementation checklist; GitHub Issue duplicate state |
| 6. Initial status | authorized execution створює файл уперше у bootstrap working tree як `artifact_status: active`, `maturity: bootstrap`, `authority: research-index`; commit review/acceptance state не кодується у front matter |
| 7. Update trigger | research status, evidence artifact, adoption/defer/reject/supersession змінився |
| 8. Supersession/deletion | після adoption одного external tracker перетворити на pointer/index або видалити через migration decision; заборонити dual-write |
| 9. Future relationship | може посилатися на Issues/Project item, але один state owner на record |
| 10. Duplication risks | GitHub Issues/Projects, README next task, Project memory |
| 11. Max initial size | рекомендовано 2-4 KiB; line count лише non-normative guidance |
| 12. Heading outline | Authority; Status taxonomy; Active/planned research; Completed notes; Adoption queue; Superseded |
| 13. Front matter | виправданий мінімальний status/authority/as_of; row metadata важливіше |
| 14. Competing owner | поки немає; GitHub Issues є майбутньою альтернативою після explicit migration |
| 15. Recommendation | **keep with changes** |

### D.7 docs/tooling/chatgpt-app-matrix.md

| Field | Contract |
|---|---|
| 1. Responsibility | Якщо створений пізніше: inventory verified ChatGPT App capabilities, permissions, scope, surfaces, fallback |
| 2. Bootstrap need | відсутній: exact scopes ще не перевірені, жоден bottleneck крім GitHub read не доведено |
| 3. Authority class | tooling inventory, не policy |
| 4. May contain | verified install/version/date; problem; read/write; approval; surface; scope; owner; failure/fallback |
| 5. Must not contain | secrets; OAuth tokens; guessed capability; normative requirement без adoption link |
| 6. Initial status | не створювати; lifecycle/adoption metadata не застосовується до відсутнього artifact |
| 7. Update trigger | DR-005 source review та конкретний App canary |
| 8. Supersession/deletion | merge в tool-registry; split лише якщо App lifecycle отримує окремого owner |
| 9. Future relationship | input до tooling policy/config, але не її заміна |
| 10. Duplication risks | MCP stack, plugin catalog, admin UI, security policy |
| 11. Max initial size | якщо з'явиться: 6-10 KiB; тільки verified rows |
| 12. Heading outline | Scope; Verification legend; Registry; Permission canaries; Failures; Rejected/deferred |
| 13. Front matter | так, evidence_as_of/status/owner |
| 14. Competing owner | майбутній unified tool-registry |
| 15. Recommendation | **defer**, пізніше ймовірно merge |

### D.8 docs/tooling/mcp-stack.md

| Field | Contract |
|---|---|
| 1. Responsibility | Якщо створений пізніше: inventory selected/evaluated MCP servers, versions, authority, trust, fallback |
| 2. Bootstrap need | відсутній: empty control repo не має code-navigation, browser, Sentry чи orchestration bottleneck |
| 3. Authority class | tooling inventory, не runtime config |
| 4. May contain | bottleneck; consumer role; read/write/network/filesystem; auth; pin; maintenance owner; threat notes; fallback; decision link |
| 5. Must not contain | credentials; unpinned accepted config; marketing claims як evidence; ChatGPT App rows без layer marker |
| 6. Initial status | не створювати; lifecycle/adoption metadata не застосовується до відсутнього artifact |
| 7. Update trigger | DR-005 evaluation + real-project canary + owner |
| 8. Supersession/deletion | merge в tool-registry; split лише за різного owner/update cadence |
| 9. Future relationship | входить до agent harness/config після окремої adoption |
| 10. Duplication risks | App matrix, Codex config, security policy, project README |
| 11. Max initial size | якщо з'явиться: 8-12 KiB |
| 12. Heading outline | Scope; Trust model; Registry; Pinning; Canaries; Fallbacks; Rejected/deferred |
| 13. Front matter | так, evidence_as_of/status/owner |
| 14. Competing owner | майбутній unified tool-registry |
| 15. Recommendation | **defer**, пізніше ймовірно merge |

## E. Recommended bootstrap tree

Exact recommended first-commit tree після source review та adoption gate:

    agentic-development-workflow/
    ├── AGENTS.md
    ├── README.md
    ├── PROJECT-CHARTER.md
    └── docs/
        ├── policies/
        │   └── research-evidence.md
        └── research/
            ├── ADW-BOOTSTRAP-RESEARCH-001.md
            └── research-register.md

Відхилення від seven-file hypothesis:

1. **docs/tooling/chatgpt-app-matrix.md вилучено з bootstrap.** Немає verified permission contract або App owner; файл одразу застарів би.
2. **docs/tooling/mcp-stack.md вилучено з bootstrap.** Немає реального bottleneck або selected MCP; навіть “порожній список” створив би хибне враження policy.
3. **docs/research/ADW-BOOTSTRAP-RESEARCH-001.md додано.** Це distinct evidence owner для bootstrap design. Якщо register посилатиметься лише на chat або external file, rationale не буде частиною accepted durable control plane.

Не створювати порожні directories: architecture, adr, context, specs, tasks, plans, templates, schemas, tooling, automation, mcp, skills, hooks, worktrees. Не додавати LICENSE, CONTRIBUTING.md, CODEOWNERS, SECURITY.md або .gitignore, доки не з'явиться окрема потреба та owner. Private governance repository без code/generated outputs не потребує їх у першому commit.

### Коли з'являються deferred artifacts

| Gate | Artifact, який може з'явитися | Умова |
|---|---|---|
| Після DR-001 adoption | workflow lifecycle/acceptance artifact | лише якщо прийнято distinct owner і не дублюється charter |
| Після DR-005 adoption | docs/tooling/tool-registry.md | verified capabilities, trust, pinning, fallback і owner |
| Після першого real grill-with-docs | CONTEXT.md або domain glossary | лише для реально неоднозначних термінів; не implementation guide |
| Після першого hard-to-reverse decision | ADR | реальна tradeoff decision, status і supersession |
| Після появи product/code topology | architecture document | descriptive current architecture з freshness owner |
| Після manual task-contract evidence | issue template або schema | поля довели користь; один tracker є owner |
| Після AFK readiness evidence | automation/config | explicit budgets, stop conditions, isolated environment, recovery |

## F. File content contracts

### F.1 AGENTS.md

**Purpose:** автоматично завантажувана карта для bounded executors і reviewers.

**Allowed content:** repository role; authority read order; current maturity; pointers to charter/policy/register; hard prohibitions; requirement reverify live state; exact acceptance caveat.

**Prohibited:** повний workflow; task status; tool list; branch commands; numeric token threshold; copied findings; broad autonomy.

**Bootstrap candidate status:** `artifact_status: active`, `maturity: bootstrap`, `authority: navigation`. Front matter is not required because the file is injected into agent context; a concise prose maturity label is sufficient. Candidate review and baseline acceptance do not change this file-level state.

**Outline:**

1. Repository role
2. Authority and read order
3. Current maturity
4. Agent boundaries
5. Verification and acceptance
6. Escalation

**Expected initial length:** hard maximum **3 KiB**. Any line-count target is non-normative drafting guidance, not a second acceptance requirement.

**Update trigger:** зміна authoritative path, maturity або hard boundary.

**Supersession:** update root file in place; nested file only for an owned subtree rule.

Критична bootstrap instruction: “Research reports are evidence. They do not modify normative policy unless an explicit adoption decision names the target artifact and adoption scope. Repository use additionally requires an accepted baseline SHA.”

### F.2 README.md

**Purpose:** human landing page.

**Allowed content:** concise purpose, maturity, start-here sequence, scope summary, authority map and a stable pointer: “See [Research Register](docs/research/research-register.md) for current research state and the next gate.”

**Prohibited:** policy text, live execution dashboard, complete research table, tool claims, aspirational directory tree.

**Bootstrap candidate status:** `artifact_status: active`, `maturity: bootstrap`, `authority: navigation`. No front matter is required; the rendered maturity statement must say that Workflow v1 is not adopted. Candidate review and baseline acceptance do not change this file-level state.

**Outline:**

1. Agentic Development Workflow
2. Current maturity
3. Purpose
4. Start here
5. Authority map
6. Scope and non-scope
7. Current work (stable pointer to Research Register)

**Expected initial length:** recommended 3-5 KiB; not a hard correctness guard.

**Update trigger:** repository purpose, entrypoint, maturity label, navigation або authority structure змінено. A research status or next-gate transition updates only the register, not README.

**Supersession:** update in place; Git history owns history.

### F.3 PROJECT-CHARTER.md

**Purpose:** normative owner mission, scope, roles, authority precedence і bootstrap safety floor.

**Allowed content:** accepted premises у стислому вигляді; repository boundaries; coordinator/executor roles; authority hierarchy; no-acceptance-by-test rule; exact full-SHA candidate principle; minimal security posture; amendment.

**Prohibited:** Workflow v1; detailed phase/gate mechanics; tool selection; task template; project-specific implementation.

**Bootstrap candidate metadata:**

    ---
    artifact: project-charter
    artifact_status: active
    adoption_status: accepted
    maturity: bootstrap
    authority: normative
    owner: repository-maintainer
    ---

Bootstrap adoption decision передує execution, тому normative content уже adopted до створення candidate SHA. `artifact_status` показує, що файл є current repository owner у цій revision; `adoption_status` показує adoption нормативного рішення; `maturity` показує ранню зрілість. Fresh review і coordinator acceptance переводять SHA між commit-level states, не змінюючи front matter. Механіка зміни normative content має вимагати explicit replacement/adoption.

**Outline:**

1. Status and authority
2. Mission
3. Scope
4. Non-scope
5. Roles
6. Authority hierarchy
7. Acceptance semantics
8. Security floor
9. Amendment and supersession

**Expected initial length:** recommended 6-8 KiB; not a hard correctness guard.

**Update trigger:** explicit decision про mission, scope, roles, hierarchy або security floor.

**Supersession:** successor names prior version; history remains in Git.

### F.4 docs/policies/research-evidence.md

**Purpose:** мінімальна policy, яка відокремлює evidence production від adoption.

**Allowed content:** use/no-use criteria; source hierarchy; metadata; lifecycle; contradictions; freshness; sensitive handling; source-review/adoption gates; supersession.

**Prohibited:** конкретні conclusions; tooling recommendations; research queue; citations to every note; workflow implementation.

**Bootstrap candidate metadata:**

    ---
    artifact: research-evidence-policy
    artifact_status: active
    adoption_status: accepted
    maturity: bootstrap
    authority: normative
    owner: research-governance
    ---

Ця metadata materializes the prior adoption decision. Candidate review і baseline acceptance не змінюють її в тому самому SHA.

**Outline:**

1. Scope
2. When research is required
3. When ordinary inspection is sufficient
4. Source hierarchy and freshness
5. Required metadata
6. Lifecycle
7. Contradictions and missing evidence
8. Source-review gate
9. Adoption gate
10. Sensitive material
11. Supersession

**Expected initial length:** recommended 6-8 KiB; not a hard correctness guard.

**Update trigger:** evidence-quality incident, new research surface або lifecycle decision.

**Supersession:** explicit policy replacement; research notes remain unchanged evidence snapshots.

### F.5 docs/research/research-register.md

**Purpose:** після першого materialization, current compact index and sole owner of mutable research/adoption state.

**Allowed content:** ID, question, owner, `research_status`, `current_decision_status`, `adoption_scope`, `adoption_ref`, `superseded_by`, evidence date, link, dependencies and `next_gate`.

**Prohibited:** report body, policy, implementation task checklist, duplicated GitHub issue comments.

**Bootstrap candidate metadata:**

    ---
    artifact: research-register
    artifact_status: active
    maturity: bootstrap
    authority: research-index
    as_of: 2026-09-02
    ---

`adoption_status` не застосовується до navigation/index artifact. `artifact_status: active` означає current repository owner у candidate revision, а не accepted baseline.

Файл не існує під час source review або bootstrap adoption. На цих двох pre-materialization gates reviewer і coordinator створюють explicit authorization inputs. Authorized execution уперше створює register та ініціалізує його перевіреним research status, current bootstrap decision status, `adoption_scope`, `adoption_ref` і `next_gate` з цих inputs.

**Immediate status taxonomy:**

| Axis | Allowed initial values | Meaning |
|---|---|---|
| artifact_status | draft, active, superseded, archived | чи є файл current repository owner у відповідній revision; не commit-review state |
| adoption_status | proposed, accepted, rejected | disposition лише нормативного рішення; не commit-review state |
| maturity | bootstrap, v1, stable | development maturity, незалежна від adoption |
| authority | normative, navigation, research-index, evidence | authority class; evidence не є policy |
| research_status | planned, in-progress, completed, reviewed, superseded | evidence-production state |
| current_decision_status | proposed, accepted, rejected, deferred, superseded | current disposition recommendations; поле належить тільки register |

Не змішувати completed research з adopted decision. “Reviewed” означає source/quality review, не policy acceptance.

**Outline:**

1. Authority and update rule
2. Status taxonomy
3. Active and planned
4. Completed notes
5. Adoption queue
6. Superseded

**Expected initial length:** recommended 2-4 KiB; not a hard correctness guard.

**Update trigger:** зміна одного зі state axes, artifact link, dependency або gate.

**Supersession:** після прийняття GitHub Issues/Projects як єдиного state owner перетворити Markdown на read-only pointer або видалити через migration commit. Dual-write заборонено.

### F.6 docs/research/ADW-BOOTSTRAP-RESEARCH-001.md

**Purpose:** durable publication-time evidence snapshot і reasoning для bootstrap decision.

**Allowed content:** metadata з цього звіту, current facts, citations, alternatives, recommendation, unresolved decisions.

**Prohibited:** секрети, copied historical chat, active policy claims, post-evidence silent edits.

**Current pre-review deliverable metadata:**

    ---
    id: ADW-BOOTSTRAP-RESEARCH-001
    artifact_status: draft
    authority: evidence
    research_status_at_publication: completed
    recommendation_status_at_publication: proposed
    evidence_as_of: 2026-09-02
    owner: agentic-development-research
    question: smallest-responsible-bootstrap-structure
    scope: repository-bootstrap-and-context-architecture
    repository: ahtoxaandy999/agentic-development-workflow
    repository_state: "main; private; unborn/empty repository; no commit SHA (GitHub Contents 404, Commits 409), verified 2026-09-02"
    supersedes: null
    ---

Source-reviewed version, яку execution включає у bootstrap candidate, використовує ту саму publication metadata, але `artifact_status: active`:

    ---
    id: ADW-BOOTSTRAP-RESEARCH-001
    artifact_status: active
    authority: evidence
    research_status_at_publication: completed
    recommendation_status_at_publication: proposed
    evidence_as_of: 2026-09-02
    owner: agentic-development-research
    question: smallest-responsible-bootstrap-structure
    scope: repository-bootstrap-and-context-architecture
    repository: ahtoxaandy999/agentic-development-workflow
    repository_state: "main; private; unborn/empty repository; no commit SHA (GitHub Contents 404, Commits 409), verified 2026-09-02"
    supersedes: null
    ---

`recommendation_status_at_publication` не змінюється через later adoption. Після materialization поточний review/adoption disposition, `adoption_scope` і `adoption_ref` змінюються лише у `research-register.md`; до materialization їх несуть explicit review/adoption authorization inputs. Material new evidence створює successor/revision з новим `evidence_as_of` та explicit relation. Після створення candidate SHA його metadata не переписується: correction створює новий SHA і потребує review.

**Outline:** секції A-O цього report.

**Expected initial length:** достатній для cited evidence; орієнтир до 100 KiB не є hard correctness guard. Note не входить у default AGENTS/read path, тому його не треба штучно стискати в AGENTS budget.

**Update trigger:** ніколи для silent refresh. Material new evidence створює нову revision/note з новим evidence_as_of та supersedes.

**Supersession:** старий note лишається versioned; successor явно вказує supersedes.

## G. Authority and artifact-lifecycle model

### G.1 Authority order

Для конкретного claim застосовується один owner:

1. current connected repository state, exact commit/diff та protected GitHub state;
2. accepted repository charter, policies, architecture та ADR у відповідних scopes;
3. accepted task issue/contract для task scope;
4. source-reviewed research note як evidence, але не policy; після bootstrap materialization current disposition читається тільки з register;
5. Project Instructions як thin runtime adapter до exact baseline SHA;
6. project memory, handoff і chat summaries як navigation aids.

Нижчий рівень не переписує вищий. Якщо artifact contradicts current code/repo state, він позначається stale і gate блокується до вирішення.

### G.2 Research promotion path

    research question
        → research plan
        → source collection
        → evidence report
        → independent source review
        → source-reviewed research note
        → explicit adoption decision
        → normative artifact update

Source-reviewed research note означає, що evidence quality перевірено. Це не означає, що recommendation прийнято. Note зберігає publication-time snapshot. До repository materialization review record і adoption record є authorization inputs; authorized execution уперше переносить їх current disposition у створюваний register, який відтоді є єдиним mutable owner.

### G.3 Separate state planes

Три state planes не замінюють один одного:

| Plane | Owner | States | Boundary |
|---|---|---|---|
| Decision adoption | до materialization: explicit coordinator adoption record як authorization input; після materialization: normative artifact плюс current disposition у research register | `proposed` → `accepted` або `rejected` | `adoption_status` застосовується лише до normative decisions; bootstrap adoption відбувається до register creation, а execution потім ініціалізує register з adoption record |
| Artifact lifecycle | сам file contract у конкретній repository revision | `draft` → `active` → `superseded` → `archived` | показує, чи файл є current owner у цій revision; не показує review/acceptance commit |
| Commit/baseline acceptance | durable acceptance record tied to exact full SHA | candidate SHA → reviewed SHA → accepted baseline SHA → superseded baseline SHA | state належить SHA, не front matter кожного файла |

У першому bootstrap candidate всі шість файлів уже `active`, а два normative files також `adoption_status: accepted`, бо adoption завершено до execution. Це не робить candidate SHA accepted baseline. Full SHA не змінюється: будь-яка content або metadata correction створює новий SHA, який проходить fresh review.

### G.4 Execution and acceptance path

    adopted charter/policy
        → accepted task issue/contract
        → isolated execution
        → candidate commit SHA
        → independent review findings
        → PR/integration checks
        → live acceptance evidence
        → explicit final acceptance
        → durable status update

PR є proposal, у якому GitHub збирає conversation, commits, checks, diff і reviews, але сам PR не означає acceptance. [GitHub Pull Requests](https://docs.github.com/en/pull-requests/reference/pull-requests)

Для bootstrap baseline точна послідовність така:

    source-reviewed evidence
        → explicit source-review authorization input
        → explicit bootstrap adoption decision
        → explicit adoption authorization input
        → branch-protection capability/configuration check
        → six active files materialized, including initialized register
        → candidate SHA
        → protection verified or enabled
        → reviewed SHA
        → coordinator acceptance record
        → accepted baseline SHA
        → later accepted replacement
        → superseded baseline SHA

### G.5 Authoritative owner by state

| Artifact/state | Authoritative owner | Role and boundary |
|---|---|---|
| ChatGPT Project Instructions | applied Project configuration; future versioned template only after canary, pinned to SHA | runtime routing only; no unique policy |
| Project memory | ChatGPT platform | non-authoritative recall; never sole owner |
| Work | current Work chat + produced artifact | execution surface, not source of truth |
| Deep Research | research plan/report | evidence producer, not adopter |
| Repository research note | committed active note in the candidate/baseline revision | durable publication-time evidence snapshot; не current adoption owner і не commit-acceptance owner |
| Pre-materialization review/adoption state | explicit source-review record і explicit coordinator adoption record | authorization inputs only; register ще не існує і не може бути оновлений |
| Research state/disposition after materialization | docs/research/research-register.md | first durable repository materialization, далі sole owner of mutable `research_status`, `current_decision_status`, `adoption_scope`, `adoption_ref`, `superseded_by`, `next_gate` |
| Charter | PROJECT-CHARTER.md at accepted SHA | mission, scope, roles, authority |
| Architecture document | future current architecture owner | descriptive current structure; created only when system exists |
| ADR | future per-decision record | adopted hard-to-reverse decision and rationale |
| Task issue | one selected tracker | task scope, state, dependencies, acceptance criteria |
| Candidate commit | Git commit object identified by exact full SHA | content-addressed review target; content change creates another SHA |
| Commit/baseline state | durable SHA-linked review/acceptance record | candidate, reviewed, accepted baseline, superseded baseline; never encoded by changing every file |
| PR | GitHub | integration proposal, review discussion і checks |
| Acceptance | explicit human/coordinator record linked to exact SHA/outcome | only owner of accepted baseline; ordinary tag alone is insufficient |
| Handoff | temporary summary with pointers | navigation/state delta; never unique rule or decision |

GitHub Issues підтримують tasks, sub-issues, dependencies та Projects metadata. Це робить їх сильним future task owner, але не доводить потребу мігрувати research register до того, як issue taxonomy прийнята. [GitHub Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues)

## H. Command Center and Research Lab topology

### H.1 Recommended topology

| Dimension | Agentic Development Command Center | Agentic Development Research Lab |
|---|---|---|
| Primary purpose | clarification, decisions, classification, planning, findings, live/final acceptance | external research, comparisons, evidence production |
| Memory | official `Project-only memory`; canary verifies effective account/workspace/surface configuration | official `Default memory` (the planned “standard memory”) |
| Allowed inputs | exact accepted baseline SHA; current adopted repo docs; reviewed notes; task/review/acceptance artifacts | bounded research question; research policy; minimal repo facts/SHA; public/approved internal sources |
| Prohibited inputs | historical long chat dump; raw source corpus; unreviewed research as policy; production secrets | normative writes; production credentials; unnecessary full private repos; Command Center decision chatter |
| Work | **not available** while Project uses `Project-only memory`; not required for Command Center | preferred для substantial multi-source report, subject to plan/workspace/surface availability |
| Deep Research | consume reviewed outputs, не основне місце production | primary home where available |
| Apps | GitHub read canary only initially | web research; GitHub read only when question requires; other Apps deferred |
| Write authority | no connector writes until a separate gate | no repository or business-system writes |
| Output promotion | explicit decision/adoption and normative update | report → source review → source-reviewed note; не policy |

### H.2 Context firewall

1. Research Lab отримує minimum necessary context, не весь Command Center transcript.
2. Кожен published output має durable publication-time metadata; після bootstrap materialization current `research_status` і `current_decision_status` зберігає тільки register.
3. У Command Center переходить source-reviewed report або concise evidence digest з посиланням на full note; рекомендація не стає policy без adoption.
4. Raw research source dump не стає Project Source за замовчуванням.
5. Жодна memory recollection не переважає exact repository SHA.
6. Старий long chat не копіюється. Потрібні premises вже мають бути переформульовані в charter або source-reviewed research note.

### H.3 Baseline SHA and epoch policy

Після першого commit обидва Projects мають містити:

- repository: ahtoxaandy999/agentic-development-workflow;
- baseline_ref: повний 40-character commit SHA;
- verified_at;
- правило повторно перевіряти default branch head перед state-dependent work;
- statement, що Project sources/memory не замінюють baseline_ref.

Новий Project epoch потрібен при material charter/instruction baseline change, підтвердженому context contamination або material platform change. Звичайна поява нового commit не вимагає нового Project: достатньо explicit baseline advance після review. Старий epoch архівується, але не переносить full transcript. `Project-only memory` можна змінити після створення, але application може тривати кілька годин; до завершення canary Project не використовується для acceptance-sensitive work. [OpenAI Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)

### H.4 Uploaded snapshots

Якщо live connector недоступний, snapshot називається:

    repo__branch__shortSHA-or-unborn__YYYYMMDDTHHMMSSZ.ext

Manifest поруч або в report має містити source repository, branch, full SHA або unborn, generated_at, exclusions, sensitivity та generator. Snapshot завжди “non-authoritative snapshot”. Не змішувати snapshots різних SHA. Його слід retire/delete з Project Sources, коли live connector успішно читає той самий або новіший SHA. Stale snapshot не може підтримувати acceptance.

## I. Apps, plugins and MCP bootstrap policy

### I.1 Bootstrap action matrix

| Tool | Layer | Concrete problem | Access | Risk | Bootstrap action |
|---|---|---|---|---|---|
| GitHub | ChatGPT app/connector | live repository facts, later Issues/PR review | provider access to target verified; current connector advertises read+write tools; approval inherits `Allow low-risk actions`; only reads canaried | accidental writes, wrong repo, stale auth, conflated layers | **verify now**, selected-repo read-only canary; no writes; conservative approval before any later execution |
| Slack | ChatGPT plugin | retrieve discussion evidence or later notify humans | pre-install exact read/write scopes not verified | sensitive conversations, message send, second source of truth | **defer** |
| Figma | ChatGPT plugin | design-to-code evidence and design-system mapping | pre-install exact scope not verified | private designs, write/change authority, stale frames | **defer** |
| Atlassian Rovo, Jira/Confluence | ChatGPT plugin | task/knowledge retrieval if those systems become owners | pre-install exact tools/scopes not verified | duplicate tracker, broad workspace search/write | **defer** |
| Notion | ChatGPT plugin | research/knowledge retrieval | pre-install exact tools/scopes not verified | competing policy store, broad page access | **defer** |
| Google Drive | ChatGPT plugin | retrieve Docs/Sheets/Slides evidence | pre-install exact tools/scopes not verified | broad Drive exposure, stale exported docs | **defer** |
| SharePoint | ChatGPT plugin | retrieve enterprise docs | pre-install exact tools/scopes not verified | tenant-wide sensitivity, version ambiguity | **defer** |
| Gmail/Outlook Email | ChatGPT plugin | person-directed evidence or notifications | not evaluated for this workflow | PII, send authority, prompt injection | **reject for bootstrap** |
| Calendar/Teams | ChatGPT plugin | scheduling/coordination | not needed for baseline | unrelated authority and personal data | **reject for bootstrap** |
| Serena | Codex MCP/tooling | semantic navigation in large codebase | local files, language server, edit/refactor/shell depending config | local execution, memory, maintenance | **document as candidate only in DR-005; defer now** |
| Context7 | Codex skill/MCP | current library docs/version mismatch | network/API/OAuth depending mode | community-doc accuracy, data egress | **document as candidate only in DR-005; defer now** |
| Playwright MCP | Codex MCP | persistent browser/UI investigation | browser profile, network, possible credentials | session leakage, token cost, not security boundary | **defer** |
| GitHub MCP | Codex MCP | issue/repo actions from executor | repo/API token; can be read/write | redundant authority, autonomous MCP actions | **defer** |
| Sentry MCP | MCP | production error/performance triage | OAuth, project endpoint | production data and action scope | **defer** |
| Project-specific MCP | MCP | expose otherwise inaccessible internal API | arbitrary | highest trust/maintenance burden | **reject until concrete bottleneck and threat model** |
| Orchestration gateway/Symphony | orchestrator | dispatch issue-driven parallel/AFK work | tracker, filesystem, process, network, agent tools | broad unattended authority, preview maturity | **defer** |

### I.2 Capability and authority detail

| Tool | Read capability | Write/approval | Supported surfaces | Scope recommendation | Authority class | Failure/fallback |
|---|---|---|---|---|---|---|
| GitHub app/connector | repos, files, commits, issues, PR/check data, verified live reads | connector advertises write tools; actual write success/failure untested; app inherits global `Allow low-risk actions` | current ChatGPT surface observed; other surface/DR capability requires canary | provider installation limited to selected repo; `Always ask` or `Allow read actions`/equivalent ask-before-write; policy-level no-write until separate gate | operational connector, never policy owner | read-only git/API; manifest snapshot; block stateful gate |
| Slack | catalog confirms workflow integration only | exact send/write contract unknown pre-install | plugin Chat/Work generally; exact Slack surface/capability requires canary | dedicated workspace/channels, read first | evidence source/communication, not decision owner | user-provided permalink/export; repo adoption record |
| Figma | catalog indicates design implementation context | exact mutation tools unknown pre-install | plugin surfaces generally; DR unknown | specific files/projects | design evidence source | pinned export + frame/version reference |
| Rovo/Jira/Confluence | catalog indicates Jira/Confluence management | exact tool schema unknown pre-install | plugin surfaces generally; DR unknown | one site/project/space | possible future task/knowledge owner only after adoption | GitHub Issues or approved export |
| Notion | catalog indicates planning/research/knowledge workflows | exact write approval unknown | plugin surfaces generally; DR unknown | selected database/pages | evidence source only | export with version/date |
| Drive/SharePoint | document retrieval likely, exact scopes not exposed by catalog | write behavior unknown | plugin surfaces generally; DR unknown | selected drive/folder/site | evidence source only | reviewed export/snapshot |

No App belongs in the committed bootstrap structure except a statement of non-selection and the already completed GitHub read canary recorded in this report. For any later candidate, capture separately: provider account/repository scope, connector actions, workspace action controls and ChatGPT approval mode. Exact install-time scopes must be captured only if a later bottleneck justifies evaluation. OpenAI confirms these controls do not grant one another's authority. [Managing app permissions in ChatGPT](https://help.openai.com/en/articles/20001495-managing-app-permissions-in-chatgpt)

### I.3 MCP selection rules for later DR-005

For every selected MCP record: exact bottleneck, consumer role, server origin, version/commit digest, auth method, filesystem/network/write scope, maintainer, threat model, canary, fallback, disable procedure, last_verified_at. Не використовувати “latest” в accepted config. Prefer read-only first, fine-grained token, project endpoint, isolated profile, explicit network allowlist.

**Serena:** evaluate only inside a representative large project against baseline rg/LSP/manual navigation; require read-only navigation canary before enabling edits.  
**Context7:** use for narrow version-specific library questions; verify load-bearing claims against official upstream docs. Ordinary official web docs remain fallback.  
**Playwright MCP:** use only if persistent interactive browser state materially beats Playwright CLI/skills; isolated profiles per task, never production profile.  
**GitHub tooling:** one authority path per executor. Prefer git/gh or a repo-scoped read-only MCP, not several concurrent writers.  
**Sentry MCP:** project-scoped endpoint and sanitized data only after production-observability ownership exists.  
**Project-specific MCP:** requires security review, schema versioning, least privilege, audit logging, failure isolation and a non-MCP fallback.

Apps і MCP є різними runtime layers, але не потребують двох bootstrap documents. Після DR-005 один docs/tooling/tool-registry.md з mandatory field **layer** мінімізує duplicate status. Split до separate App/MCP registries виправданий лише при різних owners або materially different update cadence.

### I.4 Alternatives

Шкала: L = low, M = medium, H = high. Для context cost, maintenance, stale risk, migration cost і security exposure нижче краще.

| Alternative | Clarity | Authority ownership | Context cost | Maintenance | Stale risk | Extensibility | Empty-bootstrap fit | Migration cost | Security exposure | Verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| A. Seven files unchanged | M | tooling owner missing | M | H | H | H | L | L | M | reject |
| B. Merge App matrix + MCP stack now | M | one inventory owner | M | M | H | H | M | L | M | defer merged registry to DR-005 |
| C. Defer both tooling files | H | no false owner | L | L | L | H | H | L | L | **recommend** |
| D. GitHub Issues/Projects instead of Markdown register | H after setup | tracker can own state | L | M | M if dual-write | H | M-low for unborn repo | M | M | defer selection; migrate later |
| E. Move charter under docs | M | unchanged | M | L | L | H | M | L | L | reject |
| F. Create architecture/ADR/CONTEXT/templates/schemas now | L | mostly absent | H | H | H | M | L | H | M | reject/defer |
| G. One ChatGPT Project | M | mixed research/decision authority | H | L | H contamination | M | M | M | M | fallback only |
| H. Store Project Instructions templates now | M | adapter owner unclear before canary | M | M | H | H | M-low | L | M | defer until UI canary |
| I. Merge charter into README | L | normative/navigation mixed | L | M | H | L | M | M | L | reject |
| J. Put research register in README | L | landing/state mixed | M | M | H | L | M | M | L | reject |
| K. One BOOTSTRAP.md for everything | M initially | authority types mixed | M | H | H | L | M | H | M | reject |

#### Alternative A

Має зрозумілу візуальну симетрію, але tooling files одразу міститимуть catalog snapshots, не selected stack. Вони створять уявну повноту й два maintenance queues без adopted DR-005 process.

#### Alternative B

Краща за A, бо App і MCP розрізняються полем layer, а спільні поля trust/scope/fallback не дублюються. Однак створювати навіть unified registry до першого verified candidate/owner передчасно.

#### Alternative C

Найменший responsible design. Міграційна вартість низька: після DR-005 додається один файл, а не переписуються дві speculative matrices.

#### Alternative D

GitHub Issues/Projects краще масштабуються для dependencies, assignees і automation. Але unborn repo ще не має прийнятої status taxonomy, а research register має бути доступним в exact baseline та offline clone. Після adoption tracker слід мігрувати одноразово, залишивши Markdown pointer. GitHub не підтверджує, що Issues самі усувають duplicate truth.

#### Alternative E

Charter є cross-cutting root authority. Переміщення під docs зменшує discoverability без виграшу в lifecycle чи security.

#### Alternative F

OpenAI case study має багату docs hierarchy, але вона виникла разом із реальним codebase і механічним doc gardening. Копіювати кінцеву форму в empty control repo означає плутати observed mature harness із bootstrap requirement. [Harness engineering](https://openai.com/index/harness-engineering/)

#### Alternative G

Один Project дешевший в адмініструванні, але raw research, `Default memory` і adopted decisions матимуть shared contamination surface. Два Projects залишаються виправданими як authority/context firewall. `Project-only memory` є офіційною capability, а його видимість залежить від account/workspace memory settings. Якщо effective configuration не дозволяє його увімкнути, setup зупиняється для виправлення settings або explicit risk decision; один Project із separate chats не є еквівалентною ізоляцією.

#### Alternative H

Versioned Project Instructions templates є корисними як thin adapter, але тільки після перевірки реальних UI fields, effective memory configuration і source/plugin behavior. Створені зараз templates швидко стали б documentary fiction.

#### Alternatives I-K

Вони зменшують кількість файлів ціною змішування різних authority classes та update triggers. Це не responsible minimalism.

## J. Deep Research operating model

### J.1 When to use

Deep Research доречний, коли одночасно присутні кілька ознак:

- питання широке, multi-source і впливає на architecture/security/tool adoption;
- факти temporally unstable;
- потрібне зіставлення primary sources і contradictions;
- corpus завеликий для точкового ordinary chat;
- потрібний reusable cited evidence report;
- internal approved sources треба зіставити з public evidence.

### J.2 When not to use

- exact repository state: використовувати connected GitHub/git/API;
- один вузький current API/library fact: official docs або Context7 як discovery, потім upstream verification;
- просте пояснення чи brainstorm: ordinary chat;
- implementation або code navigation: repository tools, rg/LSP/Serena candidate;
- рішення, яке вже прийняте: читати normative artifact;
- research question без clear decision consumer: спочатку clarify;
- production evidence без approved data handling.

### J.3 Source and lifecycle contract

**Source hierarchy:** current connected repo facts → official OpenAI/GitHub → current primary repositories/docs → protocol specs/papers → first-party case studies → documented practitioners → secondary discovery.

**Freshness:** кожен report має evidence_as_of. Temporally unstable platform/tool facts перевіряються в день gate. New evidence не редагує стару дату мовчки.

**Primary vs secondary:** load-bearing claims потребують primary source. Secondary source дозволений для discovery або явно позначеного practitioner counterexample.

**Contradictions:** report показує обидва джерела, їх dates/scopes, не усереднює. Для цього correction official Help Center є current source для `project-only memory`; старе negative finding із narrower Learn corpus superseded. Canary тепер перевіряє effective account/workspace/surface configuration, а не існування capability.

**Minimum report metadata:**

    id
    artifact_status: draft | active | superseded | archived
    authority: evidence
    research_status_at_publication
    recommendation_status_at_publication
    evidence_as_of
    owner
    question
    scope
    repository_state
    supersedes

`artifact_status: draft` застосовується до pre-review deliverable, який ще не є current repository evidence owner. Source-reviewed version, materialized before candidate SHA, має `artifact_status: active`. `research_status_at_publication` і `recommendation_status_at_publication` не змінюються. Optional publication metadata: sensitivity, source-review request/ref. Після materialization current `research_status`, `current_decision_status`, `adoption_scope`, `adoption_ref`, `superseded_by` і `next_gate` належать register, не note.

**Review gate:** fresh reviewer перевіряє representative citations, primary-source preference, dates, contradictions, unsupported negatives, sensitive data та відтворюваність repo facts. Авторський self-review не позначає note reviewed. Оскільки repository register ще не існує, reviewer створює explicit durable review result/reference як authorization input; він не “оновлює register”.

**Adoption gate:** до execution coordinator називає exact recommendations, six-file design, target normative artifacts/content contracts і exceptions та створює explicit adoption record/reference як authorization input. Register на цьому gate ще не існує. Authorized execution пізніше вперше materializes `current_decision_status`, `adoption_scope` і `adoption_ref` у новому register; note не редагується для зміни publication-time recommendation status. Candidate SHA також ще не існує. “Adopt report” не є достатнім рішенням.

**Storage:** canonical note path `docs/research/ADW-BOOTSTRAP-RESEARCH-001.md`; наступні notes використовують `docs/research/<ID>.md`, якщо окреме naming policy не прийнято. Під час authorized materialization новий register уперше записує current state і link, а після цього підтримує їх як sole owner. Raw source dumps не commit за замовчуванням через copyright, sensitivity і context cost.

**Supersession:** material new evidence створює successor note з новим `evidence_as_of` і explicit `supersedes`; старий note лишається historical evidence. Перехід pre-review draft → active candidate materialization без зміни evidence не змінює publication-time fields. Normative artifact змінюється окремо. Після candidate commit будь-яка correction створює новий SHA.

### J.4 Future parallel slices and AFK readiness, без bootstrap schema

| Concern | Що baseline має зробити зараз | Що чекає Workflow v1 research/adoption |
|---|---|---|
| Dependency DAG | register може показати research dependencies | task tracker native blockers/dependencies |
| Vertical slices | charter не забороняє; report фіксує evidence | task contract вимагає end-to-end demoable slice |
| Interface dependencies | нічого | explicit contract/test seam у task |
| File/symbol ownership | нічого | affected surfaces + exclusive/shared ownership |
| Resource locks | заборонити concurrent writes to same source | named DB/port/account/fixture/branch locks |
| Execution waves | нічого | topological release only for unblocked tasks |
| Worktree isolation | mention accepted premise, no dirs/config | one branch/worktree/environment per implementation task |
| Merge serialization | нічого | queue, base refresh, conflict owner, re-review |
| Budgets | no invented numbers | token/time/cost/retry/parallelism limits per task/harness |
| Stop conditions | hard boundary: ambiguity/permission/safety → stop | explicit stalled, failed verification, scope drift, budget exhaustion |
| Fresh review | acceptance principle only | new context reviews fixed SHA/diff |
| Architecture drift | no empty architecture doc | review against adopted architecture/ADRs when they exist |
| Context budget/dumb zone | concise AGENTS; no universal threshold | harness-specific threshold; clear/compact/handoff decision |
| AFK readiness | no automation | ready only with frozen scope, isolated environment, verification, observability, recovery, stop/escalation and no unresolved judgment |

Symphony’s issue-state machine, eligible-candidate checks, blocker rule, bounded concurrency, reconciliation і handoff state є strong future evidence, але repo explicitly warns it is an engineering preview for trusted environments. Це підтримує “support later”, не “encode now”. [OpenAI Symphony report](https://openai.com/index/open-source-codex-orchestration-symphony/), [Symphony repository](https://github.com/openai/symphony)

## K. Risks and mitigations

| Risk | Evidence | Impact | Mitigation | Bootstrap blocker |
|---|---|---|---|---|
| GitHub permission layers conflated | provider metadata reports admin/maintain/push/triage; connector exposes write tools; approval inherits `Allow low-risk actions` | agent або reviewer помилково вважає writes гарантовано allowed, impossible або approval-free | document three layers; selected-repo provider scope; no-write rule; read-only canary; `Always ask` or `Allow read actions` before later execution | **так**, якщо no-write setup cannot be maintained |
| Wrong or stale repository state | connector/snapshot may fail or lag | decision against nonexistent files/SHA | reverify repo/default branch/full SHA; block gate on failure | **так** для state-dependent gate |
| Secrets in Project files/memory | memory and connected sources persist context | credential leakage and cross-task reuse | no secrets; redaction; external secret manager; retire snapshots; disable memory ingestion for sensitive research where available | **так** |
| Research silently becomes policy | Deep Research produces polished report | unreviewed claims become commands | publication-time metadata in note; current disposition only in register; source review; target-specific adoption | **так** |
| Dual-write research state | note and register both claim current adoption/review status | stale contradictions and false adoption | note is evidence snapshot; register is sole current-state owner; successor for material evidence | **так** |
| Pre-materialization state assigned to a nonexistent register | source review and adoption happen before the six files are created | fictional durability and impossible update sequence | treat review/adoption records as authorization inputs; authorized execution creates and initializes register for the first time | **так** |
| Decision adoption, artifact lifecycle and baseline acceptance conflated | file metadata was expected to change after exact candidate SHA review | impossible same-SHA transition, false baseline acceptance або needless metadata-only commit | adopt normative content before execution; materialize six files as active; keep candidate/reviewed/accepted/superseded SHA state in a durable acceptance record | **так** |
| Two task trackers | Markdown + Issues/Projects/Linear | split state, missed dependency, false readiness | one owner; migration then pointer; no dual-write | так перед scale-up, ні для six-file bootstrap |
| Planned docs read as current implementation | empty architecture/tooling/schemas | agents obey fiction | do not create speculative artifacts; `artifact_status: active` only for current owners in the candidate revision; baseline state resolved by exact SHA record | **так** |
| Monolithic AGENTS.md | OpenAI observed context crowd-out/rot; empirical study shows cost/success downside | lost task context and stale instructions | hard maximum 3 KiB; map/pointers only; no duplication | **так** |
| Untrusted MCP | MCP threats and arbitrary tool/auth scope | exfiltration, unintended writes, local compromise | primary-source review, pinning, least privilege, sandbox, canary, fallback | **так** для any MCP enablement, не baseline |
| App write capability | pre-install scopes not visible in catalog | silent external mutations | defer; permission capture; read-first; per-action approval | так для connection, не baseline |
| Sensitive code in research report | multi-source Work/DR and Projects | exposure beyond intended repository/team | minimum necessary excerpts, classification, no full private dumps, approved sources only | **так** |
| Shared checkout parallelism | Matt docs report branch/stash/amend failures; OpenAI recommends worktrees | cross-task contamination, wrong commit | isolated worktree/branch/environment; shared-resource locks | так before parallel implementation |
| Passing checks mistaken for acceptance | checks/PR are evidence stages only | incomplete or wrong feature lands | explicit live and final acceptance tied to SHA/outcome | **так** |
| Candidate SHA rewritten | amend/rebase changes reviewed object | review evidence no longer applies | no amend/rebase after review begins; fixes in new commit; re-review | **так** |
| Branch protection assumed impossible or automatically suitable before unborn `main` | GitHub allows a rule to name a nonexistent branch, while plan and selected settings affect availability, bypass and branch creation | needless unprotected exception or a rule that blocks the authorized first-commit path | pre-materialization capability/configuration check; preconfigure only when compatible; otherwise explicit one-time exception and immediate post-candidate protection | **так** |
| AFK on ambiguous work | Symphony says judgment-heavy work remains interactive | costly drift and broad unintended action | readiness checklist, budget, stop/escalation, no production writes | так before AFK |
| Approval classification or policy mismatch | OpenAI says available app permission options vary by account/app/connection/workspace and sensitive actions may be blocked | unexpected prompt, denial or unintended low-risk execution | inspect effective mode; prefer `Always ask` or `Allow read actions`; policy-level separate gate for every write | так for high-authority actions |
| Human attention overload | OpenAI reports painful context switching beyond 3-5 sessions in its environment | missed review, coordination failure | bounded waves, issue control plane later, proof-of-work summaries | ні для bootstrap, так before scale |

Minimal bootstrap security posture:

1. private repository;
2. GitHub read-only canary and no connector writes;
3. `Always ask` or `Allow read actions`/equivalent ask-before-write where available, plus a separate explicit execution gate for every write;
4. no production accounts, tokens, secrets, sensitive full-repo uploads;
5. no new Apps/MCP/skills/hooks;
6. exact full-SHA review targets and no reliance on a movable ref as sole acceptance proof;
7. fresh-context source review and candidate review;
8. before materialization, check branch-protection/ruleset capability, plan and exact configuration; configure a rule targeting unborn `main` if it preserves the authorized bootstrap creation path, otherwise record a one-time exception and enable protection immediately after the first candidate;
9. human/coordinator acceptance distinct from checks;
10. failure-closed behavior for connector freshness and permission ambiguity.

GitHub documents that a branch named in a protection rule does not have to exist yet. It also documents plan-dependent availability and settings that can restrict creation of matching branches. Therefore pre-creation configuration is possible, but its operational suitability for this private repo and intended first-commit path is not assumed. Perform the capability/configuration check first: configure protection before materialization when it will not block authorized creation; otherwise explicitly authorize one bootstrap exception, record the plan/tier/configuration limitation and enable protection immediately after the first candidate. [GitHub: Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule), [GitHub: About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)

## L. Recommended bootstrap sequence

### 1. Reverify empty repository

**Outcome:** current visibility, default branch, contents і unborn state known immediately before execution.

**Files/actions:** read-only repository metadata, root contents and commits.

**Acceptance gate:** private; main; root 404 empty; commits 409 empty; no SHA. If any file/SHA exists, stop and diff this design against actual state.

**Rollback/failure:** no mutation. Connector failure blocks the empty-state assumption; use authorized read-only git/API or a manifest snapshot and mark unverified.

### 2. Independent source review of this note

**Outcome:** citations, current facts, contradictions і repository observations reviewed by a fresh context/person.

**Files/actions:** review this report only; produce findings, no repo writes.

**Acceptance gate:** no unresolved load-bearing factual error; unsupported claims corrected; fresh reviewer produces an explicit durable review result/reference. Це authorization input для later execution, не update до `research-register.md`, якого ще не існує. Current deliverable remains `artifact_status: draft` until execution materializes the source-reviewed active evidence file; publication-time research/recommendation fields stay unchanged.

**Rollback/failure:** no repository materialization is authorized. Issue a corrected revision, with a new `evidence_as_of` when evidence materially changes, and repeat source review. Do not claim that a nonexistent register preserved any state.

### 3. Explicit bootstrap adoption decision

**Outcome:** coordinator selects exact tree/contracts and records rejected/deferred alternatives.

**Files/actions:** decision names this note/revision, six-file tree, exact normative content contracts and exceptions and creates an explicit adoption record/reference. Це authorization input; register ще не існує. Still no repo write until authorized execution task.

**Acceptance gate:** scope, owner, orthogonal metadata, tooling deferral and first next task agreed; charter and research-policy decisions are adopted before their files are materialized. Candidate SHA does not yet exist.

**Rollback/failure:** defer implementation; request only the missing decision evidence.

### 4. Check branch-protection capability and bootstrap path

**Outcome:** exact GitHub plan/configuration path for unborn `main` is known before materialization.

**Files/actions:** inspect, without repository content writes, whether this private repository can create a branch protection rule or ruleset targeting unborn `main`; verify whether required reviews, status checks, branch-creation restrictions, bypass behavior and the intended first-commit method would block bootstrap creation. Record plan/tier and configuration limitations.

**Acceptance gate:** choose exactly one authorized path. Path A: configure an appropriate rule before the first commit because it targets unborn `main` and still permits the intended bootstrap creation path. Path B: when plan/configuration or creation semantics make Path A unavailable or unsuitable, record an explicit one-time bootstrap exception and the requirement to enable protection immediately after the candidate SHA exists. Do not assume either path without this check.

**Rollback/failure:** do not materialize while the creation path is ambiguous. Narrow the rule, choose a permitted creation method or explicitly approve Path B. Do not create a repository file to simulate protection.

GitHub states that the branch named in a protection rule does not have to exist yet, but availability and relevant restrictions vary by plan, repository ownership and selected settings. [GitHub: Managing a branch protection rule](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule)

### 5. Materialize the adopted six-file design

**Outcome:** working tree contains exactly six files from section E, no empty directories, no tooling/automation.

**Files/actions:** through a separately authorized execution task, create AGENTS.md and README.md as active navigation, PROJECT-CHARTER.md and research-evidence.md as `active/accepted/bootstrap/normative`, research-register.md as `active/bootstrap/research-index`, and the source-reviewed research note as `active/evidence`. Its publication-time recommendation remains `proposed`. This is the first creation of `research-register.md`. Initialize it from the prior review and adoption authorization inputs with reviewed research status, current bootstrap decision status, `adoption_scope`, `adoption_ref`, artifact link and `next_gate`; відтоді register є sole owner of mutable disposition.

**Acceptance gate:** links resolve; metadata exactly matches adopted contracts; register values faithfully materialize the explicit review/adoption inputs; no file uses metadata to claim candidate review or baseline acceptance; no secrets, Workflow v1 or duplicate owner; working tree diff equals authorized tree.

**Rollback/failure:** before commit, correct the working tree under the same execution task. Do not create candidate SHA until all six files match the adopted design.

### 6. Create the exact candidate commit SHA

**Outcome:** one full SHA content-addresses the complete six-file candidate.

**Files/actions:** create the first commit on unborn main through Path A or the explicitly authorized one-time Path B from step 4. Record its exact full SHA as `candidate`; do not change file metadata to represent this state.

**Acceptance gate:** committed tree equals the verified working-tree scope from step 5; all six files are present; no untracked or extra files; exact full SHA recorded.

**Rollback/failure:** once review starts, do not amend/rebase the candidate. Any correction creates a new SHA and invalidates review of the prior SHA.

### 7. Verify or enable protection for main

**Outcome:** the first candidate is no longer followed by an open-ended unprotected change path.

**Files/actions:** for Path A, verify that the configured rule actually matches created `main` and enforces the intended restrictions. For Path B, enable the selected protection/ruleset immediately after the candidate SHA and before candidate review. Record any plan/tier/configuration limitation outside repository content unless a separately adopted governance artifact has an owner.

**Acceptance gate:** force push/deletion controls and any feasible review/check settings match current team reality; the candidate SHA remains unchanged. If a desired setting is unavailable, a documented manual control has an accountable owner and expiry/recheck gate.

**Rollback/failure:** stop before candidate review. Fix configuration or explicitly document the minimum manual control; do not treat an unverified rule as effective.

### 8. Fresh review of the candidate SHA

**Outcome:** the exact candidate SHA becomes a reviewed SHA, not yet an accepted baseline.

**Files/actions:** independent reviewer verifies the full SHA/tree/content against the adopted six-file design and section M. Record findings against that SHA; do not edit its files.

**Acceptance gate:** no blocking finding; materialization matches adoption decision; metadata is already final for this revision; durable review record names the exact SHA.

**Rollback/failure:** reject that SHA. Execution creates a corrected new SHA, and fresh candidate review restarts for the new SHA.

### 9. Coordinator baseline acceptance

**Outcome:** exact full SHA becomes accepted baseline.

**Files/actions:** coordinator accepts the reviewed SHA as Bootstrap Context Baseline v0 and creates a durable acceptance record/pointer naming that exact full SHA. Do not modify any file in that SHA. A tag is optional only if repository governance separately adopts protected/signed-tag rules.

**Acceptance gate:** exact full candidate SHA + fresh review of that SHA + explicit coordinator acceptance tied to that SHA + durable acceptance record/pointer. A normal Git tag is a movable/deletable ref and must not be the sole proof or mandatory bootstrap blocker.

**Rollback/failure:** withhold acceptance or supersede an already accepted baseline only by accepting a new reviewed SHA. Do not retarget an acceptance record. If an optional tag was used, verify its rules/signature and never treat it as stronger than the underlying SHA-linked acceptance record.

GitHub documents API operations that update a reference to a new SHA and delete a reference. Rulesets can separately control who may delete or rename tags; signed tags add verifiable signature evidence. Therefore an ordinary annotated tag is useful navigation, not immutable acceptance evidence. [Git references API](https://docs.github.com/en/rest/git/refs), [GitHub rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), [Signing tags](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-tags)

### 10. Create the two ChatGPT Projects

**Outcome:** Command Center and Research Lab have distinct inputs/memory roles.

**Files/actions:** configure only after baseline SHA exists; apply minimal instructions that name repo/full SHA and authority order; do not import old long chat.

**Acceptance gate:** Project settings show `Project-only memory` for Command Center and `Default memory` for Research Lab; after any setting delay, canary verifies same-Project continuity, cross-project isolation, Sources, expected lack of Work in Command Center, Work availability in Research Lab and installed App visibility. Capability is official; failures here are effective account/workspace/surface configuration findings.

**Rollback/failure:** wait the documented several-hour propagation window, check account/workspace memory controls, then archive a persistently misconfigured Project and create a clean epoch; do not copy contaminated transcript. Do not treat one-Project/default-memory fallback as equivalent isolation.

### 11. GitHub canary

**Outcome:** each Project can read the exact accepted baseline without write.

**Files/actions:** verify provider identity/selected-repository scope; inspect connector action inventory and effective approval mode without changing them; ask GitHub connector for README, PROJECT-CHARTER.md і research-register.md at accepted full SHA; compare identifiers. Do not invoke a write action.

**Acceptance gate:** exact content and SHA match; provider, connector and approval layers recorded separately; selected-repository scope confirmed or limitation documented; no write action attempted. Before any later connector write, require `Always ask` or `Allow read actions`/equivalent and a separate execution gate.

**Rollback/failure:** reconnect/check scope; use read-only git/API or versioned snapshot. Mark state unverified and block adoption/implementation until freshness restored.

### 12. Start DR-001

**Outcome:** evidence for coordinator gates and artifact lifecycle from grill → task contract → candidate SHA → independent review → live/final acceptance.

**Files/actions:** create one planned register entry, then execute research in Research Lab under research policy. Не реалізовувати workflow або automation.

**Acceptance gate:** bounded research plan, primary sources, source-review owner, explicit decision consumer.

**Rollback/failure:** narrow or defer DR-001; no policy change.

## M. Bootstrap acceptance checklist

Fresh coordinator повинен визначити з committed artifacts, без старого чату:

- [ ] repository purpose;
- [ ] authority hierarchy і one-owner rule;
- [ ] current maturity та відсутність Workflow v1;
- [ ] distinct decision-adoption, artifact-lifecycle and commit/baseline-acceptance planes;
- [ ] orthogonal `artifact_status`, `adoption_status`, `maturity` і `authority` meanings;
- [ ] current research status і current decision status from the Research Register only;
- [ ] next research task DR-001 from the Research Register, not README or AGENTS.md;
- [ ] why research is not policy;
- [ ] how GitHub full SHA and connector canary are used;
- [ ] why Project memory/snapshot is non-authoritative;
- [ ] what bounded executors must not do;
- [ ] who can adopt a decision and accept outcome;
- [ ] that checks, report, commit and PR do not equal acceptance;
- [ ] connector failure and stale snapshot behavior;
- [ ] no tool is selected merely by appearing in catalog;
- [ ] no speculative directories or duplicate trackers exist.

Exact baseline gate:

- [ ] tree exactly matches section E;
- [ ] all internal links resolve;
- [ ] AGENTS.md ≤ 3 KiB and contains only map/boundaries;
- [ ] README is navigation, not policy;
- [ ] candidate PROJECT-CHARTER.md and research-evidence.md already say `active/accepted/bootstrap/normative`, because adoption preceded execution;
- [ ] candidate AGENTS.md and README.md are active navigation; candidate research-register.md is `active/bootstrap/research-index`;
- [ ] source-reviewed candidate research note is `active/evidence`, remains visibly non-normative and preserves publication-time recommendation `proposed`;
- [ ] research note contains publication-time status only; register alone has mutable `research_status`, `current_decision_status`, `adoption_scope`, `adoption_ref`, `superseded_by`, `next_gate`;
- [ ] source-review and bootstrap-adoption records existed first as explicit authorization inputs; execution created and initialized register for the first time, without claiming any pre-materialization register update;
- [ ] README and AGENTS.md only point to register for current work/next gate;
- [ ] branch-protection capability/configuration was checked before materialization; either a suitable rule targeted unborn `main`, or an explicit one-time exception was recorded and protection was enabled immediately after the candidate;
- [ ] no secrets, production accounts, Apps/MCP/skills/hooks/automation;
- [ ] fresh source review passes;
- [ ] fresh review of exact candidate full SHA passes;
- [ ] candidate → reviewed → accepted baseline state is recorded outside file front matter;
- [ ] no metadata mutation is required after candidate SHA creation;
- [ ] coordinator explicitly accepts that SHA;
- [ ] durable acceptance record/pointer names that exact SHA;
- [ ] any tag is optional and not the sole acceptance evidence.

Post-baseline Project/connector gate:

- [ ] both Projects reference the accepted full SHA;
- [ ] GitHub read canary returns that accepted full SHA without a write action;
- [ ] connector failure or stale snapshot blocks subsequent state-dependent work, not the already completed SHA acceptance record.

### M.1 Direct answers to the 20 required questions

| # | Answer |
|---:|---|
| 1 | Так. Окремий central repo має distinct cross-project governance owner; product execution state лишається у product repos/selected tracker. |
| 2 | Seven-file structure є excessive в tooling частині та incomplete без bootstrap evidence note. Рекомендація: six-file tree. |
| 3 | До DR-001 мають існувати всі шість файлів section E, включно з source-reviewed active note at `docs/research/ADW-BOOTSTRAP-RESEARCH-001.md`, у coordinator-accepted baseline SHA. Шлях: source review authorization input → bootstrap adoption authorization input → branch-protection capability/configuration check → first materialization, включно з initialized register → candidate SHA → protection verification/enablement → fresh SHA review → baseline acceptance. |
| 4 | Tooling registry після DR-005; workflow mechanics після DR-001 synthesis/adoption; CONTEXT/ADR/architecture/templates тільки після real grill/decision/owner. |
| 5 | Рівно six-file tree section E, жодних empty directories або automation. |
| 6 | Bootstrap adoption decision передує execution, тому candidate charter/policy вже є `active/accepted/bootstrap/normative`. Candidate SHA ще не accepted baseline до fresh review і coordinator acceptance. Workflow v1, task schema, Apps/MCP choices і AFK mechanics лишаються undecided; effective Project configuration потребує canary. |
| 7 | File dimensions: `artifact_status`, `adoption_status` лише для normative decisions, `maturity`, `authority`. Research note зберігає publication-time statuses. До materialization review/adoption records є authorization inputs; після first materialization register володіє current research/adoption disposition. Commit plane окремий: candidate SHA → reviewed SHA → accepted baseline SHA → superseded baseline SHA. |
| 8 | Так. PROJECT-CHARTER.md має бути root-level як cross-cutting normative owner. |
| 9 | Так, спочатку. Це minimal versioned/offline index і sole owner mutable research state; після adoption одного external tracker він мігрує без dual-write. |
| 10 | Не на bootstrap. Пізніше один tool-registry з layer; split лише при різних owners/lifecycles. |
| 11 | Не зараз. Після account/surface canary можна зберегти thin versioned templates, які посилаються на authoritative files/SHA і не дублюють policy. |
| 12 | Обидва Projects зберігають repository + full 40-character baseline SHA + verified_at; advance лише після gate. |
| 13 | Failure-closed: retry/scope check → read-only git/API → manifest snapshot; mark unverified і block state-dependent gates. |
| 14 | Ім'я містить repo/branch/SHA-or-unborn/timestamp; manifest містить exclusions/sensitivity; retire при live same/newer SHA; не змішувати versions. |
| 15 | Minimum viable policy: use/no-use, source hierarchy, metadata, lifecycle, contradiction/freshness, source review, adoption, sensitive handling, supersession. |
| 16 | AGENTS.md каже read order, maturity, no-write/no-secret/no-silent-adoption, verify state, tests/PR not acceptance, escalate ambiguity. Він не описує Workflow v1. |
| 17 | README повідомляє purpose, maturity, start-here, authority map і scope та має stable pointer на Research Register. Він не дублює current next gate, policy, tracker або tool matrix. |
| 18 | Не створювати architecture, ADR, CONTEXT, specs, tasks, plans, templates, schemas, tooling, automation, MCP/skills dirs. |
| 19 | Prior source review and bootstrap adoption authorization inputs + faithful six-file materialization with initialized register + verified branch-protection path + exact full candidate SHA + fresh review of that unchanged SHA + explicit coordinator acceptance tied to SHA + durable acceptance record/pointer. File metadata does not change between candidate and accepted baseline; any correction creates and re-reviews a new SHA. Tag optional, не sole proof. |
| 20 | DR-001: дослідити coordinator gates та artifact lifecycle до Workflow v1, без automation/tool selection. |

## N. Real unresolved decisions

| Decision | Why evidence is insufficient | Constraints | Concrete options | Recommendation | Evidence that would change it | Latest safe decision point |
|---|---|---|---|---|---|---|
| Effective `Project-only memory` configuration on the user's account/workspace/surface | official semantics verified, але actual toggles, workspace enablement і propagation не перевірені цим report | Command Center must be project-only; Work unavailable there; Research Lab uses Default memory + Work | enable required memory settings; wait propagation; clean Project epoch; explicit defer if workspace policy blocks | account/surface canary; do not downgrade capability claim to “undocumented” | actual Project settings, workspace controls and isolation/Work behavior | before using Projects for state-sensitive work |
| Effective branch-protection path for unborn `main` | GitHub officially allows a rule to name a branch that does not exist, але plan/tier, repository ownership, selected settings, bypass actors and first-commit method determine whether preconfiguration is available and operationally suitable | no unconditional unprotected first commit; no rule may deadlock authorized bootstrap creation | preconfigure a compatible rule before materialization; or explicit one-time exception followed by immediate protection after candidate | run the read/configuration capability check and choose the least permissive workable path | repository Settings, current plan/tier, actor/bypass options and dry validation of intended creation path | before materialization |
| Durable acceptance record mechanism for first unborn commit | no adopted repository governance or PR path yet | exact full SHA + fresh review + explicit acceptance + durable record required; research register must not become a competing commit-state owner; ordinary tags movable/deletable | bounded GitHub PR/Issue record used only for SHA acceptance; externally retained coordinator decision record; protected/signed tag only as optional additional pointer | select the simplest durable SHA-linked mechanism during bootstrap adoption without migrating the research tracker or adding a seventh bootstrap file | governance owner, GitHub plan/ruleset/signing/audit requirements | before accepting first SHA |
| Long-term research tracker | no scale evidence or adopted issue taxonomy | one owner; offline baseline | Markdown; GitHub Issues/Projects; Linear/Jira | Markdown initially; migrate once task volume and dependencies justify | ≥5 concurrent research items, multi-owner queue, automation need | before dual-entry starts |
| One vs two tooling registries after DR-005 | no owner/update cadence yet | distinguish App vs MCP; avoid duplicate fields | unified layer registry; split registries | unified by default | separate security/operations owners or materially different cadence | at DR-005 adoption |
| Versioned Project Instructions paths/content | UI fields/memory/plugin behavior unverified | thin adapter only; no duplicate policy | no templates; one template with variants; two files | one small template per materially different Project after canary | UI canary shows same instructions suffice or surface cannot import | immediately after Project canary, before second epoch |
| GitHub least-privilege configuration achievable in current connector | target repo access and approval default observed; full installation repository set, workspace action controls and actual write outcome not tested | bootstrap read only; provider/capability/approval layers distinct; no settings changes in this task | selected-repo provider scope; broad provider auth + `Always ask`/`Allow read actions`; no connector | selected-repo access plus read-only canary; every write remains separately gated | provider installation screen, connector action inventory, workspace settings and an explicitly authorized later action canary | before any connector write or sensitive repo |
| Whether source review accepts this corrected draft or requires a corrected evidence revision | fresh independent source review has not occurred | current deliverable remains `draft/evidence`; candidate needs an `active/evidence` source-reviewed version; publication-time recommendation stays `proposed`; before materialization the review result is an authorization input, not register state | if review passes, execution materializes the same substantive note as `active` and initializes register from the review/adoption inputs; if findings change evidence, create an explicit corrected revision and review it | include only a source-reviewed `active/evidence` version as the sixth file, before candidate SHA is created | independent source-review findings | before materialization and candidate commit |
| Numeric context/dumb-zone budget | current evidence is harness-specific; no universal reliable threshold | context cost; model/surface variation | token threshold; phase signals; no number | no bootstrap number; evaluate per harness | telemetry correlating context use with errors/cost | before AFK/parallel Workflow v1 |

Не є unresolved decisions: існування і documented semantics `Project-only memory`; центральний repo; six-file recommendation; root charter; Markdown register now; no tooling files now; research-policy need; research/policy separation. Для них evidence достатнє до adoption gate.

## O. Recommended next action

**Наступний gate: `fresh independent review limited to the CORR-003-sensitive claims`.**
