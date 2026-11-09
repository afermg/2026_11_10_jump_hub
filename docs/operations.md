# Installation and operations (oppy / amunoz)

Installation and publication are owner-controlled. These commands document the
setup and recovery process; do not rerun new-install commands over existing state.
The implementation was delegated, then reviewed and integrated by the parent.

## Approved binding

- Source repository: `/work/users/amunoz/projects/org-overleaf-sync` → private
  `afermg/org-overleaf-sync`.
- Editable source: `deck/slides.org`; assets: `deck/assets/`.
- Private slides project: <https://overleaf.quasimorphic.com/project/6acfad6134af14083d8c4c89>.
- Exact credential-free Git Bridge URL:
  `https://overleaf.quasimorphic.com/git/6acfad6134af14083d8c4c89`.
- Branch: `master`; seed: `2a95a6433d4d280b885785c5a8ed6944aa4f94f5`.
  The seed contains only unowned `main.tex`, which must remain intact.
- Root after first publication: **slides.tex**; compiler: **XeLaTeX**.
- Runtime config: `/home/amunoz/.config/org-overleaf-sync/config.json`.
- Runtime state: `/home/amunoz/.local/state/org-overleaf-sync/`.
- Dedicated publication checkout: runtime state + `/publication`.
- The Methods project `6acfa89ad7845583ccca8d10` is explicitly forbidden by code.
  The separate JUMP-lite manuscript project is never a publication target.

Parent confirmed an actual noninteractive `git ls-remote` with the no-userinfo
URL returns the seed for HEAD and `refs/heads/master`; the existing netrc Git
credential helper works without any username override. Do not print or copy
credential stores, put tokens in commands/config/URLs, or change global Git
configuration. URL rewriting and HTTP redirects are rejected.

## Current publication contract

The validated bundle includes `slides.org`, `slides.tex` and the declared assets
actually used by the deck. The Org copy is the exact snapshot used for that build,
not a later read of the editable file. It is published in the existing private
Overleaf repository without changing the LaTeX root or compiler.

The local `deck/slides.org` remains the build source. At the presenter's
instruction, **direct Overleaf edits take content priority**: preserve them and
port them back into Org before publishing. Editing the Overleaf copy of
`slides.org` stops the next sync, just like editing generated TeX or an owned
image. Reconcile through the recovery procedure below; there is no automatic
reverse sync or conflict resolution. Speaker-note-only Org changes are also
published, even when the TeX and PDF would be unchanged.

## Private presentation distribution mirror

The source mirror for this talk is
`https://github.com/afermg/2026_10_21_faseb_jump_hub`, branch `main`, with local
checkout `/home/amunoz/Documents/broad/drafts/slides/2026_10_21_faseb_jump_hub`.
It follows the presenter's existing date-prefixed talk/poster repository names.
Keep this repository **private until explicitly instructed to make it public**.

The Slides QR on the main-talk closing page points to the future GitHub PDF viewer at
`https://github.com/afermg/2026_10_21_faseb_jump_hub/blob/main/slides.pdf`.
The PDF is intentionally absent and ignored by Git. **Do not commit/push it
until the presenter explicitly approves the final slides.** PDF publication
and making the repository public are separate authorization gates.

Refresh the mirror from a fetched, verified Overleaf snapshot after source
publication. Preserve the mirror's README and ignore rules, check privacy,
inspect the staged tree for PDFs, and push only source/consumed assets. There is
no automatic GitHub push, PDF upload or visibility change. Before a later public
release, review editorial comments and history for private operational details;
do not expose the original private authoring/Overleaf projects.

## Historical first-publication checks

The following list describes the original confocal starter. For the current
talk, verify the figures in `docs/assets.json` and inspect a fresh PDF preview.

1. Review code and the external PDF/evidence. Run the tests below.
2. Verify figure hashes against `docs/provenance.md`. The checked v9 example
   includes Background Compound-in-lysosome Manders, brief coefficient definitions
   and the supplied-image-set explanation. No remeasurement belongs here.
3. Rebuild and inspect the replacement figures and PDF. No cells-only Manders
   wording should survive. Keep the repository and slides project private.
4. Parent reviews/stages/commits the source and creates/pushes the private GitHub
   repository using its normal workflow. This exporter never commits source.

## Exact runtime configuration and first checked publication

After the pre-publication gate, run as `amunoz`, not root:

```sh
cd /work/users/amunoz/projects/org-overleaf-sync
install -d -m 700 /home/amunoz/.config/org-overleaf-sync
# New install only: do not overwrite an existing runtime config without review.
test ! -e /home/amunoz/.config/org-overleaf-sync/config.json
/home/amunoz/.nix-profile/bin/python3 - <<'PY'
import json, os
from pathlib import Path
os.umask(0o077)
c = json.loads(Path('config/oppy.example.json').read_text())
c['target'] = {
    'project_id': '6acfad6134af14083d8c4c89',
    'url': 'https://overleaf.quasimorphic.com/git/6acfad6134af14083d8c4c89',
    'branch': 'master',
}
p = Path('/home/amunoz/.config/org-overleaf-sync/config.json')
with p.open('x') as f:
    f.write(json.dumps(c, indent=2) + '\n')
PY
/home/amunoz/.nix-profile/bin/python3 org_overleaf_sync.py preview \
  --config /home/amunoz/.config/org-overleaf-sync/config.json
# Inspect the returned build/slides.pdf, then explicitly approve first publication.
/home/amunoz/.nix-profile/bin/python3 org_overleaf_sync.py sync \
  --config /home/amunoz/.config/org-overleaf-sync/config.json
# Expect published, then no-change on the second invocation.
/home/amunoz/.nix-profile/bin/python3 org_overleaf_sync.py sync \
  --config /home/amunoz/.config/org-overleaf-sync/config.json
```

Parent now sets root `slides.tex` and compiler XeLaTeX through the deployed
application's native API or project settings, then validates Overleaf's compiled
PDF. The untouched initial `main.tex` is not the root after this step. Parent
owns the native API provisioning tooling; do not run another project's create
script. The service's local PDF uses the exact server TeX Live, but does not
replace this one-time server-side compile/root validation.

Config fields are absolute `source_dir`, `state_dir`, `emacs`, `tex_bin`, `qpdf`;
relative `org`; explicit relative `assets`; `timeout_seconds` (1–600); and `target`
(null for preview-only, otherwise exact `project_id`, `url`, `branch`). To publish
another deck/project, use a new config and new state directory, never retarget a
bound state directory. Org assets must be under `assets/`; paths and symlinks
are checked. Keep runtime config outside Git, mode 0600. Pin tool dependencies
in the host profile/GC roots so Nix garbage collection cannot remove them.

## Install and activate only after successful publication

```sh
cd /work/users/amunoz/projects/org-overleaf-sync
install -d -m 700 /home/amunoz/.config/systemd/user
sed \
  -e 's|@PYTHON@|/home/amunoz/.nix-profile/bin/python3|g' \
  -e 's|@REPOSITORY@|/work/users/amunoz/projects/org-overleaf-sync|g' \
  systemd/org-overleaf-sync.service.in \
  > /home/amunoz/.config/systemd/user/org-overleaf-sync.service
install -m 600 systemd/org-overleaf-sync.timer \
  /home/amunoz/.config/systemd/user/org-overleaf-sync.timer
systemd-analyze --user verify \
  /home/amunoz/.config/systemd/user/org-overleaf-sync.service \
  /home/amunoz/.config/systemd/user/org-overleaf-sync.timer
systemctl --user daemon-reload
systemctl --user start org-overleaf-sync.service
systemctl --user enable --now org-overleaf-sync.timer
systemctl --user list-timers org-overleaf-sync.timer
systemctl --user status org-overleaf-sync.service org-overleaf-sync.timer
loginctl show-user amunoz -p Linger
```

The timer runs every two minutes (up to 10 s jitter), including a catch-up trigger
after downtime. It is a user service, not a Pi/subagent job. To continue after
logout, the user manager must already linger (`Linger=yes`); if not, parent must
arrange the host-authorized `loginctl enable-linger amunoz` action. No sudo or
shared service changes are part of this repository. The service has a ten-minute
overall bound and kills the process group on timeout; each subprocess also has
a configured timeout. No autostart or persistent service was activated by tests.

## Status, logs, retention

```sh
python3 org_overleaf_sync.py status --config ~/.config/org-overleaf-sync/config.json
journalctl --user -u org-overleaf-sync.service --since today --no-pager
cat ~/.local/state/org-overleaf-sync/latest-build.json
```

- `status.json`: running, validated, published, no-change, failed, or recovery.
  A killed process may leave `running`; the service exit/journal is authoritative.
- `builds/candidate-*/`: incomplete/failed builds, including `export.log`,
  `build-1.log`, `build-2.log` where reached. A compiler failure never touches
  publication objects or live content.
- `builds/validated-*/`: checked PDF, logs, source hashes and exact bundle.
  `latest-build.json` names the latest successfully validated local build,
  **not necessarily the last successfully published build**.
- `baseline.json`: last acknowledged publication commit and exact owned Git
  blobs/modes; `binding.json`: immutable target binding; `pending.json`: push
  acknowledgment outstanding. Git output is deliberately not journaled because
  remote/helper errors can contain secrets; failures report phase/exit code.
- Successful runs retain five recent build directories and the last publication.
  Failed runs preserve diagnostics; repeated failures may require manual disk
  cleanup after inspection. Never delete baseline/binding/pending to bypass a
  conflict. No credentials belong in logs or evidence reports.

## Recovery (fail closed)

Stop the timer before troubleshooting:

```sh
systemctl --user stop org-overleaf-sync.timer
```

- **Export/build failure:** inspect candidate logs, correct Org/assets, preview,
  then manually sync. Previous remote content is untouched.
- **Owned upstream conflict:** do not reset the baseline or force push. Preserve
  the Overleaf edit, port the intended changes to Org, and with the collaborator's
  agreement restore the remote owned path to its last generated bytes in a normal
  remote commit. The next sync checks that baseline and publishes the Org change.
  This intentionally requires human reconciliation, not an automatic overwrite.
- **Unowned collision on first use:** rename/remove the conflicting remote path
  only after agreement, or choose a fresh project/state. Existing files are never
  silently adopted, even if their bytes happen to match the export.
- **Dirty publication checkout:** save and reconcile the local edits manually.
  Do not use it as an editing workspace. The exporter refuses to reset dirty work.
- **Push rejection/race/timeout:** inspect `pending.json` and remote history.
  On the next sync an exact pending commit already in remote ancestry is safely
  acknowledged (lost-ACK case); any subsequent owned remote edits still conflict.
  If the candidate did **not** reach the remote, explicitly discard just the
  pending transaction and rebuild on the current upstream:

  ```sh
  python3 org_overleaf_sync.py recover --config ~/.config/org-overleaf-sync/config.json
  python3 org_overleaf_sync.py sync --config ~/.config/org-overleaf-sync/config.json
  ```

  `recover` refuses to discard an already published candidate. It does not force
  push, rebase or change the remote; old owned hashes remain protected. A changed
  upstream owned file still fails after recovery. A failed push can have reached
  the server before the connection failed, so do not infer publication state from
  an error alone. No automatic retry/rebase occurs after a non-fast-forward.
- **Lock overlap:** another process is running. Wait/inspect systemd; do not remove
  the lock file while a process holds it (locks are automatically released on exit).

Once resolved, restart the timer with `systemctl --user start org-overleaf-sync.timer`.
Disabling automation never removes the private Overleaf project or source.

## Validation without live pushes

```sh
mkdir -p /work/users/amunoz/datasets/uoe_revision_20261005/org-overleaf-v1/test-tmp
TMPDIR=/work/users/amunoz/datasets/uoe_revision_20261005/org-overleaf-v1/test-tmp \
  PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

The suite covers real batch export/build/QPDF, repeat no-op, disabled Babel,
export/build failure, changed publication, owned and unowned upstream edits,
initial collision, remote parent symlink collision, asset traversal/symlinks,
dirty checkout, URL/branch/project allowlist, target rebinding, lock overlap,
command timeout, a real non-fast-forward rejection, simulated transport failure,
and simulated lost push acknowledgment. All pushes go to disposable bare remotes.
