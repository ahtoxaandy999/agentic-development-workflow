# Независимый adversarial review ADW-D13-PREREQUISITE-DESIGN-001

## Live-state и точный предмет review

**Live-state verification: PASS. STALE DESIGN BASIS не сработал.**

На момент проверки `main` репозитория `ahtoxaandy999/agentic-development-workflow` указывает ровно на commit `796fef15a7ba3b78b57c1f06f5911c6a3f85dad5`, а его tree равен `9c582a9cd004030bc7d0f10a58e6c77243997097`. Это тот же merge commit PR #10, который указан в proposal как live basis. fileciteturn2file0

Research Register на этом exact `main` фиксирует DR-006 как `research_status: reviewed`, `current_decision_status: accepted`, решение `accept-dr-006-evidence-and-authorize-bounded-d13-prerequisite-design`, а также `D5: CONFIRM DEFER`, `D13: CONFIRM DEFER`, `X3: CONFIRM REJECT`. DR-006-specific next gate остается `D13 prerequisite-scoping/design gate`; авторизация ограничена `design and propose only`, без PoC и выбора механизма. fileciteturn8file0 fileciteturn8file1

Контролирующий disposition `docs/research/ADW-DR-006-DISPOSITION-001.md` на live `main` имеет ожидаемый Git blob `85610d35b126bc49f68d814b5f47c7fcc41a2530`. Он прямо запрещает считать design, test plan, scenario matrix, evidence specification или acceptance bar уже выполненным D13 conformance prerequisite и сохраняет отдельность D5, D13 и X3. fileciteturn11file0

Применимый `AGENTS.md` подтвержден на blob `18d9b694de020f93c90a69940b21b2800c4a9297`. Он требует считать live repository state более авторитетным, чем snapshot/chat/handoff, не смешивать evidence, policy, mutable state и acceptance и останавливаться на authority conflict или stale/unverifiable state. fileciteturn3file0 Репозиторий также подтверждает Charter как владельца authority hierarchy и запрета на duplicate task owner, а `WORKFLOW-V1.md` как единственного normative owner Workflow v1. fileciteturn4file0 fileciteturn5file0

**Точный proposal subject review:** прикрепленный `ADW-D13-PREREQUISITE-DESIGN-001`, `artifact_status: proposed`, `normative_effect: none`, basis commit/tree совпадают с live basis. fileciteturn0file0 Локально по exact bytes прикрепленного `/mnt/data/Pasted text.txt` я получил:

`bytes = 65,733`  
`SHA-256 = eb06edc9b27c2c3a01210e8340f85a89723594f719b5c380fd75b76cd04fc9f8`

Локально вычисляемый Git-style blob SHA-1 этих bytes равен `320214335252f8dcca7194b3ae442ff0e18e4c83`, но это **не** remote Git object identity. Proposal не присутствует в проверенном repository state как опубликованный объект, и пользователь не предоставил authoritative expected proposal digest/blob. Поэтому review можно надежно привязать к exact attachment bytes и его SHA-256, но нельзя утверждать, что он привязан к уже существующему repository blob или immutable candidate SHA. Поиск exact ID в текущем репозитории также не обнаружил persisted copy. Это соответствует текущей стадии proposal, а не является stale-basis проблемой.

**Overall verdict: `REQUIRES_CORRECTION`.**

Finding counts:

| Severity | Count |
|---|---:|
| BLOCKER | 2 |
| MAJOR | 3 |
| MINOR | 0 |
| NOTE | 2 |

Главный вывод: архитектурное направление в целом правильное, transport-neutral и существенно лучше, чем прямое наследование Symphony semantics. Но exact proposal пока не определяет достаточно сильный semantic writer fence, а Stage 2 conformance contract допускает опасное смешение simulated controller evidence с фактическим D13 conformance evidence. Дополнительно остаются три material ambiguities в semantic-state ownership, restart state machine и operation-specific effect contract. Эти пробелы непосредственно затрагивают условия, которые DR-005 и DR-006 сделали prerequisites для reconsideration D13. fileciteturn10file0 fileciteturn10file1 fileciteturn11file0

## Findings

| ID | Severity | Exact section / clause | Finding |
|---|---|---|---|
| F-01 | **BLOCKER** | §14.1 Stage 2; §14.2; §15; §16 | Fixture/test-double evidence не отделено от actual D13 conformance prerequisite |
| F-02 | **BLOCKER** | §8.1-8.4; §6.2; §6.4; §13.2 | Active writer claim пока является сильным record/invariant, но не определенным semantic fence |
| F-03 | **MAJOR** | §4.1 row `Execution-control semantic state`; §4.5; §6.1-6.2 | Не определен точный boundary между designated Workflow execution-state owner и runtime controller |
| F-04 | **MAJOR** | §5.2-5.3; §4.5; §11-12 | Runtime state machine не замкнут для restart/reconciliation и нескольких failure paths |
| F-05 | **MAJOR** | §6.4; §10; §11.4; §13.2 | Effect contract задает общие требования, но не дает достаточных operation-specific semantics для всех разрешаемых consequential effects |

**F-01, BLOCKER: Stage 2 может превратить simulation в D13 conformance.**

Proposal §14.1 говорит, что Stage 2 "may use deterministic transport/effect test doubles or another non-operational fixture", после чего §16 определяет условия, когда "D13 conformance prerequisite is satisfied". §15 перечисляет сценарии, которые должны быть "actually exercised", но не устанавливает, какие из них должны проходить против реальных persistence/process/Git/transport/effect semantics, а какие можно удовлетворить полностью моделированным объектом. fileciteturn0file0

Это конфликтует с load-bearing distinction из DR-006 disposition: design, test plan, scenario matrix и evidence specification сами по себе D13 conformance не удовлетворяют; требуется **actual accepted conformance evidence**. fileciteturn11file0 DR-005, в свою очередь, разрешает reconsideration D13 только после accepted adapter/ownership design **и conformance evidence preserving DI-1/DI-2**, а DI-2 включает freshness, operation-aware retry, containment, recovery history и terminal guards. fileciteturn10file0 fileciteturn10file1 Workflow v1 требует перед retry классифицировать реальную operation semantics, устанавливать prior effects и блокировать blind retry при ambiguous completion. fileciteturn21file0

**Concrete failure mode:** coordinator получает полностью зеленый suite против deterministic fake transport, fake journal, fake process liveness, fake Git и fake side-effect port. Suite показывает "duplicate writer rejected", "process contained", "journal restored", "ambiguous effect reconciled". Proposal §16 позволяет назвать такой package удовлетворившим D13 prerequisite, хотя ни atomic fencing, ни actual crash durability, ни OS process containment, ни Git/ref semantics, ни transport resume/cancel semantics не были проверены.

**Smallest sufficient correction:** разделить conformance claims минимум на:

`abstract-controller conformance`  
`transport conformance`  
`target-environment conformance`

и прямо записать, что deterministic doubles могут давать только ограниченную evidence claim внутри abstract-controller layer. Fixture-only package **не может один** удовлетворить accepted D13 conformance prerequisite. Для prerequisite должно быть указано, какая минимальная часть требует exact runnable controller realization и real substrate behavior, даже если transport-specific и production-target behavior остаются более поздними gates.

**F-02, BLOCKER: writer claim не определен как настоящий fence.**

Proposal хорошо устанавливает invariant "at most one active write claim", claim ID, generation, denial duplicate dispatch, запрет timeout release и необходимость containment predecessor перед replacement. fileciteturn0file0 Но отсутствует semantic rule, которая делает claim **атомарно уникальным и непреодолимым stale writer-ом**.

Не определено:

- кто является единственным authoritative owner текущего claim;
- какая операция атомарно переводит `no current claim -> claim generation N`;
- как два controller instances после split-brain/restart не получают оба "valid" claim;
- должен ли каждый mutation path проверять текущую generation непосредственно перед effect;
- что происходит со stale holder generation `N` после выдачи `N+1`;
- через какой enforcement point stale writer физически или логически лишается возможности продолжить mutation.

Это особенно существенно потому, что существующий protected-write decision прямо говорит, что worktree isolation не решает fencing, а candidate-branch writer exclusivity в уже принятом operating path все еще является procedural limitation. fileciteturn19file0 Workflow v1 требует exactly one mutable owner и explicit/atomic ownership transfer на semantic boundary. fileciteturn6file0

**Concrete failure mode:** controller A держит claim generation 4. Controller A становится недоступен, но executor/process остается способным писать. Controller B после restart реконструирует journal недостаточно точно и выпускает generation 5. Поскольку generation не обязана проверяться на каждом write/effect boundary, старый executor generation 4 продолжает mutation одновременно с replacement executor generation 5. В журнале будет "one active claim", но реальных writers будет два.

**Smallest sufficient correction:** без выбора технологии определить semantic fencing contract:

`single authoritative claim owner/store -> atomic compare-and-acquire -> monotonic generation/fencing token -> mandatory current-generation validation at every write-capable boundary -> stale-generation denial -> release only after proven containment + reconciliation`.

Local workspace mutation, Git mutation и разрешенные external effects должны либо проходить через boundary, который проверяет current generation, либо дизайн обязан доказать другим способом, почему stale writer более не может produce effects. Claim record без такого enforcement нельзя считать fencing.

**F-03, MAJOR: semantic execution-state ownership остается двусмысленным.**

§4.1 использует формулировку `Existing project/task execution-state owner`, а в колонке runtime relationship говорит `Supplies/records semantic transitions`. §6.2 одновременно отдает controller "dispatch ordering". fileciteturn0file0

Workflow v1 намного точнее: task-control, cancellation и recovery transitions имеет единственного `designated run/task execution-state owner`; controllers и side-effect owners поставляют evidence, но не становятся вторым writer этих semantic planes. fileciteturn20file0 Explanatory task-control reference еще конкретнее: execution-control authority supplies transitions, а sole recorder `R` alone updates current projection. fileciteturn18file0

**Concrete failure mode:** реализация трактует "controller owns dispatch ordering" и "supplies/records semantic transitions" как право controller самостоятельно записать task `active`, `blocked` или recovery transition в своем journal или project task state. Возникают либо два owners, либо runtime state становится surrogate semantic state, что прямо нарушает DI-1.

**Smallest sufficient correction:** заменить vague owner на runtime-resolved exact role:

- authority resolver обязан возвращать exact designated task/run execution-state owner и, если применимо, sole recorder;
- controller может выдавать operation evidence / transition request;
- semantic owner или его designated recorder производит authoritative transition;
- controller начинает/возобновляет effect только после fresh authoritative observation соответствующего разрешенного transition;
- runtime journal никогда не является semantic transition record.

Это не требует выбрать конкретный task tracker или schema.

**F-04, MAJOR: restart reconstruction не имеет детерминированного destination rule.**

В §5.3 restart ведет в `RECONCILING`, но основной diagram показывает только последующий путь в `EXECUTOR_ACTIVE`. При этом controller может упасть во время `REVIEWER_ACTIVE`, `CORRECTION_ACTIVE`, `AWAITING_NEW_AUTHORITATIVE_CANDIDATE` или `FRESH_REVIEWER_ACTIVE`. Для этих случаев нет исчерпывающей mapping rule. В `FRESH_REVIEWER_ACTIVE` результат "anything else -> BLOCKED or TERMINATED" также оставляет реализации выбор между двумя semantic outcomes. fileciteturn0file0

Workflow v1 не разрешает timeout, silence, missing evidence или ambiguity превращать в success, а unresolved ambiguity требует block/intervention и сохраняет recovery history. fileciteturn21file0

**Concrete failure mode:** restart во время R1 review. После reconciliation один implementation возвращается в `REVIEWER_ACTIVE`, другой запускает replacement reviewer, третий попадает в `EXECUTOR_ACTIVE` по diagram. Все три могут формально утверждать соответствие proposal, хотя последствия для freshness, duplicate review и candidate binding различаются.

**Smallest sufficient correction:** добавить exhaustive restart/reconciliation projection:

`pre-crash runtime phase + authoritative semantic state + journal evidence + live worker state + workspace/Git state + outstanding effects -> exactly one allowed runtime destination or BLOCKED`.

Для каждого active/awaiting state должны быть определены at least `resume same operation`, `replace after containment`, `advance from already-completed exact effect`, `BLOCKED`, `TERMINATED`, с однозначными guards. `BLOCKED vs TERMINATED` нельзя оставлять implementation choice там, где решение зависит от authority/evidence.

**F-05, MAJOR: side-effect contract слишком общий для operation-aware conformance.**

§6.4 правильно требует explicit authority, expected state/version, reconciliation и exact result identity. Но §10 затем для нескольких effect classes оставляет правила в форме `operation-specific` или `tool/domain-specific`. В частности, local workspace mutation, Git object creation, PR update/publication и tracker mutation не имеют полного design-level tuple:

`authority + exact target + expected state + operation identity + ambiguity reconciliation + repeatability classification + safe retry predicate`. fileciteturn0file0

Workflow v1 требует именно operation-aware classification до retry и запрещает blind repeat при ambiguous completion. fileciteturn21file0 Existing protected write path уже конкретизирует один пример: branch push выполняется non-force с explicit expected state; ambiguous ready/merge требует read-only inspection и не повторяется без доказательства non-occurrence и fresh authority. fileciteturn19file0

**Concrete failure mode:** две реализации side-effect port по-разному трактуют ambiguous `create PR` или Git ref update. Одна считает operation idempotent по request identity, другая повторяет создание после transport timeout, третья блокирует. Proposal не дает conformance reviewer объективного основания определить, какая реализация правильная.

**Smallest sufficient correction:** определить общий mandatory effect descriptor и минимальные per-class semantics. Для операций, запрещенных будущим minimum PoC, достаточно явно сказать `no execution contract exists; only denial conformance applies`. Для разрешаемых Git/workspace effects нужно зафиксировать semantic retry/reconcile contract, не выбирая библиотеку или transport.

**NOTE N-01:** reviewer independence contract сам по себе сформулирован качественно. Fresh reviewer имеет новую execution identity и новую context, не наследует executor history, связан с immutable candidate SHA и не получает candidate mutation authority; correction создает C2 и fresh R2. Это соответствует Workflow v1 correction/re-review semantics. fileciteturn0file0 fileciteturn20file0

**NOTE N-02:** текущая App Server re-verification не создает D5 selection. Proposal использует App Server только как сравниваемый transport и явно сохраняет отдельный D5 gate. Это authority-safe. Более того, текущий upstream Codex продолжает показывать transport-specific edge cases вокруг `thread/resume`, что подтверждает необходимость отдельного transport/target validation, а не право считать documented protocol surface operational proof. citeturn0search0turn0search4

## Архитектурная оценка

**Authority model:** **CORRECTION REQUIRED.** Основная декомпозиция правильная: `authority resolver -> deterministic controller -> replaceable transport`, отдельно `side-effect/reconciliation boundary`. Runtime journal объявлен execution/recovery evidence, а не task/review/acceptance owner. Это сохраняет базовую идею DD-003 и DI-1. fileciteturn0file0 fileciteturn6file0 Но F-03 нужно исправить, потому что exact semantic execution-state owner и recorder boundary сейчас не достаточно определены.

**Runtime / recovery journal:** **PARTIALLY ACCEPTABLE, CORRECTION REQUIRED.** Плюсы: missing/corrupt journal не дает clean start; journal проигрывает live authority; unreconstructable writer/effect state блокирует continuation; recovery episodes не переписываются задним числом. Это соответствует reliance-based durability и fail-closed recovery. fileciteturn0file0 fileciteturn21file0 Недостаток: restart destination semantics не замкнуты, F-04. Retention boundary приемлема: journal может быть удален только после terminal runtime, отсутствия active claim, reconciliation consequential effects и передачи relied-on recovery evidence явному custodian. fileciteturn0file0

**Adapter architecture:** **PASS SUBJECT TO FINDINGS.** Transport не получает права определять Workflow v1 transitions, acceptance или candidate correctness. Authority resolver read-only. Side-effect port заявлен subordinate to authorization, а не generic scheduler. Архитектура действительно допускает Native Threads, App Server или другой transport без изменения Workflow semantics. fileciteturn0file0 Текущий Codex source также подтверждает, что protocol surface имеет собственные stable/experimental distinctions, поэтому transport-specific behavior разумно оставлять за отдельной evidence layer. fileciteturn17file0

**Writer fencing:** **FAIL, BLOCKS DESIGN ACCEPTANCE.** Design определяет хорошую policy вокруг ownership, но пока не определяет semantic fence, который объективно предотвращает stale/concurrent writer. F-02 load-bearing.

**Reviewer independence:** **PASS AT DESIGN-SEMANTICS LEVEL.** Fresh context, immutable SHA, отсутствие executor-history inheritance, отсутствие candidate-write authority, new SHA on correction и fresh affected review определены корректно. fileciteturn0file0 Реальное доказательство этих свойств конкретным transport остается отдельным conformance matter.

**External effects / recovery:** **CORRECTION REQUIRED.** Default deny, read-only reconciliation after ambiguity, no blind retry и exact candidate binding правильны. Но F-05 не позволяет одинаково реализовать и проверить все разрешаемые effect classes.

**DI-1:** **INTENT PRESERVED, ACCEPTANCE NOT YET PROVEN.** Proposal прямо различает runtime states и Workflow states и запрещает выводить acceptance/verification/review из worker completion. Это соответствует принятой DI-1 boundary: platform/runtime states не заменяют task, verification, review, disposition, normativity или acceptance planes. fileciteturn10file1 Но F-03 должен быть исправлен, иначе implementation может превратить journal/controller в second semantic owner.

**DI-2:** **INTENT PRESERVED, DESIGN CONTRACT INCOMPLETE.** Freshness, stale-authority denial, ambiguous effect handling, containment, retained recovery history и terminal guards присутствуют. fileciteturn0file0 Однако настоящая DI-2 conformance зависит именно от F-01, F-02, F-04 и F-05: simulated retry/containment или unenforced writer token нельзя считать доказательством operation-aware safety.

## D13 conformance evidence и роль fixtures

**Да, deterministic test doubles и non-operational fixtures могут легитимно доказать часть D13 prerequisite properties. Нет, они не могут самостоятельно доказать весь accepted D13 conformance prerequisite.**

Разрешенная claim boundary должна выглядеть так:

| Property | Fixture / test double sufficient? | Требуется более сильное evidence |
|---|---|---|
| Controller transition determinism | Да | Exact executable controller realization |
| Runtime state не означает Workflow pass/acceptance | Да | Controller transition tests |
| Stale authority input блокирует dispatch | Да, для controller decision logic | Реальный authority resolver integration позднее подтверждает freshness source |
| Automatic accept/ready/merge отсутствует | Да | Structural/interface tests |
| Correction требует C2 и new review assignment | Да, policy logic | Real Git needed to prove actual candidate identity behavior |
| Wrong candidate/reviewer subject rejected | Да, abstract identity checks | Real Git/transport for operational binding |
| Duplicate dispatch внутри одного controller instance | Да | Не доказывает global writer exclusivity |
| Atomic unique writer ownership | **Нет** | Real claim implementation, concurrency/crash exercise |
| Stale writer не может писать после replacement | **Нет** | Real process/effect containment plus fencing enforcement |
| Journal survives controller crash | **Нет**, не через in-memory fake | Real durable implementation and restart |
| Corrupt/missing journal fail-closed | Частично | Real storage failure/recovery exercise |
| Git object/ref expected-state behavior | **Нет** | Real Git repository/ref operations |
| Ambiguous Git mutation reconciliation | **Нет** | Real Git/remote or controlled equivalent with actual operation semantics |
| Transport fresh reviewer context | **Нет** | Actual selected transport |
| Transport resume/read/interrupt/reconcile | **Нет** | Actual selected transport |
| Reviewer lacks effective external write capability | **Нет** | Actual permissions/credentials/environment |
| GitHub/remote/tracker effect containment | **Нет** | Actual relevant target interface/environment |
| Target sandbox/process retention/credentials | **Нет** | Target-environment validation |

Эта граница следует из Workflow v1: evidence должен фиксировать expected/observed preconditions, operation identities, retries, dedup/version keys и reconciliation, а retry зависит от фактической operation semantics, не от названия mock method. fileciteturn21file0 DR-006 source review также прямо не сертифицирует target-environment runtime behavior и требует повторно проверять unstable App Server/Codex behavior на зависимом gate. fileciteturn12file0

**Следовательно, три conformance уровня должны быть разделены.**

`Abstract-controller conformance` подтверждает, что exact controller realization правильно реализует authority inputs, state transitions, negative guards, identity binding, DI-1 semantics и modeled recovery decisions. Deterministic doubles здесь уместны, но для writer fencing, durable restart и Git/process semantics внутри этой же layer нужны реальные integration substrates, а не только mocks.

`Transport conformance` подтверждает, что конкретный adapter для Native Threads, App Server или другого transport действительно обеспечивает lifecycle observation, executor continuity, fresh reviewer context, interruption/containment evidence и restart reconciliation без подмены Workflow semantics.

`Target-environment conformance` подтверждает actual filesystem/process behavior, credentials, sandbox/permission boundaries, Git remote behavior, protection configuration и allowed external effects в конкретной среде.

Эти levels не должны автоматически выдавать authority друг другу. Abstract-controller PASS не выбирает transport. Transport PASS не означает target deployment safety. Target conformance не означает acceptance или D13/D5 selection.

**Текущий proposal действительно рискует считать simulation evidence actual conformance.** Формулировка Stage 2 допускает non-operational fixture для "D13 conformance", а §16 затем определяет satisfaction всей prerequisite без claim-level distinction. Именно это является F-01 BLOCKER. fileciteturn0file0

При этом требовать target-environment conformance уже на current design gate было бы чрезмерно и означало бы смешать design acceptance с PoC/operational validation. Исправление должно определить evidence taxonomy и gate composition, а не выбрать transport или запустить PoC.

## D5 separation, PoC ceiling и скрытая authority

**D5 separation: PASS.** Proposal не выбирает App Server. Он сравнивает Native Threads и App Server как возможные adapter targets, прямо называет comparison non-selection verdict, сохраняет D5 `CONFIRM DEFER` и требует отдельный applicable D5 selection перед App Server-based PoC. Это в точности соответствует DR-006 disposition. fileciteturn0file0 fileciteturn11file0

Фраза о том, что App Server имеет более явные lifecycle primitives, сама по себе не является selection. Current pinned `openai/codex@b1f3c2f77e7cb802af0d8ef1c325cb6e9d39d8d9` действительно существует; current protocol source имеет explicit thread parameters и отдельно маркированные experimental fields. fileciteturn16file0 fileciteturn17file0 Но operational reliability этих primitives остается transport evidence, а не design proof, что дополнительно подтверждается недавними upstream reports о `thread/resume` edge cases. citeturn0search0turn0search4

**Future PoC ceiling: PASS.** Proposal удерживает максимальную форму:

`executor -> C1 -> fresh reviewer -> one correction -> C2 -> fresh reviewer -> STOP before human acceptance`

и отдельно допускает только controlled restart/reconciliation evidence и duplicate-writer denial. Automatic ready, merge, acceptance, tracker migration, distributed workers, parallel writers и AFK/unattended execution явно исключены. fileciteturn0file0 Это соответствует non-authorities DR-006 disposition. fileciteturn11file0

**Hidden mechanism-selection authority: не обнаружена.**

**Hidden implementation authority: не обнаружена.** Proposal несколько раз отделяет design acceptance от later conformance realization и прямо говорит, что conformance work требует отдельного gate. fileciteturn0file0

**Hidden PoC authority: не обнаружена.** Stage 3 только позволяет coordinator "consider" D13 PoC disposition после accepted design и accepted conformance, а Stage 4 остается отдельным actual PoC gate. fileciteturn0file0

**Hidden Workflow v1 amendment: не обнаружена.** Runtime controller не получает normative semantics authority, а D5/D13/X3 формально сохраняются. После исправления F-03 это разделение станет достаточно точным.

## Точные corrections required

До coordinator disposition proposal должен получить новый exact identity и fresh review. Нужны только следующие material corrections, без выбора технологии.

**Writer fencing:** заменить current claim model на explicit semantic fencing contract. В design должны появиться единственный authoritative claim owner, atomic unique acquisition, monotonic generation/fencing token, mandatory stale-generation denial на всех write-capable boundaries, explicit release/transfer guards и правило, что new generation невозможна до proven predecessor containment/reconciliation. Не требуется выбирать database, lock service или OS primitive.

**Conformance taxonomy:** переписать §14-16 так, чтобы fixture evidence имело явный claim ceiling. Отдельно определить abstract-controller, transport и target-environment conformance. Прямо запретить трактовать fixture-only suite как полное accepted D13 conformance prerequisite. Определить minimum prerequisite evidence, которое должно использовать real controller realization и real substrate behavior для durability, writer fencing, process containment и Git semantics.

**Semantic owner boundary:** заменить `Existing project/task execution-state owner` на runtime-resolved exact designated owner/recorder contract. Controller не должен записывать Workflow task-control/cancellation/recovery state. Он поставляет facts/request, затем перечитывает authoritative transition перед consequential dispatch/resumption.

**Restart state machine:** добавить exhaustive reconciliation transition matrix для restart из каждого active/awaiting state. Для каждой комбинации нужно иметь один outcome: resume same identity, recognize already-completed operation, replace only after containment, block/intervention, либо terminate. Убрать неопределенные choices вроде `BLOCKED or TERMINATED`.

**Effect descriptors:** для каждого effect, который design разрешает выполнять до/в minimum PoC, определить mandatory operation identity, authority, expected state, reconciliation readback и safe retry predicate. Для effects, которые minimum PoC запрещает, явно оставить только denial conformance, не проектируя преждевременно mutation implementation.

Эти corrections являются design-semantic, не mechanism-specific. Они не требуют выбирать Native Threads, App Server, Symphony, storage engine, lock implementation или GitHub automation.

После corrections прежний attachment SHA-256 `eb06edc9b27c2c3a01210e8340f85a89723594f719b5c380fd75b76cd04fc9f8` должен считаться историческим review subject. Материально исправленный текст требует новой exact identity и fresh independent affected review, поскольку Workflow v1 связывает review с immutable subject и требует нового identity после material correction. fileciteturn20file0

## Recommended next gate и итоговый disposition

**Recommended next gate: correction of `ADW-D13-PREREQUISITE-DESIGN-001`, затем fresh independent review exact corrected proposal.**

Не следует переходить к coordinator acceptance текущего текста как accepted D13 prerequisite ownership/adapter design. Также не следует переходить к implementation, conformance execution, D13 reconsideration, D5 selection или PoC.

После исправления design review должен прежде всего повторно проверить пять закрывающих predicates:

`semantic owner is unique`  
`writer claim is enforceable fencing, not bookkeeping`  
`restart has deterministic reconstruction`  
`allowed effects have operation-aware contracts`  
`fixture claims cannot masquerade as full D13 conformance`

Все остальные крупные архитектурные направления текущего proposal можно сохранить. Authority resolver, deterministic controller, replaceable transport, separate effect/reconciliation boundary, fresh-reviewer model, exact-candidate correction semantics, D5 separation и bounded PoC ceiling не требуют redesign.

**VERDICT: REQUIRES_CORRECTION**

**Finding counts: 2 BLOCKER / 3 MAJOR / 0 MINOR / 2 NOTE**

NOT READY FOR COORDINATOR DISPOSITION